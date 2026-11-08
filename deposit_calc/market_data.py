"""Live benchmarks from the FRED API (Federal Reserve Bank of St. Louis).

The code calls the FRED HTTP API directly with your own API key; no MCP
server or other middleman is involved. Get a free key at
https://fred.stlouisfed.org/docs/api/api_key.html and export it::

    export FRED_API_KEY=your32characterlowercasekey

Keep the key in the environment (or a git-ignored ``.env``), never in the
repository. FRED takes the key as a query parameter, so it never appears in
this module's error messages.
"""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
from typing import Callable
from urllib.parse import urlencode

from . import __version__

FRED_OBSERVATIONS_URL = "https://api.stlouisfed.org/fred/series/observations"
API_KEY_ENV = "FRED_API_KEY"

ECB_DEPOSIT_RATE_SERIES = "ECBDFR"
"""ECB Deposit Facility Rate for Euro Area, percent, daily."""
ITALY_HICP_SERIES = "CP0000ITM086NEST"
"""Harmonized Index of Consumer Prices: Total for Italy, monthly index."""

YEAR_ON_YEAR = "pc1"
"""FRED ``units`` value: percent change from a year ago."""

Fetcher = Callable[[str], bytes]
"""Takes a full request URL and returns the raw response body."""


class FredError(RuntimeError):
    """FRED could not be reached or did not return usable data."""


@dataclass(frozen=True)
class Observation:
    series_id: str
    date: date
    value: Decimal

    def to_dict(self) -> dict:
        return {"series_id": self.series_id, "date": self.date.isoformat(), "value": str(self.value)}


def http_fetch(url: str, timeout: float = 15.0) -> bytes:
    """Default fetcher: one HTTPS GET with the standard library."""
    request = urllib.request.Request(url, headers={"User-Agent": f"deposit-calc/{__version__}"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as error:
        raise FredError(_api_error_message(error.read(), f"HTTP {error.code}")) from None
    except urllib.error.URLError as error:
        raise FredError(f"could not reach FRED: {error.reason}") from None
    except TimeoutError:
        raise FredError("FRED did not answer in time") from None


class FredClient:
    """Minimal client for FRED's ``series/observations`` endpoint.

    ``api_key`` defaults to the ``FRED_API_KEY`` environment variable.
    ``fetch`` and ``today`` can be replaced, which is how the tests run
    without network access.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        fetch: Fetcher | None = None,
        today: Callable[[], date] = date.today,
    ) -> None:
        key = (api_key if api_key is not None else os.environ.get(API_KEY_ENV, "")).strip()
        if not key:
            raise FredError(
                f"no FRED API key: set the {API_KEY_ENV} environment variable "
                "(free key at https://fred.stlouisfed.org/docs/api/api_key.html)"
            )
        if not re.fullmatch(r"[a-z0-9]{32}", key):
            raise FredError(
                f"{API_KEY_ENV} does not look like a FRED API key "
                "(expected 32 lowercase letters and digits)"
            )
        self._key = key
        self._fetch = fetch or http_fetch
        self._today = today

    def __repr__(self) -> str:
        return "FredClient(api_key=***)"

    def latest(self, series_id: str, *, units: str = "lin", years_back: int = 3) -> Observation:
        """Most recent non-missing value of ``series_id``.

        The request covers the last ``years_back`` years so transformed
        units such as ``pc1`` (year-on-year change) have enough history.
        """
        params = {
            "series_id": series_id,
            "api_key": self._key,
            "file_type": "json",
            "units": units,
            "observation_start": (self._today() - timedelta(days=365 * years_back)).isoformat(),
        }
        try:
            body = self._fetch(f"{FRED_OBSERVATIONS_URL}?{urlencode(params)}")
        except FredError as error:
            raise FredError(self._scrub(str(error))) from None
        try:
            payload = json.loads(body)
        except (UnicodeDecodeError, json.JSONDecodeError):
            raise FredError(f"FRED sent a response that is not JSON for {series_id}") from None
        if not isinstance(payload, dict):
            raise FredError(f"unexpected FRED response for {series_id}")
        if "error_message" in payload:
            raise FredError(self._scrub(_api_error_message(body, "FRED error")))

        for item in reversed(payload.get("observations") or []):
            raw = str(item.get("value", ".")).strip()
            if raw in ("", "."):  # FRED marks missing values with "."
                continue
            try:
                return Observation(series_id, date.fromisoformat(item["date"]), Decimal(raw))
            except (KeyError, ValueError, InvalidOperation):
                raise FredError(f"unexpected observation in FRED data for {series_id}") from None
        raise FredError(f"FRED returned no values for {series_id}")

    def _scrub(self, message: str) -> str:
        return message.replace(self._key, "***")


def ecb_deposit_rate(client: FredClient) -> Observation:
    """Latest ECB deposit facility rate, in percent."""
    return client.latest(ECB_DEPOSIT_RATE_SERIES)


def italy_inflation(client: FredClient) -> Observation:
    """Latest Italian HICP inflation, year-on-year, in percent."""
    return client.latest(ITALY_HICP_SERIES, units=YEAR_ON_YEAR)


def _api_error_message(body: bytes, fallback: str) -> str:
    try:
        payload = json.loads(body)
        message = payload.get("error_message") if isinstance(payload, dict) else None
    except (UnicodeDecodeError, json.JSONDecodeError):
        message = None
    return f"FRED: {message}" if message else f"FRED request failed ({fallback})"
