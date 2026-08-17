# Final Answer

Correct answer: `regional_biomass_burning_smoke_with_low_ventilation_context`.

Expected compact JSON:

```json
{
  "metrics": {
    "source_region_count": 4,
    "scene_haze_ratio": 1.066,
    "mean_wind_m_s": 0.693,
    "low_wind_day_fraction": 1.0,
    "precip_total_mm": 208.49,
    "dry_day_fraction": 0.0
  },
  "pass_fail": {
    "source_count": "pass",
    "scene_haze_change": "pass",
    "low_ventilation": "pass",
    "local_dryness": "fail"
  },
  "final_consistency": "regional_biomass_burning_smoke_with_low_ventilation_context",
  "rejected_alternative": "local dry-weather or heat-led proof fails the dryness threshold"
}
```

# Key Computations

The event-window daily weather series contains 46 available days, from 2000-08-14 through 2000-09-28. The fire and smoke report text names four heaviest-burning source regions: western Zambia, southern Angola, northern Namibia, and northern Botswana. Therefore `source_region_count = 4`, which passes the `>= 3` rule.

For the true-color scene pair, black scan gaps are ignored before counting haze-candidate pixels. A haze-candidate pixel has `70 <= luma <= 220` and `saturation <= 0.20`, with `luma = 0.2126R + 0.7152G + 0.0722B` and `saturation = (max(R,G,B) - min(R,G,B)) / max(R,G,B)`. The pre-scene haze fraction is `0.5895`; the event-scene haze fraction is `0.6283`; therefore `scene_haze_ratio = 0.6283 / 0.5895 = 1.066`.

The 10 m wind mean is `0.693 m/s`. All 46 available wind values are at or below `1.0 m/s`, so `low_wind_day_fraction = 46 / 46 = 1.0`. Daily precipitation totals sum to `208.49 mm`, and `0 / 46` days are at or below `0.5 mm`, so `dry_day_fraction = 0.0`. The heat-side check is small: the `Tmax > 30 C` load is `2.27 C-days`.

# Reasoning Path

The source-region test passes because `4 >= 3`. The image-change test passes because `1.066 >= 1.05`. The low-ventilation test passes because `0.693 <= 1.0` and `1.0 >= 0.80`.

The local-dryness test fails: even though the requested dry-day fraction is directly computed, the precipitation total is far above the `<= 50 mm` cutoff and the dry-day fraction is below the `>= 0.50` cutoff. This failed local-weather test does not block the final label, because the final consistency rule requires the source-count, scene-haze-change, and low-ventilation tests to pass.

# Computed Interpretation

The threshold ledger supports a regional biomass-burning smoke/aerosol label with low local ventilation context. A local dry-weather or heat-led proof is rejected by the precipitation and heat checks, especially `208.49 mm` total precipitation, `0.0` dry-day fraction, and only `2.27 C-days` above 30 C.

# Scoring Rubric

Total: 20 points.

- Requested JSON structure (4 points): Returns the metrics object, pass/fail object, final consistency label, and short rejected alternative. Partial credit: 2-3 points for parseable JSON with one missing object or minor field-name mismatch; 1 point for mostly correct content outside strict JSON.
- Numeric anchors and formulas (5 points): Computes source-region count, haze ratio, mean wind, low-wind fraction, precipitation total, and dry-day fraction with correct units and formulas. Partial credit: up to 1 point for source count, 1.5 for image haze ratio, 1.5 for wind values, and 1 for precipitation values when formulas are mostly correct.
- Threshold decisions (4 points): Correctly marks source count, scene haze change, and low ventilation as pass, and local dryness as fail. Partial credit: 1 point for each correct pass/fail state; no credit for a state whose threshold direction is reversed.
- Calculation reasoning (3 points): Shows the image haze calculation and daily weather aggregation as explicit numeric checks. Partial credit: 1.5 points for the image calculation path and 1.5 points for the weather aggregation path if one path is incomplete.
- Rejected alternative (2 points): Rejects a local dry-weather or heat-led proof using the failed dryness test and small heat load. Partial credit: 1 point for rejecting either local dryness or heat-led proof with a correct numeric reason.
- Concise consistency label (1 point): Uses a short final label that follows from the pass/fail tests. Partial credit: 0.5 point for an equivalent but wordier label that preserves the three passing tests.
- No uncomputed escalation (1 point): Avoids adding measured health-impact, road-closure, or burn-scar severity assertions not computed by the ledger. Partial credit: 0.5 point for one minor extra assertion that does not change the final label.
