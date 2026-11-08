import json
import os
import unittest
from datetime import date
from decimal import Decimal
from unittest import mock
from urllib.parse import parse_qs, urlparse

from deposit_calc.market_data import (
    API_KEY_ENV,
    FRED_OBSERVATIONS_URL,
    FredClient,
    FredError,
    ecb_deposit_rate,
    italy_inflation,
)

KEY = "abcdefghijklmnopqrstuvwxyz123456"


def observations(*pairs):
    return json.dumps(
        {"observations": [{"date": day, "value": value} for day, value in pairs]}
    ).encode()


class FakeFetch:
    def __init__(self, body):
        self.body = body
        self.urls = []

    def __call__(self, url):
        self.urls.append(url)
        if isinstance(self.body, Exception):
            raise self.body
        return self.body

    def params(self):
        query = parse_qs(urlparse(self.urls[-1]).query)
        return {name: values[0] for name, values in query.items()}


def client(body, api_key=KEY):
    fetch = FakeFetch(body)
    return FredClient(api_key, fetch=fetch, today=lambda: date(2026, 11, 8)), fetch


class FredClientTest(unittest.TestCase):
    def test_returns_the_latest_non_missing_value(self):
        fred, _ = client(observations(("2026-11-05", "2.50"), ("2026-11-06", "2.25"), ("2026-11-07", ".")))
        latest = fred.latest("ECBDFR")
        self.assertEqual(latest.date, date(2026, 11, 6))
        self.assertEqual(latest.value, Decimal("2.25"))
        self.assertEqual(latest.to_dict(), {"series_id": "ECBDFR", "date": "2026-11-06", "value": "2.25"})

    def test_request_calls_the_fred_api_directly_with_the_key(self):
        fred, fetch = client(observations(("2026-09-01", "1.6")))
        italy_inflation(fred)
        self.assertTrue(fetch.urls[0].startswith(FRED_OBSERVATIONS_URL + "?"))
        self.assertEqual(
            fetch.params(),
            {
                "series_id": "CP0000ITM086NEST",
                "api_key": KEY,
                "file_type": "json",
                "units": "pc1",
                "observation_start": "2023-11-09",
            },
        )

    def test_ecb_rate_uses_untransformed_units(self):
        fred, fetch = client(observations(("2026-11-06", "2.50")))
        self.assertEqual(ecb_deposit_rate(fred).value, Decimal("2.50"))
        self.assertEqual(fetch.params()["series_id"], "ECBDFR")
        self.assertEqual(fetch.params()["units"], "lin")

    def test_key_comes_from_the_environment(self):
        with mock.patch.dict(os.environ, {API_KEY_ENV: f"  {KEY}\n"}):
            fred = FredClient(fetch=FakeFetch(observations(("2026-11-06", "2.5"))))
        self.assertEqual(fred.latest("ECBDFR").value, Decimal("2.5"))
        self.assertNotIn(KEY, repr(fred))

    def test_missing_or_malformed_key_is_refused_before_any_request(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(FredError, API_KEY_ENV):
                FredClient()
        for bad in ("short", KEY.upper(), KEY + "0"):
            with self.subTest(key=bad), self.assertRaises(FredError):
                FredClient(bad)

    def test_api_errors_are_reported_without_the_key(self):
        body = json.dumps(
            {"error_code": 400, "error_message": f"Bad Request. api_key {KEY} is not registered."}
        ).encode()
        fred, _ = client(body)
        with self.assertRaises(FredError) as caught:
            fred.latest("ECBDFR")
        self.assertIn("not registered", str(caught.exception))
        self.assertNotIn(KEY, str(caught.exception))

    def test_fetch_errors_are_scrubbed_too(self):
        fred, _ = client(FredError(f"could not reach FRED for key {KEY}"))
        with self.assertRaises(FredError) as caught:
            fred.latest("ECBDFR")
        self.assertNotIn(KEY, str(caught.exception))

    def test_unusable_responses_raise_fred_error(self):
        for case, body in {
            "not json": b"<html>",
            "not an object": b"[]",
            "no observations": observations(),
            "only missing values": observations(("2026-11-06", ".")),
            "bad value": observations(("2026-11-06", "n/a")),
            "bad date": observations(("06/11/2026", "2.5")),
        }.items():
            fred, _ = client(body)
            with self.subTest(case=case), self.assertRaises(FredError):
                fred.latest("ECBDFR")


if __name__ == "__main__":
    unittest.main()
