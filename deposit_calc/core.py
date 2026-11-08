"""Net-return maths for Italian time deposits (conti deposito).

Money is handled as ``Decimal`` and every charge is rounded to the cent,
the way it appears on a bank statement.

Defaults follow the Italian rules for private individuals:

* ``WITHHOLDING_TAX_PCT`` (ritenuta sugli interessi): 26% of gross interest.
* ``STAMP_DUTY_PCT`` (imposta di bollo): 0.20% a year on the capital,
  charged pro rata for the period the money stays deposited.

Both are parameters, so other tax regimes can be simulated too.
Interest uses a simple months / 12 convention; a bank that counts days
(act/365) can differ by a few cents.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, fields
from datetime import date
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from enum import Enum
from pathlib import Path
from typing import Iterable, Union

Number = Union[int, float, str, Decimal]

CENT = Decimal("0.01")
HUNDRED = Decimal(100)
TWELVE = Decimal(12)

WITHHOLDING_TAX_PCT = Decimal("26")
STAMP_DUTY_PCT = Decimal("0.20")


def to_decimal(value: Number, field_name: str = "value") -> Decimal:
    """Convert ``value`` to a finite ``Decimal`` without float noise."""
    if isinstance(value, bool):
        raise TypeError(f"{field_name} must be a number, not a boolean")
    if isinstance(value, Decimal):
        result = value
    elif isinstance(value, float):
        result = Decimal(str(value))
    elif isinstance(value, (int, str)):
        try:
            result = Decimal(value)
        except InvalidOperation:
            raise ValueError(f"{field_name} is not a number: {value!r}") from None
    else:
        raise TypeError(f"{field_name} must be a number, got {type(value).__name__}")
    if not result.is_finite():
        raise ValueError(f"{field_name} must be a finite number, got {value!r}")
    return result


def round_cents(value: Decimal) -> Decimal:
    """Round to the cent, halves away from zero (as on bank statements)."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


class EarlyWithdrawal(str, Enum):
    """What happens to interest when money leaves before maturity (svincolo anticipato)."""

    FORFEIT_INTEREST = "forfeit_interest"
    """No interest on the withdrawn sum (the Crédit Agricole Italia rule)."""
    PRO_RATA = "pro_rata"
    """Interest accrues at the contract rate until the withdrawal."""
    REDUCED_RATE = "reduced_rate"
    """Interest accrues at a lower fallback rate (``reduced_rate_pct``)."""


@dataclass(frozen=True)
class DepositOffer:
    """One time-deposit offer: a rate locked for a fixed term.

    ``annual_costs`` covers other yearly euro costs the offer forces on you,
    such as the fee and stamp duty of a required current account; it is
    charged pro rata for the months the money is held.
    """

    bank: str
    gross_rate_pct: Decimal
    term_months: int
    name: str = ""
    stamp_duty_paid_by_bank: bool = False
    annual_costs: Decimal = Decimal(0)
    early_withdrawal: EarlyWithdrawal = EarlyWithdrawal.FORFEIT_INTEREST
    reduced_rate_pct: Decimal = Decimal(0)
    min_amount: Decimal | None = None
    max_amount: Decimal | None = None
    valid_until: date | None = None
    notes: str = ""

    def __post_init__(self) -> None:
        def set_field(name: str, value: object) -> None:
            object.__setattr__(self, name, value)

        if not isinstance(self.bank, str) or not self.bank.strip():
            raise ValueError("bank must be a non-empty name")
        if (
            isinstance(self.term_months, bool)
            or not isinstance(self.term_months, int)
            or self.term_months <= 0
        ):
            raise ValueError("term_months must be a positive whole number of months")

        for name in ("gross_rate_pct", "annual_costs", "reduced_rate_pct"):
            value = to_decimal(getattr(self, name), name)
            if value < 0:
                raise ValueError(f"{name} cannot be negative")
            set_field(name, value)

        for name in ("min_amount", "max_amount"):
            raw = getattr(self, name)
            if raw is not None:
                value = to_decimal(raw, name)
                if value < 0:
                    raise ValueError(f"{name} cannot be negative")
                set_field(name, value)
        if (
            self.min_amount is not None
            and self.max_amount is not None
            and self.min_amount > self.max_amount
        ):
            raise ValueError("min_amount cannot be greater than max_amount")

        try:
            set_field("early_withdrawal", EarlyWithdrawal(self.early_withdrawal))
        except ValueError:
            allowed = ", ".join(policy.value for policy in EarlyWithdrawal)
            raise ValueError(
                f"early_withdrawal must be one of: {allowed} (got {self.early_withdrawal!r})"
            ) from None

        if isinstance(self.valid_until, str):
            set_field("valid_until", date.fromisoformat(self.valid_until))
        elif self.valid_until is not None and not isinstance(self.valid_until, date):
            raise ValueError("valid_until must be a date or an ISO string (YYYY-MM-DD)")

    @property
    def label(self) -> str:
        """Short human-readable name, e.g. ``"Crédit Agricole 6m"``."""
        return f"{self.bank} {self.name}" if self.name else f"{self.bank} {self.term_months}m"

    def accepts(self, amount: Number) -> bool:
        """Whether ``amount`` is inside the offer's minimum and maximum."""
        value = to_decimal(amount, "amount")
        if self.min_amount is not None and value < self.min_amount:
            return False
        if self.max_amount is not None and value > self.max_amount:
            return False
        return True

    def is_expired(self, today: date | None = None) -> bool:
        """Whether the offer's ``valid_until`` date is in the past."""
        if self.valid_until is None:
            return False
        return (today or date.today()) > self.valid_until


