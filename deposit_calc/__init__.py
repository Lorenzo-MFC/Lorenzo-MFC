"""deposit_calc: net return of Italian time deposits (conti deposito).

Quick use::

    from deposit_calc import DepositOffer, simulate

    offer = DepositOffer(bank="Crédit Agricole", gross_rate_pct="3.25", term_months=6)
    result = simulate(offer, 10_000)
    result.net_interest          # Decimal('110.25')
    result.net_annual_rate_pct   # Decimal('2.205')
"""

__version__ = "0.1.0"

from .core import (
    STAMP_DUTY_PCT,
    WITHHOLDING_TAX_PCT,
    DepositOffer,
    DepositResult,
    EarlyWithdrawal,
    compare,
    load_offers,
    real_rate_pct,
    simulate,
)

__all__ = [
    "STAMP_DUTY_PCT",
    "WITHHOLDING_TAX_PCT",
    "DepositOffer",
    "DepositResult",
    "EarlyWithdrawal",
    "compare",
    "load_offers",
    "real_rate_pct",
    "simulate",
]
# Live data from the FRED API lives in deposit_calc.market_data (needs FRED_API_KEY).
