# Hurricane Ophelia Wind-Rain Phase Ledger

During 9-16 October 2017, Hurricane Ophelia affected Ireland and the UK after transitioning toward a windstorm. A meteorology review needs a calculation-only ledger for a local point near Dublin: decide whether the local signature is best classified as wind-pressure severity with offset rainfall, rather than rainfall-led, surge-led, image-led, or population-led.

Return a compact JSON object with exactly these top-level keys:

```json
{
  "task_family": "ophelia_wind_pressure_rain_phase_ledger",
  "diagnosis_label": "<concise label>",
  "ledger": [
    {
      "row_id": "wind_pressure_alignment",
      "formula_or_test": "<formula, inequality, or timing test>",
      "computed_values": {},
      "result": "<pass/reject/context>",
      "reason": "<one sentence>"
    }
  ],
  "final_conclusion": "<one sentence>",
  "rejected_alternatives": ["<short label>", "<short label>"]
}
```

The `ledger` must contain exactly these five rows:

1. `wind_pressure_alignment`: compute peak gust, peak sustained wind, minimum pressure, 6 h/12 h/24 h pressure falls, peak-gust to pressure-minimum lag, and the gust-to-sustained-wind ratio. Mark the row as passing only if the pressure minimum lags the peak gust by no more than 1 hour and the 24 h pressure fall is at least 20 hPa.
2. `gust_persistence`: compute the event-window hour count and the counts and shares for gust hours at or above 70, 90, and 100 km/h. Mark the row as passing only if the at-or-above-70 km/h gust count is at least 10 hours and the at-or-above-100 km/h count is at least 3 hours.
3. `local_rain_offset`: compute event precipitation, 16 October precipitation, the 16 October rainfall share, wettest-hour timing, and wettest-24 h timing. Use these values to reject a rainfall-led local classification when 16 October has less than 25% of event precipitation and the wettest hour is not on the peak-gust date.
4. `daily_wind_rain_split`: compare the daily peak wind date with the daily peak precipitation date and mark whether the wind and precipitation peaks are date-separated.
5. `supporting_context_check`: summarize mapped population and package-declared area precipitation context. Treat these as supporting checks only, not as physical wind-severity proof.

Keep the proof numeric and ledger-based. Narrative impact explanation, damage inference from imagery, population-density severity claims, surge-first claims, or rainfall-led local conclusions will not satisfy the task.
