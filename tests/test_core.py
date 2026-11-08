import json
import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

from deposit_calc import (
    DepositOffer,
    EarlyWithdrawal,
    compare,
    load_offers,
    real_rate_pct,
    simulate,
)

EXAMPLES = Path(__file__).resolve().parent.parent / "examples" / "credit-agricole-2026-08.json"


def offer(**overrides):
    fields = {"bank": "Crédit Agricole", "gross_rate_pct": "3.25", "term_months": 6}
    fields.update(overrides)
    return DepositOffer(**fields)


class SimulateAtMaturityTest(unittest.TestCase):
    def test_matches_the_research_document_example(self):
        # The research doc says 3.25% gross for 6 months is about 2.21% net a year.
        result = simulate(offer(), 10_000)
        self.assertEqual(result.gross_interest, Decimal("162.50"))
        self.assertEqual(result.withholding_tax, Decimal("42.25"))
        self.assertEqual(result.stamp_duty, Decimal("10.00"))
        self.assertEqual(result.other_costs, Decimal("0.00"))
        self.assertEqual(result.net_interest, Decimal("110.25"))
        self.assertEqual(result.final_balance, Decimal("10110.25"))
        self.assertEqual(result.net_annual_rate_pct, Decimal("2.205"))
        self.assertTrue(result.matured)

    def test_bank_paying_stamp_duty_raises_the_net(self):
        result = simulate(offer(stamp_duty_paid_by_bank=True), 10_000)
        self.assertEqual(result.stamp_duty, Decimal("0.00"))
        self.assertEqual(result.net_interest, Decimal("120.25"))

    def test_annual_costs_are_charged_pro_rata(self):
        # e.g. 34.20 € a year of current-account stamp duty, for 6 months.
        result = simulate(offer(annual_costs="34.20"), 10_000)
        self.assertEqual(result.other_costs, Decimal("17.10"))
        self.assertEqual(result.net_interest, Decimal("93.15"))

    def test_tax_and_stamp_duty_rates_are_configurable(self):
        result = simulate(offer(), 10_000, withholding_tax_pct="12.5", stamp_duty_pct=0)
        self.assertEqual(result.withholding_tax, Decimal("20.31"))  # 20.3125 rounded
        self.assertEqual(result.stamp_duty, Decimal("0.00"))

    def test_float_inputs_do_not_leak_binary_noise(self):
        result = simulate(offer(gross_rate_pct=3.25), 10_000.10)
        self.assertEqual(result.offer.gross_rate_pct, Decimal("3.25"))
        self.assertEqual(result.amount, Decimal("10000.1"))

    def test_zero_rate_deposit_only_costs_stamp_duty(self):
        result = simulate(offer(gross_rate_pct=0), 10_000)
        self.assertEqual(result.net_interest, Decimal("-10.00"))


class EarlyWithdrawalTest(unittest.TestCase):
    def test_forfeit_keeps_stamp_duty_but_pays_no_interest(self):
        result = simulate(offer(), 10_000, months_held=3)
        self.assertFalse(result.matured)
        self.assertEqual(result.gross_interest, Decimal("0.00"))
        self.assertEqual(result.withholding_tax, Decimal("0.00"))
        self.assertEqual(result.stamp_duty, Decimal("5.00"))
        self.assertEqual(result.net_interest, Decimal("-5.00"))

    def test_pro_rata_pays_the_contract_rate_until_withdrawal(self):
        result = simulate(offer(early_withdrawal="pro_rata"), 10_000, months_held=3)
        self.assertEqual(result.gross_interest, Decimal("81.25"))
        self.assertEqual(result.withholding_tax, Decimal("21.13"))  # 21.125 rounds half up
        self.assertEqual(result.net_interest, Decimal("55.12"))

    def test_reduced_rate_uses_the_fallback_rate(self):
        reduced = offer(early_withdrawal=EarlyWithdrawal.REDUCED_RATE, reduced_rate_pct=1)
        result = simulate(reduced, 10_000, months_held=3)
        self.assertEqual(result.gross_interest, Decimal("25.00"))
        self.assertEqual(result.net_interest, Decimal("13.50"))

    def test_holding_the_full_term_counts_as_maturity(self):
        result = simulate(offer(), 10_000, months_held=6)
        self.assertTrue(result.matured)
        self.assertEqual(result.net_interest, Decimal("110.25"))

    def test_fractional_months_are_allowed(self):
        result = simulate(offer(early_withdrawal="pro_rata"), 12_000, months_held="1.5")
        self.assertEqual(result.gross_interest, Decimal("48.75"))


