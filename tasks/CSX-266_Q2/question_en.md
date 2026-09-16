# Black Summer Monthly Fire-Weather Ledger

For the Australian Black Summer compound heat, drought, fire, and smoke event, use the local CSX-266 daily weather evidence to rebuild a calendar-month diagnostic for 2019-09-01 through 2020-02-29.

For each calendar month, compute:

- `heat_days_ge_40c`: days with daily maximum temperature at least 40.0 C.
- `dry_fraction`: days with zero daily precipitation divided by days in the month.
- `wind_days_ge_35kmh`: days with daily maximum 10 m wind speed at least 35.0 km/h.
- `hot_windy_days`: days satisfying both the heat and wind thresholds.
- `precip_total_mm`: monthly precipitation total.
- `peak_tmax_c`: monthly maximum daily temperature.

Use this diagnostic formula:

```text
I = 2*heat_days_ge_40c
    + 20*dry_fraction
    + 2*wind_days_ge_35kmh
    + 3*hot_windy_days
    + 1.5*max(0, peak_tmax_c - 40)
    - 0.2*min(precip_total_mm, 50)
```

Use the unrounded dry-day fraction inside `I`, but report `dry_fraction` rounded to three decimals. Round `precip_total_mm`, `peak_tmax_c`, `I`, and margin values to one decimal.

Set `answer` to `december_margin_confirmed` only if 2019-12 is the month whose diagnostic index exceeds both 2020-01 and 2019-11 by at least 25.0 index units; otherwise set it to `not_confirmed`.

Return only JSON in this shape:

```json
{
  "answer": "<december_margin_confirmed or not_confirmed>",
  "dominant_month": "YYYY-MM",
  "ledger": {
    "heat_days_ge_40c": 0,
    "dry_fraction": 0.0,
    "wind_days_ge_35kmh": 0,
    "hot_windy_days": 0,
    "precip_total_mm": 0.0,
    "peak_tmax_c": 0.0
  },
  "diagnostic_index": 0.0,
  "margin_vs_january": 0.0,
  "margin_vs_november": 0.0
}
```
