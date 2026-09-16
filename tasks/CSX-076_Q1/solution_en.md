# Final Answer

```json
{
  "target_family": "pakistan_monsoon_flood_load_numeric_diagnosis",
  "gridded_means_mm": {
    "gpm": 792.492,
    "chirps": 815.383,
    "era5_land": 846.553
  },
  "gridded_comparison_window": {
    "start_date": "2022-06-14",
    "end_date": "2022-07-29"
  },
  "ensemble_mean_mm": 818.143,
  "point_rainfall": {
    "event_days": 110,
    "total_mm": 1493.3,
    "peak_day_mm": 150.31,
    "peak_day_share": 0.1007,
    "wet_day_fraction": 0.3818,
    "heavy_day_fraction": 0.2818,
    "longest_heavy_spell_days": 13,
    "max_14day_share": 0.4438
  },
  "threshold_state": "all_gridded_means_gt_700mm_and_peak_day_lt_15pct",
  "final_label": "persistent_monsoon_flood_load_consistent"
}
```

# Key Computations

- Event window from the event anchor: 2022-06-14 to 2022-10-01, giving 110 daily point-rainfall entries.
- The three gridded accumulated-rainfall summaries share a declared package comparison window from 2022-06-14 to 2022-07-29; they are not treated as full June-October gridded totals.
- Gridded comparison-window accumulated-rainfall means: GPM = 792.492 mm, CHIRPS = 815.383 mm, ERA5-Land = 846.553 mm.
- Ensemble mean formula: `(792.492 + 815.383 + 846.553) / 3 = 818.143 mm`.
- All three gridded means exceed the 700 mm accumulated-load check.
- Point total over the 110-day window: 1493.3 mm.
- Peak day: 150.31 mm on 2022-08-18.
- Peak-day share formula: `150.31 / 1493.3 = 0.1007`.
- Wet-day fraction formula: `42 / 110 = 0.3818` for days with at least 1 mm.
- Heavy-day fraction formula: `31 / 110 = 0.2818` for days with at least 10 mm.
- Longest heavy spell: 13 days, from 2022-08-13 through 2022-08-25.
- Maximum 14-day total: 662.76 mm from 2022-08-13 through 2022-08-26, with share `662.76 / 1493.3 = 0.4438`.

# Reasoning Path

The gridded products agree on a broad accumulated rainfall load over their declared comparison window: each mean is above 700 mm, and their ensemble mean is 818.143 mm. The full daily point series then supplies the June-October persistence test. Although the peak day is intense, it accounts for only 10.07 percent of the event total, below the 15 percent single-day dominance control used here.

The persistence metrics reinforce that result. There are 42 wet days, 31 heavy days, and a 13-day heavy-rain spell. The strongest 14-day window accounts for 44.38 percent of the point total, so the largest burst is important but still embedded in a longer monsoon-load sequence.

# Computed Interpretation

The computed label is `persistent_monsoon_flood_load_consistent`: severity is numerically tied to sustained monsoon accumulation and multi-day concentration, not to one isolated daily pulse or to report wording alone.

# Scoring Rubric

- 3 points: Final structured answer. Full credit for the requested JSON fields, target family, threshold state, and final label. Partial credit for a mostly complete JSON answer with one missing field group.
- 4 points: Gridded rainfall calculations. Full credit for the declared 2022-06-14 to 2022-07-29 gridded comparison window, the three gridded means, the 818.143 mm ensemble mean, and the all-above-700 mm threshold result. Partial credit for correct means with missing or rounded ensemble arithmetic.
- 4 points: Point total and peak-day concentration. Full credit for 110 days, 1493.3 mm total, 150.31 mm peak day, and 0.1007 peak-day share. Partial credit for the total and peak value without the ratio test.
- 3 points: Persistence metrics. Full credit for 42/110 wet-day fraction, 31/110 heavy-day fraction, and the 13-day heavy spell. Partial credit for two of the three persistence anchors.
- 2 points: Rolling-window calculation. Full credit for the 662.76 mm maximum 14-day total and 0.4438 share. Partial credit for the correct window total without the share.
- 2 points: Threshold reasoning. Full credit for combining the gridded load check, peak-day share below 15 percent, and heavy-day persistence into one threshold state. Partial credit for applying only one threshold correctly.
- 1 point: Rejection of weak alternatives. Full credit for explicitly rejecting a single-day-only or report-only explanation using the computed values. Partial credit for rejecting one alternative without a numeric reason.
- 1 point: Concise computed interpretation. Full credit for a short event-specific interpretation that does not add new loss estimates. Partial credit for a correct label with overly broad prose.
