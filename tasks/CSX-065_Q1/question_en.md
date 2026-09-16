# Southeast Asia Monsoon Flood Rainfall-Exposure Diagnostic

A hydrology review team is checking whether the 2011 Southeast Asia monsoon floods should be summarized as a sustained rainfall-exposure signal rather than a short rain pulse. The local package anchors the event to the Chao Phraya and Mekong floodplain systems from late July into mid-December 2011.

Compute a compact diagnostic from the technical record. Use inclusive date arithmetic for the full event window and for the precipitation summary window, combine the three accumulated-rainfall summaries into one consensus rainfall signal, compute the population-weighted exposure load, and treat the paired-image scene counts as a separate confirmation test. The exposure load is `consensus_mean_mm * population_millions`, where `population_millions` is the WorldPop population-sum value divided by 1,000,000.

Use these tests:

- `duration_persistence`: pass if the full event window is at least 120 days.
- `rain_window`: pass if the precipitation summary window is at least 30 days and no more than half of the full event window.
- `mean_rain`: pass if the three-product mean accumulated rainfall is at least 300 mm.
- `peak_rain`: pass if the highest product maximum accumulated rainfall is at least 600 mm.
- `cross_product_agreement`: pass if the lowest product mean divided by the highest product mean is at least 0.85.
- `image_pair`: pass only if both pre-event and post-event image counts are at least 1.

Score the diagnostic as the number of passing tests out of 6. Return valid JSON with exactly these top-level fields:

```json
{
  "answer": "<compact label>",
  "metrics": {
    "event_days": <integer>,
    "precip_days": <integer>,
    "coverage_pct": <number>,
    "consensus_mean_mm": <number>,
    "daily_mean_mm": <number>,
    "mean_agreement_ratio": <number>,
    "max_peak_mm": <number>,
    "population_millions": <number>,
    "exposure_mm_million": <number>,
    "image_counts": [<integer>, <integer>]
  },
  "tests": {
    "duration_persistence": "pass|fail",
    "rain_window": "pass|fail",
    "mean_rain": "pass|fail",
    "peak_rain": "pass|fail",
    "cross_product_agreement": "pass|fail",
    "image_pair": "pass|fail"
  },
  "score": <integer>,
  "computed_interpretation": "<one sentence tied to the computed diagnostic>"
}
```

Use the label `persistent_monsoon_rainfall_exposure_signal_no_image_pair` when the first five tests pass and the paired-image test fails. Keep the interpretation to the computed threshold result; do not add loss totals, road-closure counts, or intervention notes.