@dataclass(frozen=True)
class DepositResult:
    """Breakdown of what a deposit earns, every charge already rounded to the cent."""

    offer: DepositOffer
    amount: Decimal
    months_held: Decimal
    matured: bool
    gross_interest: Decimal
    withholding_tax: Decimal
    stamp_duty: Decimal
    other_costs: Decimal

    @property
    def net_interest(self) -> Decimal:
        """What you keep: gross interest minus tax, stamp duty and other costs."""
        return self.gross_interest - self.withholding_tax - self.stamp_duty - self.other_costs

    @property
    def final_balance(self) -> Decimal:
        return self.amount + self.net_interest

    @property
    def net_annual_rate_pct(self) -> Decimal:
        """Net return as a yearly percentage (exact; round it for display)."""
        return self.net_interest / self.amount * TWELVE / self.months_held * HUNDRED

    def real_annual_rate_pct(self, inflation_pct: Number) -> Decimal:
        """Net yearly return after inflation (see ``real_rate_pct``)."""
        return real_rate_pct(self.net_annual_rate_pct, inflation_pct)

    def to_dict(self, today: date | None = None, inflation_pct: Number | None = None) -> dict:
        """JSON-ready dict. Money is given as strings to keep exact cents."""
        offer = self.offer
        real = None
        if inflation_pct is not None:
            real = str(
                self.real_annual_rate_pct(inflation_pct).quantize(
                    Decimal("0.0001"), rounding=ROUND_HALF_UP
                )
            )
        return {
            "offer": offer.label,
            "bank": offer.bank,
            "term_months": offer.term_months,
            "gross_rate_pct": str(offer.gross_rate_pct),
            "amount": str(self.amount),
            "months_held": str(self.months_held),
            "matured": self.matured,
            "gross_interest": str(self.gross_interest),
            "withholding_tax": str(self.withholding_tax),
            "stamp_duty": str(self.stamp_duty),
            "other_costs": str(self.other_costs),
            "net_interest": str(self.net_interest),
            "final_balance": str(self.final_balance),
            "net_annual_rate_pct": str(
                self.net_annual_rate_pct.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
            ),
            "real_annual_rate_pct": real,
            "valid_until": offer.valid_until.isoformat() if offer.valid_until else None,
            "expired": offer.is_expired(today),
        }


def real_rate_pct(nominal_pct: Number, inflation_pct: Number) -> Decimal:
    """Yearly return after inflation, in percent (Fisher equation).

    ``(1 + nominal) / (1 + inflation) - 1``: a 2.205% net return with 1.5%
    inflation is a real gain of about 0.69% a year in purchasing power.
    """
    nominal = to_decimal(nominal_pct, "nominal_pct") / HUNDRED
    inflation = to_decimal(inflation_pct, "inflation_pct") / HUNDRED
    if inflation <= -1:
        raise ValueError("inflation_pct must be greater than -100")
    return ((1 + nominal) / (1 + inflation) - 1) * HUNDRED


