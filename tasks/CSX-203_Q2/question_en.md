# Severe Haze Consistency Proof

A technical review team is checking whether the January 6-16, 2013 northern and eastern China haze episode is numerically consistent with persistent cold-season aerosol haze rather than precipitation-cleared obscuration, heat stress, or a package-supported active-burn smoke control signal.

Compute the following diagnostics from the local event-package values:

- `haze_term_count`: count how many of `haze`, `smog`, and `air quality` appear in the event narrative.
- `dry_fraction`: event-window dry days divided by event-window days.
- `mean_vector_wind_mps`: `sqrt(u10_mean^2 + v10_mean^2)` from the regional 10 m mean wind components.
- `regional_precip_mean_mm`: average of the two regional event-accumulated precipitation means.
- `diffuse_veil_index`: `(event_mean_brightness - pre_event_mean_brightness) - abs(event_mean_chroma - pre_event_mean_chroma)`.
- `burn_evidence_count`: available wildfire-event count plus available pre-scene and post-scene burn-severity scene counts.

Apply these thresholds: `haze_term_count >= 2`, `dry_fraction >= 0.80`, `mean_vector_wind_mps < 1.0`, `regional_precip_mean_mm <= 2.0`, `diffuse_veil_index >= 20.0`, and `burn_evidence_count == 0` as a bounded package-evidence check. Set `consistency_score` to the number of passed tests out of six. Use `persistent_winter_aerosol_haze` as the final label only when all six tests pass; otherwise use `not_proven_by_thresholds`.

Return compact JSON:

```json
{
  "metrics": {
    "haze_term_count": 0,
    "dry_fraction": 0.0,
    "mean_vector_wind_mps": 0.0,
    "regional_precip_mean_mm": 0.0,
    "diffuse_veil_index": 0.0,
    "burn_evidence_count": 0
  },
  "tests": {
    "haze_text": "<pass|fail>",
    "dry_window": "<pass|fail>",
    "weak_wind": "<pass|fail>",
    "low_precipitation": "<pass|fail>",
    "diffuse_brightening": "<pass|fail>",
    "no_package_burn_evidence": "<pass|fail>"
  },
  "consistency_score": "<passed>/6",
  "final_label": "<compact_label>",
  "rejected_alternative": "<one short computed rejection>"
}
```
