# Final Answer

Correct Answer: `66.1` on the 0-100 index.

```json
{
  "final_index": 66.1,
  "image": {
    "pre_mean_brightness": 90.19,
    "event_mean_brightness": 100.86,
    "brightness_delta": 10.67,
    "pre_low_bright_share": 0.3094,
    "event_low_bright_share": 0.3444,
    "low_bright_delta_pp": 3.5
  },
  "dryness": {
    "analysis_window": "2015-09-01 to 2015-10-16",
    "day_count": 46,
    "dry_day_count": 15,
    "dry_share": 0.3261,
    "longest_dry_run": 3,
    "point_precip_mm": 197.6
  },
  "precipitation": {
    "gpm_mean_mm": 275.3,
    "chirps_mean_mm": 234.4,
    "gap_mm": 40.9,
    "ratio": 1.174
  },
  "burn_gate": 1,
  "receptor_density": {
    "area_km2": 2478.94,
    "population": 2750.7,
    "population_density_km2": 1.11,
    "osm_elements": 183,
    "osm_density_km2": 0.0738
  }
}
```

# Calculation

Image metrics give mean brightness `90.19 -> 100.86`, so `brightness_delta = 10.67`. The low-bright share is `30.94% -> 34.44%`, so `low_bright_delta_pp = 3.51`.

For the shared weather-analysis window, 2015-09-01 through 2015-10-16, Open-Meteo has `46` daily records, `15` days below `1.0` mm, dry share `0.3261`, longest dry run `3`, and point precipitation `197.6` mm. GPM and CHIRPS event means are `275.3` and `234.4` mm, giving gap `40.9` mm and ratio `1.174`. The dNBR counts are `pre_count = 0` and `post_count = 0`, so `burn_gate = 1`. The compact AOI area is `2478.94` square kilometers, with population density `1.11` per square kilometer and OSM density `0.0738` elements per square kilometer.

`100 * (0.45 * min(1, 10.67/15) + 0.25 * min(1, 3.51/5) + 0.20 * 0.3261 + 0.10 * 1) = 66.1`.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "Image brightness and low-bright share changes drive the visual dryness component, Open-Meteo dryness supports persistence, and GPM/CHIRPS plus receptor density provide context.",
    "counterfactual_rejection": "A burn-scar-confirmation reading fails because the dNBR pre/post counts are zero and the burn gate is only a scoring condition, not mapped burn severity.",
    "uncertainty_or_scale_caveat": "Masked AOI, OSM, and population products are authoritative for derived density statistics but not for judging absolute place metadata."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

- 4 points: Computes the all-pixel image brightness and low-bright share deltas with correct rounding.
- 4 points: Computes the daily precipitation ledger over the shared weather-analysis window, including dry count, dry share, longest run, and total point precipitation.
- 3 points: Computes the GPM-CHIRPS mean gap and ratio.
- 3 points: Applies the dNBR count gate exactly from the structured counts.
- 3 points: Computes AOI area plus population and OSM densities from masked authoritative product statistics.
- 3 points: Applies the final formula and reports the rounded index in the requested JSON schema.