def simulate(
    offer: DepositOffer,
    amount: Number,
    *,
    months_held: Number | None = None,
    withholding_tax_pct: Number = WITHHOLDING_TAX_PCT,
    stamp_duty_pct: Number = STAMP_DUTY_PCT,
) -> DepositResult:
    """Simulate depositing ``amount`` in ``offer``.

    Without ``months_held`` the deposit is held to maturity. With it, the
    money leaves early and the offer's ``early_withdrawal`` policy decides
    how much interest is paid. Stamp duty and ``annual_costs`` are charged
    for the months actually held.
    """
    capital = to_decimal(amount, "amount")
    if capital <= 0:
        raise ValueError("amount must be greater than zero")
    if not offer.accepts(capital):
        raise ValueError(f"{offer.label} does not accept {capital} € ({_limits(offer)})")

    withholding = to_decimal(withholding_tax_pct, "withholding_tax_pct")
    if not 0 <= withholding <= 100:
        raise ValueError("withholding_tax_pct must be between 0 and 100")
    stamp_pct = to_decimal(stamp_duty_pct, "stamp_duty_pct")
    if stamp_pct < 0:
        raise ValueError("stamp_duty_pct cannot be negative")

    term = Decimal(offer.term_months)
    held = term if months_held is None else to_decimal(months_held, "months_held")
    if held <= 0 or held > term:
        raise ValueError(f"months_held must be more than 0 and at most {offer.term_months}")
    matured = held == term

    if matured or offer.early_withdrawal is EarlyWithdrawal.PRO_RATA:
        rate = offer.gross_rate_pct
    elif offer.early_withdrawal is EarlyWithdrawal.REDUCED_RATE:
        rate = offer.reduced_rate_pct
    else:
        rate = Decimal(0)

    years = held / TWELVE
    gross = round_cents(capital * rate / HUNDRED * years)
    tax = round_cents(gross * withholding / HUNDRED)
    stamp = (
        round_cents(Decimal(0))
        if offer.stamp_duty_paid_by_bank
        else round_cents(capital * stamp_pct / HUNDRED * years)
    )
    other = round_cents(offer.annual_costs * years)

    return DepositResult(
        offer=offer,
        amount=capital,
        months_held=held,
        matured=matured,
        gross_interest=gross,
        withholding_tax=tax,
        stamp_duty=stamp,
        other_costs=other,
    )


def compare(
    offers: Iterable[DepositOffer],
    amount: Number,
    *,
    withholding_tax_pct: Number = WITHHOLDING_TAX_PCT,
    stamp_duty_pct: Number = STAMP_DUTY_PCT,
) -> list[DepositResult]:
    """Simulate each offer that accepts ``amount``, held to maturity.

    Results are sorted best net annual rate first. Comparing yearly rates
    across different terms assumes the money can be reinvested at a similar
    rate when a shorter deposit ends. Offers whose limits exclude ``amount``
    are left out; use ``DepositOffer.accepts`` to list them.
    """
    results = [
        simulate(
            offer,
            amount,
            withholding_tax_pct=withholding_tax_pct,
            stamp_duty_pct=stamp_duty_pct,
        )
        for offer in offers
        if offer.accepts(amount)
    ]
    results.sort(key=lambda r: (r.net_annual_rate_pct, r.net_interest), reverse=True)
    return results


def load_offers(path: str | Path) -> list[DepositOffer]:
    """Read offers from a JSON file.

    The file holds either a list of offers or an object with an ``"offers"``
    list (other keys, such as ``"source"``, are ignored). Each offer uses the
    ``DepositOffer`` field names.
    """
    data = json.loads(Path(path).read_text(encoding="utf-8"), parse_float=Decimal)
    items = data.get("offers") if isinstance(data, dict) else data
    if not isinstance(items, list):
        raise ValueError(f"{path}: expected a list of offers or an object with an 'offers' list")

    known = {f.name for f in fields(DepositOffer)}
    offers = []
    for number, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"{path}: offer #{number} must be a JSON object")
        unknown = sorted(set(item) - known)
        if unknown:
            raise ValueError(f"{path}: offer #{number} has unknown field(s): {', '.join(unknown)}")
        try:
            offers.append(DepositOffer(**item))
        except (TypeError, ValueError) as error:
            raise ValueError(f"{path}: offer #{number}: {error}") from None
    return offers


def _limits(offer: DepositOffer) -> str:
    low = f"{offer.min_amount} €" if offer.min_amount is not None else "no minimum"
    high = f"{offer.max_amount} €" if offer.max_amount is not None else "no maximum"
    return f"{low} to {high}"
