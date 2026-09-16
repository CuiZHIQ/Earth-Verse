# Final Answer

```json
{
  "satellite_smoke_load": {
    "pre_pct": 64.82,
    "event_pct": 87.91,
    "ratio": 1.356,
    "threshold_pass": true
  },
  "source_fire_count": {
    "reported_heavy_burning_zones": 4,
    "eonet_wildfire_events": 0,
    "catalog_gap_ratio": 0.0,
    "threshold_pass": true
  },
  "wind_transport": {
    "u_mean_mps": 0.728,
    "v_mean_mps": 0.093,
    "bearing_deg": 82.7,
    "threshold_pass": true
  },
  "precip_clearing": {
    "wet_days": 7,
    "support_days": 46,
    "wet_fraction": 0.152,
    "gpm_chirps_mean_ratio": 1.026,
    "rain_clearing_dominant": false
  },
  "consistency_score": 5,
  "diagnosis": "transport_persistent_biomass_burning_smoke"
}
```

# Key Computations

Satellite smoke load uses the fixed lower-middle image window and the stated valid/haze masks. The pre-event scene has 78,340 haze pixels out of 120,861 valid pixels, so `pre_pct = 64.82`. The event scene has 123,406 haze pixels out of 140,385 valid pixels, so `event_pct = 87.91`. The ratio is `87.9054 / 64.8183 = 1.356`, with a delta of 23.09 percentage points, passing the smoke-load threshold.

The source/fire ledger counts four named heavy-burning zones: western Zambia, southern Angola, northern Namibia, and northern Botswana. The two local EONET wildfire returns contain zero wildfire events, so `catalog_gap_ratio = 0 / 4 = 0.0`; this is a catalog-gap result, while the source-zone count still passes.

The ERA5 mean wind vector is `u = 0.727944 m/s`, `v = 0.093224 m/s`. Speed is `sqrt(u^2 + v^2) = 0.734 m/s`, and the transport bearing is `atan2(u, v) = 82.7 degrees`, which passes the east-northeast transport test.

Daily point precipitation support covers 2000-08-14 through 2000-09-28, or 46 days. There are 7 days with at least 10 mm precipitation, giving `7 / 46 = 0.152`; the longest such wet run is 2 days, so rain clearing is not dominant. The gridded event-mean precipitation ratio is `326.385 / 318.026 = 1.026`, passing the 0.90-1.10 product-consistency test.

# Reasoning Path

The ledger applies five independent threshold checks. First, the event scene has both a large haze-fraction ratio and a 20-plus percentage-point increase over the pre-event scene. Second, the report-derived source-zone count is high even though the local catalog count is zero, so the catalog value is treated as a gap in that catalog return rather than as a zero-source result. Third, the mean wind has positive eastward and northward components and a bearing inside the east-northeast sector. Fourth, only 7 of 46 support days reach 10 mm and the longest wet run is 2 days, so the rain-clearing flag remains false. Fifth, the GPM/CHIRPS mean ratio stays close to 1.

# Computed Interpretation

All five checks pass: smoke-load ratio, source-zone count, wind transport, rain clearing not dominant, and precipitation product consistency. The resulting `consistency_score` is 5, and the compact label is `transport_persistent_biomass_burning_smoke`. The answer should remain a numeric ledger rather than a broader impact narrative.

# Scoring Rubric

- 3 points: Returns the requested six-field JSON structure with nested numeric values, booleans, and diagnosis string. Partial credit: 1-2 points for a mostly correct structure with missing or mistyped fields.
- 5 points: Correctly computes the satellite smoke-load mask, pre/event haze fractions, ratio near 1.356, and threshold pass. Partial credit: 2-4 points for correct masking but one rounded value or threshold detail wrong.
- 3 points: Correctly reports four heavy-burning zones, zero local EONET wildfire events, and `catalog_gap_ratio = 0.0` without treating the catalog zero as absence of burning. Partial credit: 1-2 points for correct counts but incomplete ratio or catalog-gap handling.
- 3 points: Correctly computes the ERA5 wind vector, including positive `u` and `v`, bearing near 82.7 degrees, and transport pass. Partial credit: 1-2 points for correct components but an incomplete bearing or sector test.
- 3 points: Correctly computes precipitation clearing values: 7 wet days, 46 support days, wet fraction near 0.152, non-dominant rain clearing, and GPM/CHIRPS ratio near 1.026. Partial credit: 1-2 points for correct wet-day arithmetic but one product-ratio or run-length detail wrong.
- 2 points: Correctly combines the five threshold tests into `consistency_score = 5` and the stated diagnosis. Partial credit: 1 point for the right score or label but not both.
- 1 point: Keeps the answer limited to the numeric ledger and avoids added health-impact or action-guidance narrative. Partial credit: no partial credit for this one-point criterion.

Total: 20 points.
