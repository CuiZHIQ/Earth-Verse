# CSX-245 Fault-Coupled Severity Ledger

Using only structured values in the local CSX-245 package, compute a numeric ledger for the 1 January 2024 Noto Peninsula earthquake. Use the USGS finite-fault and ShakeMap properties, Sentinel-1 VV pre/post statistics, annual satellite-embedding cosine-change statistics, event-day precipitation maxima, WorldPop count, and the tsunami flag.

Compute these derived values:

- `area_km2 = model_length_km * model_width_km`
- `length_width_ratio = model_length_km / model_width_km`
- `radar_range_db = s1_vv_post_minus_pre_db_max - s1_vv_post_minus_pre_db_min`
- `max_precip_mm = max(ERA5-Land max, GPM max, CHIRPS max)`

Then score the ledger:

- `fault = 2*rake_band + 1*dip_band + 2*near_surface + 2*long_length + 2*large_area + 1*elongated`, where the flags are true for rake 45-135 deg, dip 20-50 deg, model top < 1 km, length >= 150 km, area >= 7500 km2, and length/width >= 3.5.
- `shaking = 2*mmi_high + 2*pga_high + 2*pgv_high`, where the flags are true for MMI >= 8.5, PGA >= 1.5 g, and PGV >= 100 cm/s.
- `radar = 1*mean_shift + 1*wide_range + 1*post_count_ok`, where the flags are true for abs(mean VV change) >= 2 dB, VV range >= 40 dB, and post count >= 2.
- `context = 1` when max precipitation < 10 mm, annual embedding mean change < 0.05, and the tsunami flag equals 1; otherwise `0`.

Set `class_label` to `full_threshold_rupture_scale_surface_change` when `total_score == 20`; otherwise set it to `partial_threshold_surface_change`.

Return compact JSON with this structure:

```json
{
  "area_km2": 0,
  "length_width_ratio": 0,
  "radar_range_db": 0,
  "max_precip_mm": 0,
  "component_scores": {
    "fault": 0,
    "shaking": 0,
    "radar": 0,
    "context": 0
  },
  "total_score": 0,
  "class_label": "",
  "numeric_anchors": {
    "magnitude_mww": 0,
    "maximum_mmi": 0,
    "max_pga_g": 0,
    "max_pgv_cm_s": 0,
    "finite_fault_rake_deg": 0,
    "model_top_km": 0,
    "radar_mean_change_db": 0,
    "annual_embedding_mean_change": 0,
    "population_millions": 0,
    "tsunami_flag": 0
  }
}
```
