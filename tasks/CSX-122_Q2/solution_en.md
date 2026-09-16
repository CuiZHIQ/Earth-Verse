# Final Answer

```json
{
  "answer": {
    "duration_alignment": {
      "wmo_days": 36.0,
      "gdacs_days": 33.75,
      "ratio": 1.067,
      "gap_days": 2.25,
      "lag_h": 34.0
    },
    "rainfall_concentration": {
      "event_mm": 393.6,
      "wet_days": 36,
      "wetday_mean_mm": 10.9,
      "late_mm": 136.6,
      "late_share": 0.347,
      "late_day_mean_mm": 34.1,
      "late_amp": 3.12
    },
    "peak_window_check": {
      "max72h_mm": 112.4,
      "max72h_share": 0.286,
      "max168h_mm": 146.7,
      "max168h_share": 0.373
    },
    "gridded_contrast": {
      "gpm_max_mean": 3.38,
      "chirps_max_mean": 2.72,
      "chirps_gpm_mean": 1.05
    }
  },
  "classification": "late concentrated pulse on a long wet baseline",
  "not_pattern": "not uniform accumulation or a one-day-only spike"
}
```

# Key Computations

The WMO duration is 36.0 days and the GDACS tropical-cyclone duration is 33.75 days, so `ratio = 36.0 / 33.75 = 1.067` and `gap_days = 36.0 - 33.75 = 2.25`. The Malawi flood starts 34.0 hours after the GDACS tropical-cyclone end.

Open-Meteo gives 393.6 mm across 36 wet days, so the event wet-day mean is `393.6 / 36 = 10.9` mm. The Malawi late window contributes 136.6 mm, so `late_share = 136.6 / 393.6 = 0.347`. Across the four-day late window from 2023-03-12 through 2023-03-15, the unrounded daily mean rounds to `34.1 mm`, and `late_amp` rounds to `3.12`.

The wettest 72-hour total is 112.4 mm, giving `112.4 / 393.6 = 0.286`. The wettest 168-hour total is 146.7 mm, giving `146.7 / 393.6 = 0.373`. The gridded accumulated-rainfall contrasts are `389.4 / 115.28 = 3.38` for GPM, `328.85 / 120.94 = 2.72` for CHIRPS, and `120.94 / 115.28 = 1.05` for the CHIRPS/GPM mean ratio.

# Reasoning Path

The duration row first establishes that the 36-day WMO duration and the 33.75-day GDACS duration are close enough to describe the same long event window, while the 34.0-hour flood lag keeps the Malawi timing tied to the late portion of the cyclone record.

The rainfall row then separates persistence from concentration. A 36-wet-day event mean of 10.9 mm per wet day shows a long wet baseline, but the late window averages 27.3 mm per day and holds 34.7% of the event precipitation. That is a clear late concentration, not an even spread across the full window.

The peak-window row prevents the answer from collapsing into a single-day interpretation. The wettest 72 hours contain 28.6% of the event total, and the wettest 168 hours contain 37.3%, so the late pulse is multi-day.

The gridded contrast row checks that gridded maxima are much larger than their means in both GPM and CHIRPS, while the CHIRPS and GPM means are close. This is consistent with a concentrated rainfall pattern rather than a flat accumulation field.

# Computed Interpretation

The compact interpretation is a long wet Freddy baseline with a late multi-day rainfall pulse over Malawi. The computed ledger rejects both a uniform accumulation label and a one-day-only spike label.

# Scoring Rubric

- 3 points: Final classification correctly states a late concentrated pulse on a long wet baseline. Partial credit: 1-2 points for naming only the long duration or only the late concentration.
- 3 points: Duration row reports 36.0 days, 33.75 days, ratio 1.067, gap 2.25 days, and 34.0 hours. Partial credit: 1-2 points for correct values with one missing formula result or one timing error.
- 5 points: Rainfall concentration row reports 393.6 mm, 36 wet days, 10.9 mm wet-day mean, 136.6 mm late-window precipitation, 0.347 share, 34.1 mm late-window daily mean, and 3.12 amplification using the 2023-03-12 to 2023-03-15 late window. Partial credit: 2-4 points for correct totals but incomplete share, mean, or amplification arithmetic.
- 3 points: Peak-window row reports 112.4 mm, 0.286, 146.7 mm, and 0.373, and treats the concentration as multi-day. Partial credit: 1-2 points for correct precipitation totals but missing shares or the multi-day inference.
- 3 points: Gridded contrast row reports GPM maximum/mean ratio 3.38, CHIRPS maximum/mean ratio 2.72, and CHIRPS/GPM mean ratio 1.05. Partial credit: 1-2 points for using only one gridded ratio or reversing one mean-ratio calculation.
- 2 points: The answer rejects the uniform or one-day-only pattern without adding claims beyond the computed ledger. Partial credit: 1 point for rejecting only one of those two patterns.
- 1 point: Output is concise JSON with the required four row names plus `classification` and `not_pattern`. Partial credit: no partial credit for prose-only answers.
