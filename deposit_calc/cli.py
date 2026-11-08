"""Command line interface: ``deposit-calc net``, ``compare`` and ``benchmarks``."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path
from typing import Callable, Sequence

from . import __version__
from .core import (
    STAMP_DUTY_PCT,
    WITHHOLDING_TAX_PCT,
    DepositOffer,
    DepositResult,
    EarlyWithdrawal,
    _limits,
    compare,
    load_offers,
    simulate,
    to_decimal,
)
from .market_data import (
    API_KEY_ENV,
    ECB_DEPOSIT_RATE_SERIES,
    ITALY_HICP_SERIES,
    FredClient,
    FredError,
    Observation,
    ecb_deposit_rate,
    italy_inflation,
)


def _decimal(text: str) -> Decimal:
    try:
        return to_decimal(text, "number")
    except (TypeError, ValueError):
        raise argparse.ArgumentTypeError(
            f"not a number: {text!r} (use a dot for decimals, e.g. 3.25)"
        ) from None


def _positive_int(text: str) -> int:
    try:
        value = int(text)
    except ValueError:
        value = 0
    if value <= 0:
        raise argparse.ArgumentTypeError(f"must be a positive whole number: {text!r}")
    return value


def _iso_date(text: str) -> date:
    try:
        return date.fromisoformat(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a date in YYYY-MM-DD form: {text!r}") from None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="deposit-calc",
        description=(
            "Net return of Italian time deposits (conti deposito) after the 26%% "
            "withholding tax and the 0.20%% yearly stamp duty."
        ),
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    output = argparse.ArgumentParser(add_help=False)
    output.add_argument("--json", action="store_true", help="print JSON instead of a table")

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--amount", type=_decimal, required=True, help="capital to deposit, in euro"
    )
    common.add_argument(
        "--withholding-tax",
        type=_decimal,
        default=WITHHOLDING_TAX_PCT,
        metavar="PCT",
        help="tax on interest in percent (default: %(default)s)",
    )
    common.add_argument(
        "--stamp-duty",
        type=_decimal,
        default=STAMP_DUTY_PCT,
        metavar="PCT",
        help="yearly stamp duty on the capital in percent (default: %(default)s)",
    )
    inflation = common.add_mutually_exclusive_group()
    inflation.add_argument(
        "--inflation",
        type=_decimal,
        metavar="PCT",
        help="yearly inflation in percent, to show the real return",
    )
    inflation.add_argument(
        "--live",
        action="store_true",
        help=f"fetch Italian inflation and the ECB deposit rate from FRED (needs {API_KEY_ENV})",
    )

    commands = parser.add_subparsers(dest="command", required=True, metavar="COMMAND")

    net = commands.add_parser(
        "net",
        parents=[common, output],
        help="net return of one offer, optionally withdrawn early",
    )
    net.add_argument(
        "--rate", type=_decimal, required=True, help="gross yearly rate in percent, e.g. 3.25"
    )
    net.add_argument(
        "--months", type=_positive_int, required=True, help="length of the deposit in months"
    )
    net.add_argument("--bank", default="Deposit", help="name shown in the output")
    net.add_argument(
        "--bank-pays-stamp-duty",
        action="store_true",
        help="the bank covers the stamp duty instead of you",
    )
    net.add_argument(
        "--annual-costs",
        type=_decimal,
        default=Decimal(0),
        metavar="EURO",
        help="other yearly costs, e.g. a required current account (default: 0)",
    )
    net.add_argument(
        "--withdraw-after",
        type=_decimal,
        metavar="MONTHS",
        help="also show the result of withdrawing everything after this many months",
    )
    net.add_argument(
        "--early-policy",
        choices=[policy.value for policy in EarlyWithdrawal],
        default=EarlyWithdrawal.FORFEIT_INTEREST.value,
        help="interest paid on early withdrawal (default: %(default)s)",
    )
    net.add_argument(
        "--reduced-rate",
        type=_decimal,
        default=Decimal(0),
        metavar="PCT",
        help="yearly rate used by --early-policy reduced_rate (default: 0)",
    )

    ranking = commands.add_parser(
        "compare",
        parents=[common, output],
        help="rank the offers in a JSON file by net yearly return",
    )
    ranking.add_argument("offers_file", type=Path, help="JSON file of offers")
    ranking.add_argument(
        "--today",
        type=_iso_date,
        metavar="YYYY-MM-DD",
        help="date used to flag expired offers (default: today)",
    )

    commands.add_parser(
        "benchmarks",
        parents=[output],
        help=f"latest ECB deposit rate and Italian inflation from FRED (needs {API_KEY_ENV})",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    runners = {"net": _run_net, "compare": _run_compare, "benchmarks": _run_benchmarks}
    try:
        output = runners[args.command](args)
    except (OSError, ValueError, FredError) as error:
        print(f"deposit-calc: error: {error}", file=sys.stderr)
        return 1
    print(output)
    return 0


class _Benchmarks:
    """Inflation (and, when live, the ECB rate) used to put returns in context."""

    def __init__(self, args: argparse.Namespace) -> None:
        self.inflation_pct: Decimal | None = None
        self.inflation: Observation | None = None
        self.ecb_rate: Observation | None = None
        if getattr(args, "inflation", None) is not None:
            self.inflation_pct = args.inflation
        elif getattr(args, "live", False):
            client = FredClient()
            self.inflation = italy_inflation(client)
            self.ecb_rate = ecb_deposit_rate(client)
            self.inflation_pct = self.inflation.value

    def to_dict(self) -> dict | None:
        if self.inflation_pct is None:
            return None
        return {
            "inflation_pct": str(self.inflation_pct),
            "source": "fred" if self.inflation else "manual",
            "italy_inflation": self.inflation.to_dict() if self.inflation else None,
            "ecb_deposit_rate": self.ecb_rate.to_dict() if self.ecb_rate else None,
        }

    def lines(self) -> list[str]:
        if self.inflation_pct is None:
            return []
        if self.inflation is None:
            return [f"Inflation: {self.inflation_pct}% a year (from --inflation)"]
        return _benchmark_lines(self.ecb_rate, self.inflation)


def _benchmark_lines(ecb_rate: Observation | None, inflation: Observation) -> list[str]:
    lines = []
    if ecb_rate is not None:
        lines.append(
            f"ECB deposit facility rate: {_pct(ecb_rate.value)} "
            f"on {ecb_rate.date.isoformat()} (FRED {ECB_DEPOSIT_RATE_SERIES})"
        )
    lines.append(
        f"Italian inflation, year on year: {_pct(inflation.value)} "
        f"in {inflation.date:%Y-%m} (FRED {ITALY_HICP_SERIES})"
    )
    return lines


def _run_benchmarks(args: argparse.Namespace) -> str:
    client = FredClient()
    ecb_rate = ecb_deposit_rate(client)
    inflation = italy_inflation(client)
    if args.json:
        return json.dumps(
            {"ecb_deposit_rate": ecb_rate.to_dict(), "italy_inflation": inflation.to_dict()},
            indent=2,
        )
    return "\n".join(_benchmark_lines(ecb_rate, inflation))


def _run_net(args: argparse.Namespace) -> str:
    offer = DepositOffer(
        bank=args.bank,
        gross_rate_pct=args.rate,
        term_months=args.months,
        stamp_duty_paid_by_bank=args.bank_pays_stamp_duty,
        annual_costs=args.annual_costs,
        early_withdrawal=args.early_policy,
        reduced_rate_pct=args.reduced_rate,
    )
    rates = {"withholding_tax_pct": args.withholding_tax, "stamp_duty_pct": args.stamp_duty}
    at_maturity = simulate(offer, args.amount, **rates)
    early = None
    if args.withdraw_after is not None:
        early = simulate(offer, args.amount, months_held=args.withdraw_after, **rates)
    benchmarks = _Benchmarks(args)
    inflation = benchmarks.inflation_pct

    if args.json:
        return json.dumps(
            {
                "at_maturity": at_maturity.to_dict(inflation_pct=inflation),
                "early_withdrawal": early.to_dict(inflation_pct=inflation) if early else None,
                "benchmarks": benchmarks.to_dict(),
            },
            ensure_ascii=False,
            indent=2,
        )

    columns = [("At maturity", at_maturity)]
    if early:
        columns.append((f"Withdrawn after {early.months_held} months", early))
    header = (
        f"{offer.label}: {_pct(offer.gross_rate_pct)} gross for {offer.term_months} months "
        f"on {_money(at_maturity.amount)} €"
    )
    lines = [header, "", _breakdown(columns, args.withholding_tax, args.stamp_duty, inflation)]
    notes = benchmarks.lines()
    if early and offer.early_withdrawal is EarlyWithdrawal.FORFEIT_INTEREST:
        notes.append("Early withdrawal forfeits all interest; stamp duty is still charged.")
    if inflation is not None and at_maturity.real_annual_rate_pct(inflation) < 0:
        notes.append("The real return is negative: the deposit loses purchasing power.")
    if notes:
        lines += [""] + [f"- {note}" for note in notes]
    return "\n".join(lines)


def _run_compare(args: argparse.Namespace) -> str:
    offers = load_offers(args.offers_file)
    if not offers:
        raise ValueError(f"{args.offers_file}: the file contains no offers")
    today = args.today or date.today()
    results = compare(
        offers,
        args.amount,
        withholding_tax_pct=args.withholding_tax,
        stamp_duty_pct=args.stamp_duty,
    )
    skipped = [offer for offer in offers if not offer.accepts(args.amount)]
    benchmarks = _Benchmarks(args)
    inflation = benchmarks.inflation_pct

    if args.json:
        return json.dumps(
            {
                "amount": str(args.amount),
                "today": today.isoformat(),
                "benchmarks": benchmarks.to_dict(),
                "results": [result.to_dict(today, inflation) for result in results],
                "skipped": [{"offer": o.label, "limits": _limits(o)} for o in skipped],
            },
            ensure_ascii=False,
            indent=2,
        )

    lines = [
        f"Ranking for {_money(args.amount)} €, each offer held to maturity "
        "(best net yearly rate first)",
        "",
    ]
    if results:
        headers = ["#", "Offer", "Term", "Gross", "Net/yr"]
        if inflation is not None:
            headers.append("Real/yr")
        headers += ["Net interest", "Valid until"]
        rows = []
        for position, result in enumerate(results, start=1):
            offer = result.offer
            valid = offer.valid_until.isoformat() if offer.valid_until else "-"
            if offer.is_expired(today):
                valid += " EXPIRED"
            row = [
                str(position),
                offer.label,
                f"{offer.term_months}m",
                _pct(offer.gross_rate_pct),
                _pct(result.net_annual_rate_pct),
            ]
            if inflation is not None:
                row.append(_pct(result.real_annual_rate_pct(inflation)))
            row += [_money(result.net_interest), valid]
            rows.append(row)
        right = set(range(len(headers) - 1)) - {1}
        lines.append(_table(headers, rows, right_aligned=right))
    else:
        lines.append("No offer accepts this amount.")

    notes = benchmarks.lines()
    if skipped:
        notes.append(
            "Skipped, amount outside the offer's limits: "
            + "; ".join(f"{o.label} ({_limits(o)})" for o in skipped)
        )
    if any(result.offer.is_expired(today) for result in results):
        notes.append(
            "EXPIRED offers are past their valid_until date: check the bank's current terms."
        )
    if inflation is not None and any(r.real_annual_rate_pct(inflation) < 0 for r in results):
        notes.append("A negative real rate means the deposit loses purchasing power.")
    if len({result.offer.term_months for result in results}) > 1:
        notes.append(
            "Yearly rates of different terms assume you can reinvest at a similar rate."
        )
    if notes:
        lines += [""] + [f"- {note}" for note in notes]
    return "\n".join(lines)


def _breakdown(
    columns: list[tuple[str, DepositResult]],
    withholding: Decimal,
    stamp_pct: Decimal,
    inflation: Decimal | None = None,
) -> str:
    offer = columns[0][1].offer
    stamp_label = (
        "Stamp duty (paid by bank)" if offer.stamp_duty_paid_by_bank else f"Stamp duty {stamp_pct}%"
    )
    rows: list[tuple[str, Callable[[DepositResult], str]]] = [
        ("Gross interest", lambda r: _money(r.gross_interest)),
        (f"Withholding tax {withholding}%", lambda r: _minus(r.withholding_tax)),
        (stamp_label, lambda r: _minus(r.stamp_duty)),
        ("Other costs", lambda r: _minus(r.other_costs)),
        ("Net interest", lambda r: _money(r.net_interest)),
        ("Final balance", lambda r: _money(r.final_balance)),
        ("Net yearly rate", lambda r: _pct(r.net_annual_rate_pct)),
    ]
    if inflation is not None:
        rows.append(
            (
                f"Real yearly rate ({inflation}% inflation)",
                lambda r: _pct(r.real_annual_rate_pct(inflation)),
            )
        )
    body = [[label] + [render(result) for _, result in columns] for label, render in rows]
    headers = [""] + [title for title, _ in columns]
    return _table(headers, body, right_aligned=set(range(1, len(headers))))


def _table(headers: list[str], rows: list[list[str]], right_aligned: set[int]) -> str:
    widths = [max(len(row[i]) for row in [headers] + rows) for i in range(len(headers))]

    def render(row: list[str]) -> str:
        cells = [
            cell.rjust(widths[i]) if i in right_aligned else cell.ljust(widths[i])
            for i, cell in enumerate(row)
        ]
        return "  ".join(cells).rstrip()

    return "\n".join(render(row) for row in [headers] + rows)


def _money(value: Decimal) -> str:
    return f"{value:,.2f}"


def _minus(value: Decimal) -> str:
    return _money(-value) if value else _money(value)


def _pct(value: Decimal) -> str:
    return f"{value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}%"
