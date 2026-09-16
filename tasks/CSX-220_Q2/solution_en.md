# Final Answer

```json
{
  "ledger_rows": [
    {
      "test": "wet_context_consistency",
      "formula": "min(local_event_mm, gridded_event_mm, independent_event_mm) > 0 and min/max >= 0.50",
      "value": {
        "local_event_mm": 8.9,
        "gridded_event_mm": 7.56,
        "independent_event_mm": 6.65,
        "min_max_ratio": 0.747
      },
      "threshold": "all sources > 0 mm and min/max >= 0.50",
      "result": "PASS"
    },
    {
      "test": "event_day_rainfall_dominance",
      "formula": "local_event_mm / local_15d_mm >= 0.50 and event day is the local 15-day precipitation maximum",
      "value": {
        "local_event_mm": 8.9,
        "local_15d_mm": 100.2,
        "event_day_share_15d": 0.089,
        "max_precip_mm": 31.6,
        "max_precip_date": "2020-12-27"
      },
      "threshold": "event-day share >= 0.50 and max date is 2020-12-30",
      "result": "FAIL"
    },
    {
      "test": "near_freezing_state",
      "formula": "-1 <= gridded_tmax_mean_c <= 3 and local_tmin_c <= 0 <= local_tmax_c",
      "value": {
        "gridded_tmax_mean_c": 0.91,
        "local_tmin_c": -0.2,
        "local_tmax_c": 1.6
      },
      "threshold": "near-freezing gridded mean and local daily range crossing 0 C",
      "result": "PASS"
    },
    {
      "test": "reported_extent_geometry",
      "formula": "flow_ha = 300 * 700 / 10000; total_affected_ha = flow_ha + 9.0",
      "value": {
        "flow_ha": 21.0,
        "reported_debris_ha": 9.0,
        "total_affected_ha": 30.0
      },
      "threshold": "flow_ha >= 20 and total_affected_ha >= 30",
      "result": "PASS"
    },
    {
      "test": "short_window_surface_dominance",
      "formula": "abs(short_window_SAR_VV_mean) / abs(optical_dNBR_mean) and abs(short_window_SAR_VV_mean) / annual_embedding_change",
      "value": {
        "s1_to_s2_ratio": 1.845,
        "s1_to_annual_ratio": 6.996
      },
      "threshold": "S1/S2 >= 1.5 and S1/annual >= 5",
      "result": "PASS"
    },
    {
      "test": "local_exposure_context",
      "formula": "compact elements >= 10 and amenity features >= 1 and highway features >= 1",
      "value": {
        "compact_exposure_elements": 100,
        "amenity_features": 50,
        "highway_features": 50
      },
      "threshold": "compact exposure has enough mapped receptor features",
      "result": "PASS"
    }
  ],
  "computed_label": "sensitive_ground_wet_context_short_window_disturbance",
  "rejected_alternative": "Event-day rainfall dominance fails because the event day contributes only 0.089 of local 15-day precipitation and the local maximum was 31.6 mm on 2020-12-27."
}
```

# Key Computations

| test | formula and values | result |
|---|---|---|
| `wet_context_consistency` | Local event precipitation = 8.9 mm, gridded mean = 7.56 mm, independent gridded mean = 6.65 mm. `min/max = 6.65 / 8.9 = 0.747`, with all sources above 0 mm. | PASS |
| `event_day_rainfall_dominance` | Local 15-day precipitation = 100.2 mm and 5-day precipitation = 72.2 mm. Event-day share is `8.9 / 100.2 = 0.089`; the 15-day maximum is 31.6 mm on 2020-12-27, not 2020-12-30. | FAIL |
| `near_freezing_state` | Gridded event-day Tmax mean = 0.91 C; local event-day range is -0.2 C to 1.6 C, so the day crosses 0 C and stays in the stated near-freezing band. | PASS |
| `reported_extent_geometry` | `flow_ha = 300 * 700 / 10000 = 21.0 ha`; `total_affected_ha = 21.0 + 9.0 = 30.0 ha`; debris-to-flow ratio = 0.429. | PASS |
| `short_window_surface_dominance` | `abs(S1 VV mean) = 0.6378`, `abs(S2 dNBR mean) = 0.3457`, annual embedding change = 0.0912. Ratios: `S1/S2 = 1.845`, `S1/annual = 6.996`. | PASS |
| `local_exposure_context` | Compact exposure has 100 elements, including 50 amenity features and 50 highway features. Broad population sum is 1,059,042.03, or 10,590.42 people per compact feature if naively divided. | PASS |

Rejected alternative: event-day rainfall dominance fails because the event day accounts for only 0.089 of the local 15-day precipitation and was not the wettest day in that window.

# Reasoning Path

The wet-context row passes because all three event-day precipitation sources are above zero and the smallest-to-largest source ratio is `0.747`, above the `0.50` threshold.

The event-day rainfall-dominance row fails both checks. The event day contributes only `0.089` of the 15-day local precipitation, below `0.50`, and the local 15-day maximum is 2020-12-27 rather than 2020-12-30.

The near-freezing row passes because the gridded event-day mean maximum temperature is `0.91 C`, inside `[-1, 3]`, and the local daily range crosses zero from `-0.2 C` to `1.6 C`.

The reported-extent, short-window surface, and local-exposure rows also pass: `21.0 ha` flow area and `30.0 ha` total affected area meet the geometry thresholds; the SAR ratios are `1.845` and `6.996`, both above their thresholds; and compact exposure counts exceed all count thresholds.

With those five required rows passing and event-day rainfall dominance failing, the deterministic label rule returns `sensitive_ground_wet_context_short_window_disturbance`.

# Computed Interpretation

The result is a threshold-ledger diagnosis: wet context, near-freezing state, reported geometry, short-window surface change, and compact local exposure are all numerically consistent, while the event day is not rainfall-dominant within the local 15-day window.

# Scoring Rubric

Total: 20 points.

- Requested ledger structure, 3 points: returns a compact ledger with all six required tests, formulas or formula references, numeric values, pass/fail states, and the final computed label; partial credit for most required fields with one missing test, formula, or pass/fail state.
- Rainfall and temperature calculations, 4 points: correctly computes 100.2 mm 15-day precipitation, 72.2 mm 5-day precipitation, 0.089 event-day share, 0.747 cross-source wetness ratio, 0.91 C gridded Tmax mean, and -0.2 C to 1.6 C local event-day range; partial credit for mostly correct precipitation or temperature values with minor rounding or one missing source.
- Extent, surface-change, and exposure calculations, 5 points: correctly computes 21.0 ha flow area, 30.0 ha total affected area, 1.845 S1/S2 ratio, 6.996 S1/annual ratio, and compact exposure counts of 100 total, 50 amenity, and 50 highway features; partial credit for correct values in two of the three groups or for small rounding differences.
- Threshold decisions, 4 points: applies the thresholds so wet context, near-freezing state, reported extent, short-window surface dominance, and local exposure pass while event-day rainfall dominance fails; partial credit if final states are mostly right but one threshold is inverted or omitted.
- Rejected alternative, 2 points: rejects event-day rainfall dominance using both the 0.089 event-day share and the 2020-12-27 precipitation maximum; partial credit for using only one of the two numeric reasons.
- Concise label interpretation, 1 point: states the label only as the consequence of the numeric ledger, not as a broad landslide narrative; partial credit if the label is correct but the interpretation is verbose.
- Overclaim control, 1 point: keeps broad population context separate from observed local losses and does not state that rainfall is proven as the dominant trigger; partial credit if only one of the two scope limits is handled correctly.
