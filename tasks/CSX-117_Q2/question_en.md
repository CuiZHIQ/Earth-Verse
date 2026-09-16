# Hurricane Ian Landfall-Core Timing Ledger

A tropical-cyclone verification desk is checking whether Hurricane Ian's late-September 2022 record supports a tightly coupled landfall-core intensity and rainfall signature. Build a calculation-led ledger that uses the technical record to test wind-pressure timing, rainfall concentration, and the contrast between point rainfall and gridded precipitation maxima.

Return only a compact JSON object with exactly these top-level fields:

```json
{
  "target_family": "ian_landfall_core_timing_rainfall_concentration_ledger",
  "checks": [
    {
      "id": "catalog_window",
      "test": "",
      "values": {},
      "pass": true,
      "reason": ""
    }
  ],
  "final_classification": "",
  "score_summary": ""
}
```

Use exactly the five checks below, in this order. Each check must include the formula or logical test, the needed numeric or boolean values with unit-implied keys, a boolean pass/fail result, and a one-sentence reason.

1. `catalog_window`: test whether the catalog alert is Red, the affected countries include the United States and Cuba, and a local event-summary report text mentions Florida, the Carolinas, and Cuba.
2. `wind_pressure_lock`: test whether the peak gust and minimum pressure occur at the same hour and the pressure drop is greater than 40 hPa. Define pressure drop as the first hourly sea-level pressure value in the event-window point series minus the minimum sea-level pressure in that same series.
3. `rainfall_concentration`: test whether total point precipitation exceeds 200 mm, the wettest 24-hour share exceeds 0.65, and the peak-hour rainfall is within 6 hours of the pressure minimum.
4. `duration_balance`: test whether the wettest 72 hours contain more than 0.90 of total point precipitation while the wettest 6 hours contain less than 0.50 of the wettest 24-hour amount.
5. `gridded_peak_contrast`: compute the largest gridded precipitation maximum divided by the point wettest-24-hour amount, and test whether the fraction is below 0.50.

The final classification must be one concise sentence, and the score summary must state how many of the five checks pass.
