# deposit-calc

Works out what an Italian **conto deposito** really pays you once tax, stamp duty, extra
costs, early withdrawal and inflation are counted. You can use it from the command line
or as a Python library. It needs nothing beyond the Python standard library (tested on
Python 3.13).

- **Net return**: gross interest, minus the 26% withholding tax (*ritenuta*), minus the
  0.20% yearly stamp duty (*imposta di bollo*) charged pro rata, minus any other costs,
  such as the current account a bank makes you open.
- **Early withdrawal** (*svincolo anticipato*): forfeit all interest (the Crédit Agricole
  rule), pro rata, or a reduced fallback rate.
- **Comparison**: ranks offers from a JSON file by net yearly rate and flags expired
  promotions.
- **Real return**: the net rate after inflation, using a figure you give it or live data.
- **Live data with your own API key**: the latest ECB deposit facility rate and Italian
  inflation (HICP, year on year), fetched straight from the FRED HTTP API. It sends
  plain HTTPS requests and uses no MCP server or other middleman.

Money is handled as exact decimals and each charge is rounded to the cent. Programs get
exact strings when they ask for `--json`.

## Run it

From the repository root, with no install needed:

```bash
python3 -m deposit_calc net --rate 3.25 --months 6 --amount 10000 --withdraw-after 3 --inflation 1.5
```

```
Deposit 6m: 3.25% gross for 6 months on 10,000.00 €

                                   At maturity  Withdrawn after 3 months
Gross interest                          162.50                      0.00
Withholding tax 26%                     -42.25                      0.00
Stamp duty 0.20%                        -10.00                     -5.00
Other costs                               0.00                      0.00
Net interest                            110.25                     -5.00
Final balance                        10,110.25                  9,995.00
Net yearly rate                          2.21%                    -0.20%
Real yearly rate (1.5% inflation)        0.69%                    -1.67%

- Inflation: 1.5% a year (from --inflation)
- Early withdrawal forfeits all interest; stamp duty is still charged.
```

Compare the offers in a file:

```bash
python3 -m deposit_calc compare examples/credit-agricole-2026-08.json --amount 50000
```

```
Ranking for 50,000.00 €, each offer held to maturity (best net yearly rate first)

#  Offer                   Term  Gross  Net/yr  Net interest  Valid until
1  Crédit Agricole 4 mesi    4m  3.75%   2.58%        429.17  2026-09-30 EXPIRED
2  Crédit Agricole 6 mesi    6m  3.25%   2.21%        551.25  2026-09-30 EXPIRED
3  Crédit Agricole 9 mesi    9m  2.75%   1.83%        688.12  2026-09-30 EXPIRED

- EXPIRED offers are past their valid_until date: check the bank's current terms.
- Yearly rates of different terms assume you can reinvest at a similar rate.
```

To get a `deposit-calc` command, install it with `pip install .`. Run
`deposit-calc --help` (or `deposit-calc net --help`) to see every option.

## Live data from FRED, with your API key

1. Get a free API key at <https://fred.stlouisfed.org/docs/api/api_key.html>. It's 32
   lowercase letters and digits.
2. Put it in an environment variable. Never put it in a file you commit; `.env` is
   already git-ignored.

   ```bash
   export FRED_API_KEY=your32characterkey
   ```

3. Use `--live` on `net` or `compare`, or ask for the benchmarks on their own:

   ```bash
   python3 -m deposit_calc benchmarks
   python3 -m deposit_calc compare examples/credit-agricole-2026-08.json --amount 50000 --live
   ```

`--live` adds a **Real/yr** column (or row) and prints both benchmarks with their dates.
It uses the FRED series `ECBDFR` (ECB Deposit Facility Rate for Euro Area) and
`CP0000ITM086NEST` (Harmonized Index of Consumer Prices: Total for Italy) with
`units=pc1` (percent change from a year ago). Without a key, `--inflation PCT` gives the
same real-return view offline.

FRED takes the key as a URL parameter. The client strips it from every error message and
never prints it.

## Use it from Python

```python
from deposit_calc import DepositOffer, compare, load_offers, simulate

offer = DepositOffer(bank="Crédit Agricole", gross_rate_pct="3.25", term_months=6)
result = simulate(offer, 10_000)
result.net_interest                 # Decimal('110.25')
result.net_annual_rate_pct          # Decimal('2.205')
result.real_annual_rate_pct("1.5")  # about 0.69

early = simulate(offer, 10_000, months_held=3)  # early_withdrawal policy applies
ranked = compare(load_offers("examples/credit-agricole-2026-08.json"), 50_000)
```

```python
from deposit_calc.market_data import FredClient, ecb_deposit_rate, italy_inflation

fred = FredClient()                 # reads FRED_API_KEY
italy_inflation(fred)               # Observation(series_id, date, value)
ecb_deposit_rate(fred)
```

To test without the network, pass `FredClient(fetch=...)` a function that takes a URL
and returns the response bytes.

## Offer file format

A JSON list of offers, or an object with an `"offers"` list (other keys, such as
`"source"`, are ignored):

| Field | Required | Meaning |
|---|---|---|
| `bank` | yes | Bank name |
| `gross_rate_pct` | yes | Gross yearly rate in percent, e.g. `3.25` |
| `term_months` | yes | Length of the deposit in whole months |
| `name` | no | Label for the offer, e.g. `"6 mesi"` |
| `stamp_duty_paid_by_bank` | no | `true` if the bank covers the 0.20% stamp duty |
| `annual_costs` | no | Other yearly euro costs, e.g. the required current account |
| `early_withdrawal` | no | `forfeit_interest` (default), `pro_rata` or `reduced_rate` |
| `reduced_rate_pct` | no | Yearly rate used by `reduced_rate` |
| `min_amount`, `max_amount` | no | Euro limits the rate applies to |
| `valid_until` | no | Last day of the offer, `YYYY-MM-DD` |
| `notes` | no | Free text |

`examples/credit-agricole-2026-08.json` holds the rates from
[the August 2026 research](../credit-agricole-prodotti-finanziari-conti-deposito.md).
That promotion ended on 30 September 2026, so update the file with current rates before
relying on it.

## Assumptions and limits

- Interest is simple interest over months / 12. A bank that counts days (act/365) can
  differ by a few cents.
- The defaults are the rules for private individuals in Italy: 26% tax on deposit
  interest and 0.20% yearly stamp duty. Change them with `--withholding-tax` and
  `--stamp-duty`.
- The real rate uses the latest year-on-year inflation, which looks backward. Future
  inflation can differ.
- This is a calculator, not financial advice. The bank's official information sheet
  (*foglio informativo*) is what counts.

## Tests

```bash
python3 -m unittest
```

The FRED tests use a fake HTTP layer, so they need neither network access nor an API key.
