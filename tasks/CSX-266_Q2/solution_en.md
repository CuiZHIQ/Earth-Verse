# Solution

## Correct Answer

```json
{
  "answer": "december_margin_confirmed",
  "dominant_month": "2019-12",
  "ledger": {
    "heat_days_ge_40c": 20,
    "dry_fraction": 0.935,
    "wind_days_ge_35kmh": 3,
    "hot_windy_days": 2,
    "precip_total_mm": 0.4,
    "peak_tmax_c": 46.0
  },
  "diagnostic_index": 79.6,
  "margin_vs_january": 29.7,
  "margin_vs_november": 30.3
}
```

## Computation

The daily weather series is aggregated by calendar month for 2019-09 through 2020-02. The diagnostic index is:

```text
I = 2*heat_days_ge_40c
    + 20*dry_fraction
    + 2*wind_days_ge_35kmh
    + 3*hot_windy_days
    + 1.5*max(0, peak_tmax_c - 40)
    - 0.2*min(precip_total_mm, 50)
```

For 2019-12, the ledger is:

```text
heat_days_ge_40c = 20
dry_fraction = 29 / 31 = 0.935
wind_days_ge_35kmh = 3
hot_windy_days = 2
precip_total_mm = 0.4
peak_tmax_c = 46.0
```

Substituting those values gives:

```text
I_2019-12 = 2*20 + 20*(29/31) + 2*3 + 3*2 + 1.5*(46.0 - 40) - 0.2*0.4
           = 79.6
```

The same formula gives `I_2020-01 = 49.9` and `I_2019-11 = 49.3`. The December margins are therefore:

```text
79.6 - 49.9 = 29.7
79.6 - 49.3 = 30.3
```

Both margins exceed 25.0 index units, so the required threshold diagnosis is `december_margin_confirmed`.

## Interpretation

The December ledger shows the clearest compound monthly signal: many heat-threshold days, almost no rain, a severe monthly heat peak, and some hot-windy overlap. January still has heat and wind support, but its wet relief and fewer heat-threshold days reduce the index. November is very dry and windier by day count, but its heat persistence is much weaker.

This is a local diagnostic reconstruction from the package weather series. It should not be treated as an official fire-danger product, burned-area estimate, mortality estimate, or loss estimate.

## Scoring Rubric

Total: 20 points.

- 4 points: Provides `answer = december_margin_confirmed` and `dominant_month = 2019-12`.
- 4 points: Correctly computes the December ledger: 20 heat-threshold days, dry fraction 0.935, 3 wind-threshold days, 2 hot-windy days, 0.4 mm precipitation, and 46.0 C peak temperature.
- 4 points: Correctly applies the formula and reports `diagnostic_index = 79.6` for 2019-12.
- 3 points: Correctly computes the January comparison, including `I_2020-01 = 49.9` and `margin_vs_january = 29.7`.
- 3 points: Correctly computes the November comparison, including `I_2019-11 = 49.3` and `margin_vs_november = 30.3`.
- 2 points: Keeps the explanation tied to the computed weather index, monthly margins, and stated comparison window.
