# Final Answer

```json
{
  "target_family": "pakistan_2022_monsoon_indus_persistence_gate",
  "metrics": {
    "peak_to_mean_intensity": 10.972,
    "heavy_rain_persistence": 0.2844,
    "red_window_fraction": 0.7248,
    "grid_mean_spread_fraction": 0.0661,
    "peak_window_share": 0.3244
  },
  "gates": {
    "intensity_gate": true,
    "persistence_gate": true,
    "regional_consensus_gate": true,
    "pulse_guardrail": true
  },
  "final_label": "sustained_indus_storage_signal",
  "computed_consequence": "persistent_loading_outweighs_short_peak"
}
```

# Key Computations

The locked window is 109 days. NASA POWER precipitation totals 1493.3 mm, with a 150.3 mm daily peak and 31 days at or above 10 mm/day. The peak-to-mean ratio is high, but the heavy-rain fraction, 79-day GDACS red flood fraction, three-product grid spread, and 7-day share all satisfy the persistence gate.

# Reasoning Path

The event mean daily precipitation is `1493.3 / 109 = 13.7 mm/day`, so the point peak-to-mean intensity is `150.3 / 13.7 = 10.972`, which passes the `>= 8.0` intensity gate. Heavy-rain persistence is `31 / 109 = 0.2844`, and the red flood-window fraction is `79 / 109 = 0.7248`; together they pass the persistence gate.

The three gridded comparison-window mean precipitation values, over their declared 2022-06-14 to 2022-07-29 window, are 846.6 mm, 792.5 mm, and 815.4 mm. Their mean is 818.1 mm, so the spread fraction is `(846.6 - 792.5) / 818.1 = 0.0661`, below the 0.10 regional-consensus threshold. The maximum 7-day point total is 484.48 mm, so the 7-day share is `484.48 / 1493.3 = 0.3244`, below the 0.40 pulse guardrail. All four gates are true, so the deterministic label is `sustained_indus_storage_signal`.

# Computed Interpretation

The calculated ledger indicates that the event was not explained by a single short rainfall pulse: persistent heavy-rain days, long red flood duration, cross-product precipitation agreement, and a limited 7-day share all point to sustained basin loading.

# Scoring Rubric

- 3 points: Returns the requested compact JSON fields: `target_family`, `metrics`, `gates`, `final_label`, and `computed_consequence`. Partial credit: 1-2 points if the answer is mostly complete but omits one required field or includes a field in an unusable shape.
- 4 points: Computes the event-window and rainfall anchors: 109 days, 1493.3 mm point total, 150.3 mm daily peak, and 31 days at or above 10 mm/day. Partial credit: 1-3 points for a correct window with one or two incorrect rainfall anchors, or correct rainfall anchors with a minor window error.
- 3 points: Computes `peak_to_mean_intensity = 10.972` within tolerance from the daily peak divided by the event-window daily mean. Partial credit: 1-2 points for the right formula with rounding or denominator errors that still preserve the gate outcome.
- 4 points: Computes `heavy_rain_persistence = 0.2844` and `red_window_fraction = 0.7248` within tolerance. Partial credit: 1-3 points if only one fraction is correct or both use the correct counts but the wrong denominator or rounding.
- 3 points: Computes `grid_mean_spread_fraction = 0.0661` over the declared 2022-06-14 to 2022-07-29 gridded comparison window and `peak_window_share = 0.3244` over the point series. Partial credit: 1-2 points if one metric is correct or the formulas are correct but the values are slightly outside tolerance.
- 2 points: Applies all four thresholds correctly and returns `sustained_indus_storage_signal`. Partial credit: 1 point if the gate booleans are mostly correct but the final label or one threshold comparison is wrong.
- 1 point: Keeps the consequence short and directly derived from the gate results. Partial credit: 0.5 points if the consequence is directionally correct but adds minor extra detail.
