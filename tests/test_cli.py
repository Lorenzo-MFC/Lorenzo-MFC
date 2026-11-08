import contextlib
import io
import json
import os
import unittest
from pathlib import Path
from unittest import mock

from deposit_calc.cli import main
from deposit_calc.market_data import API_KEY_ENV

EXAMPLES = str(Path(__file__).resolve().parent.parent / "examples" / "credit-agricole-2026-08.json")
KEY = "abcdefghijklmnopqrstuvwxyz123456"


def run(*argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(list(argv))
    return code, out.getvalue(), err.getvalue()


def fake_fred(url):
    """Stand-in for the FRED API: 2.50% ECB rate, 1.6% Italian inflation."""
    if "series_id=ECBDFR" in url:
        rows = [{"date": "2026-11-06", "value": "2.50"}]
    else:
        rows = [{"date": "2026-08-01", "value": "1.4"}, {"date": "2026-09-01", "value": "1.6"}]
    return json.dumps({"observations": rows}).encode()


@contextlib.contextmanager
def live_fred():
    with mock.patch.dict(os.environ, {API_KEY_ENV: KEY}), mock.patch(
        "deposit_calc.market_data.http_fetch", side_effect=fake_fred
    ) as fetch:
        yield fetch


class NetCommandTest(unittest.TestCase):
    def test_text_breakdown(self):
        code, out, _ = run("net", "--rate", "3.25", "--months", "6", "--amount", "10000")
        self.assertEqual(code, 0)
        self.assertIn("110.25", out)
        self.assertIn("2.21%", out)
        self.assertIn("-42.25", out)

    def test_json_with_early_withdrawal_and_manual_inflation(self):
        code, out, _ = run(
            "net", "--rate", "3.25", "--months", "6", "--amount", "10000",
            "--withdraw-after", "3", "--inflation", "1.5", "--json",
        )
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual(data["at_maturity"]["net_interest"], "110.25")
        self.assertEqual(data["at_maturity"]["real_annual_rate_pct"], "0.6946")
        self.assertEqual(data["early_withdrawal"]["net_interest"], "-5.00")
        self.assertEqual(data["benchmarks"]["source"], "manual")

    def test_negative_real_return_is_flagged(self):
        _, out, _ = run("net", "--rate", "1", "--months", "12", "--amount", "1000", "--inflation", "3")
        self.assertIn("loses purchasing power", out)

    def test_domain_errors_exit_with_1(self):
        code, _, err = run("net", "--rate", "3", "--months", "6", "--amount", "1000", "--withdraw-after", "9")
        self.assertEqual(code, 1)
        self.assertIn("months_held", err)

    def test_usage_errors_exit_with_2(self):
        for argv in (
            ["net", "--rate", "3", "--months", "6"],
            ["net", "--rate", "3,25", "--months", "6", "--amount", "1"],
            ["net", "--rate", "3", "--months", "0", "--amount", "1"],
            ["net", "--rate", "3", "--months", "6", "--amount", "1", "--inflation", "2", "--live"],
        ):
            with self.subTest(argv=argv), self.assertRaises(SystemExit) as caught:
                run(*argv)
            self.assertEqual(caught.exception.code, 2)


class CompareCommandTest(unittest.TestCase):
    def test_ranks_the_example_offers_and_flags_expired_ones(self):
        code, out, _ = run("compare", EXAMPLES, "--amount", "50000", "--today", "2026-11-08")
        self.assertEqual(code, 0)
        lines = out.splitlines()
        self.assertTrue(lines[3].startswith("1  Crédit Agricole 4 mesi"))
        self.assertIn("EXPIRED", out)

    def test_json_reports_skipped_offers(self):
        code, out, _ = run("compare", EXAMPLES, "--amount", "2000000", "--json", "--today", "2026-09-01")
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual([r["term_months"] for r in data["results"]], [4, 9])
        self.assertEqual(data["skipped"][0]["offer"], "Crédit Agricole 6 mesi")
        self.assertFalse(data["results"][0]["expired"])

    def test_missing_file_exits_with_1(self):
        code, _, err = run("compare", "no-such-file.json", "--amount", "1000")
        self.assertEqual(code, 1)
        self.assertIn("no-such-file.json", err)


class LiveDataTest(unittest.TestCase):
    def test_compare_live_adds_real_rates_and_benchmarks(self):
        with live_fred() as fetch:
            code, out, _ = run("compare", EXAMPLES, "--amount", "50000", "--live", "--today", "2026-11-08")
        self.assertEqual(code, 0)
        self.assertEqual(fetch.call_count, 2)
        self.assertIn("Real/yr", out)
        self.assertIn("ECB deposit facility rate: 2.50% on 2026-11-06", out)
        self.assertIn("Italian inflation, year on year: 1.60% in 2026-09", out)

    def test_net_live_json(self):
        with live_fred():
            code, out, _ = run("net", "--rate", "3.25", "--months", "6", "--amount", "10000", "--live", "--json")
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual(data["benchmarks"]["source"], "fred")
        self.assertEqual(data["benchmarks"]["ecb_deposit_rate"]["value"], "2.50")
        self.assertEqual(data["at_maturity"]["real_annual_rate_pct"], "0.5955")

    def test_benchmarks_command(self):
        with live_fred():
            code, out, _ = run("benchmarks", "--json")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)["italy_inflation"]["value"], "1.6")

    def test_live_without_a_key_explains_how_to_set_it(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            code, _, err = run("benchmarks")
        self.assertEqual(code, 1)
        self.assertIn(API_KEY_ENV, err)


if __name__ == "__main__":
    unittest.main()
