# Wildfire-Smoke Consistency Proof

During the 2024 South America wildfire-smoke episode, a technical review team needs a calculation-first consistency check for the working diagnosis: regional wildfire-smoke load with localized burn scars and incomplete precipitation clearing.

Build a row-wise numeric ledger that tests this diagnosis against local package data. Use explicit formulas and compute these checks. Where the catalog, weather, or precipitation products provide only the 2024-08-01 to 2024-09-15 daily slice, keep that slice denominator and do not infer daily records for 2024-09-16 to 2024-09-21.

1. Event-window persistence: inclusive days from 2024-08-01 through 2024-09-21.
2. Smoke/PM proxy load: reported 2024 PM2.5 days above 35 ug/m3 divided by the event-window days; treat this as a reported 2024 burden proxy, not as a direct event-day PM monitor series.
3. Burn-event density: wildfire event records naming Brazil, Bolivia, or Paraguay during the 2024-08-01 to 2024-09-15 daily catalog slice, divided by 46 days; also compute the fraction of those 46 days with at least one such record.
4. Fire-weather support: over the daily weather slice 2024-08-01 to 2024-09-15, compute heat load `sum(max(Tmax_C - 35, 0))`, longest run with precipitation <= 0.1 mm/day, and count of days with maximum 10 m wind >= 20 km/h.
5. Precipitation-clearing test: CHIRPS mean accumulated precipitation divided by 46 days, plus the daily dry-day fraction from the same weather slice.
6. Satellite localization: dNBR peak-to-mean ratio, annual embedding-change peak-to-mean ratio, and whether broad conversion is ruled out by both low means.

Return compact JSON with:

```json
{
  "event_window_days": 0,
  "ledger": [
    {"test": "", "formula": "", "value": 0, "threshold_result": "", "implication": ""}
  ],
  "final_classification": "",
  "rejected_alternative": ""
}
```

Use numeric values with units in field names or row text, round derived ratios to two decimals where appropriate, and keep the final classification to one sentence.
