# Oman Landfall Phase Severity Proof

A technical review team is checking whether Cyclone Gonu's initial Oman coastal phase is best calibrated from a co-timed landfall rain, gust, and pressure window rather than from one peak signal or a displaced map layer.

Compute a compact proof ledger for the 168-hour event window and return JSON in this shape:

```json
{
  "answer": "<compact severity label>",
  "rows": [
    {
      "row_id": "<row label>",
      "calculation": "<formula or comparison used>",
      "value": "<numeric result with units or boolean>",
      "decision": "<pass/fail or calibration implication>"
    }
  ],
  "final_consistency": "<one sentence>"
}
```

Required row labels:

1. `landfall_peak_day_concentration`
2. `wind_pressure_timing_window`
3. `independent_daily_same_day_support`
4. `regional_precip_max_context`
5. `map_layer_nonreplacement_check`

The proof must include rainfall concentration fractions, the co-timing span for gust, wind, and pressure extrema, same-day support from an independent daily point series, point-to-regional precipitation ratios, and a map/image nonreplacement check showing that derived map, exposure, and image summaries are context rather than replacements for the Oman point-window calibration.
