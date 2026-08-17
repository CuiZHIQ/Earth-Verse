# Oso Landslide Numeric Diagnosis Ledger

A geotechnical analysis team is checking the March 22, 2014 Oso landslide near Steelhead Haven. Compute a compact numeric ledger that tests whether the incident record supports an antecedent-wet, high-mobility, river-blockage label. Use the quantitative incident record for the input values, then apply the formulas and thresholds below.

Return JSON with exactly these six top-level fields:

```json
{
  "rainfall_load": {
    "antecedent_15d_mm": 0.0,
    "event_day_gridded_max_mm": 0.0,
    "antecedent_to_event_day_ratio": 0.0
  },
  "landslide_extent": {
    "avg_speed_mph": 0.0,
    "overrun_area_sqmi": 0.0,
    "moved_mass_mtons": 0.0,
    "mass_density_mtons_per_sqmi": 0.0
  },
  "river_extent": {
    "dam_depth_ft": 0.0,
    "temporary_lake_mi": 0.0,
    "blockage_ft_mi": 0.0
  },
  "context_index_per_100k": 0.0,
  "threshold_score": {
    "passed": 0,
    "possible": 8
  },
  "computed_label": ""
}
```

Use these derived quantities:

- `antecedent_to_event_day_ratio = antecedent_15d_mm / event_day_gridded_max_mm`
- `mass_density_mtons_per_sqmi = moved_mass_mtons / overrun_area_sqmi`
- `blockage_ft_mi = dam_depth_ft * temporary_lake_mi`
- `context_index_per_100k = (OSM way count + OSM amenity count) / population * 100000`

The eight threshold checks are: antecedent rainfall at least 150 mm, antecedent/event-day ratio at least 10, average speed at least 30 mph, overrun area at least 0.25 square mile, moved mass at least 10 million tons, dam depth at least 20 ft, temporary lake length at least 2 miles, and a direct-impact index of 3 from fatalities at least 25, covered structures at least 25, and covered road length at least 0.5 mile. If at least 7 of 8 checks pass and the rainfall ratio check passes, set `computed_label` to `antecedent_wet_high_mobility_river_blockage`; otherwise use `limited_landslide_river_signal` for 5-6 passes or `insufficient_numeric_proof` for fewer than 5 passes.