class ValidationTest(unittest.TestCase):
    def test_bad_simulation_inputs_are_rejected(self):
        for kwargs in (
            {"amount": 0},
            {"amount": -100},
            {"amount": 1000, "months_held": 0},
            {"amount": 1000, "months_held": 7},
            {"amount": 1000, "withholding_tax_pct": 101},
            {"amount": 1000, "stamp_duty_pct": -1},
            {"amount": "abc"},
        ):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                simulate(offer(), **kwargs)

    def test_bad_offers_are_rejected(self):
        for overrides in (
            {"bank": " "},
            {"gross_rate_pct": -1},
            {"term_months": 0},
            {"term_months": 2.5},
            {"term_months": True},
            {"annual_costs": -5},
            {"min_amount": 5000, "max_amount": 1000},
            {"early_withdrawal": "sometimes"},
            {"gross_rate_pct": "nan"},
        ):
            with self.subTest(overrides=overrides), self.assertRaises(ValueError):
                offer(**overrides)

    def test_boolean_is_not_a_number(self):
        with self.assertRaises(TypeError):
            offer(gross_rate_pct=True)

    def test_amount_outside_the_offer_limits_is_rejected(self):
        capped = offer(max_amount=1_000_000)
        self.assertFalse(capped.accepts(1_000_001))
        with self.assertRaises(ValueError):
            simulate(capped, 1_000_001)


class OfferTest(unittest.TestCase):
    def test_label_and_expiry(self):
        promo = offer(name="6 mesi", valid_until="2026-09-30")
        self.assertEqual(promo.label, "Crédit Agricole 6 mesi")
        self.assertEqual(offer().label, "Crédit Agricole 6m")
        self.assertEqual(promo.valid_until, date(2026, 9, 30))
        self.assertFalse(promo.is_expired(date(2026, 9, 30)))
        self.assertTrue(promo.is_expired(date(2026, 10, 1)))
        self.assertFalse(offer().is_expired())


class CompareTest(unittest.TestCase):
    def test_ranks_by_net_yearly_rate_and_skips_ineligible_offers(self):
        offers = [
            offer(name="9m", gross_rate_pct="2.75", term_months=9),
            offer(name="4m", gross_rate_pct="3.75", term_months=4),
            offer(name="capped", gross_rate_pct="5", max_amount=1000),
        ]
        ranked = compare(offers, 50_000)
        self.assertEqual([r.offer.name for r in ranked], ["4m", "9m"])
        self.assertEqual(ranked[0].net_interest, Decimal("429.17"))


class RealRateTest(unittest.TestCase):
    def test_fisher_equation(self):
        self.assertEqual(real_rate_pct(0, 0), Decimal(0))
        self.assertAlmostEqual(float(real_rate_pct("2.205", "1.5")), 0.6946, places=4)
        self.assertLess(real_rate_pct(2, 3), 0)

    def test_result_real_rate_and_dict(self):
        result = simulate(offer(), 10_000)
        data = result.to_dict(date(2026, 11, 8), inflation_pct="1.5")
        self.assertEqual(data["net_annual_rate_pct"], "2.2050")
        self.assertEqual(data["real_annual_rate_pct"], "0.6946")
        self.assertEqual(data["net_interest"], "110.25")
        self.assertIsNone(result.to_dict()["real_annual_rate_pct"])

    def test_inflation_of_minus_100_is_rejected(self):
        with self.assertRaises(ValueError):
            real_rate_pct(2, -100)


class LoadOffersTest(unittest.TestCase):
    def test_example_file_loads_with_exact_decimals(self):
        offers = load_offers(EXAMPLES)
        self.assertEqual([o.term_months for o in offers], [4, 6, 9])
        self.assertEqual(offers[1].gross_rate_pct, Decimal("3.25"))
        self.assertEqual(offers[1].max_amount, Decimal("1000000"))
        self.assertEqual(offers[0].valid_until, date(2026, 9, 30))

    def _load(self, data):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "offers.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return load_offers(path)

    def test_a_plain_list_is_accepted(self):
        offers = self._load([{"bank": "B", "gross_rate_pct": 3, "term_months": 12}])
        self.assertEqual(offers[0].bank, "B")

    def test_unknown_missing_and_invalid_fields_are_reported(self):
        cases = {
            "unknown field": [{"bank": "B", "gross_rate_pct": 3, "term_months": 12, "rate": 3}],
            "missing field": [{"bank": "B", "gross_rate_pct": 3}],
            "invalid value": [{"bank": "B", "gross_rate_pct": -3, "term_months": 12}],
            "not an object": ["B"],
            "wrong shape": {"deposits": []},
        }
        for case, data in cases.items():
            with self.subTest(case=case), self.assertRaises(ValueError):
                self._load(data)


if __name__ == "__main__":
    unittest.main()
