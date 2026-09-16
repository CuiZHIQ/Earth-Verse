# Smoke Persistence Numeric Proof

For the late-August 2004 Angola fire-and-smoke episode, compute a compact proof that the observed haze persistence is better represented by a source-plus-transport persistence state than by source intensity alone, broad precipitation clearing, or simple point ventilation.

Return a JSON object with exactly these keys:

```json
{
  "answer": "short_label",
  "window_days": 0,
  "source_smoke": {
    "fire_hits": 0,
    "source_flags": 0,
    "transport_flags": 0,
    "transport_source_ratio": 0.0,
    "smoke_family_hits": 0,
    "aod_pm_hits": 0
  },
  "clearing": {
    "local_precip_mm": 0.0,
    "low_precip_days_le2mm": 0,
    "regional_mean_mm": 0.0,
    "regional_max_mean_ratio": 0.0,
    "era5_wind_ms": 0.0,
    "local_wind_kmh": 0.0,
    "pass_count": 0
  },
  "satellite": {
    "mean_abs_rgb_delta": 0.0,
    "normalized_rgb_delta": 0.0,
    "smoke_delta_pct_points": 0.0
  },
  "persistence_score": 0
}
```

Use these calculation rules:

- `window_days` is the inclusive event-window duration.
- `source_flags` counts the presence of seasonal burning, charcoal production, and satellite-detected fires. `transport_flags` counts high-pressure persistence, counterclockwise recirculation, and downwind Atlantic haze. `transport_source_ratio = transport_flags / source_flags`.
- `fire_hits` is the count of exact `fire` or `fires` terms in the article title plus event-body narrative only. `smoke_family_hits` counts exact `smoke`, `smog`, and `haze` terms in the same article-title-plus-body text. `aod_pm_hits` counts exact AOD, PM2.5, PM10, aerosol, and particulate terms.
- `clearing.pass_count` is the number of threshold tests that pass: local event-day precipitation below 2 mm, local maximum wind below 10 km/h, mean 10 m vector wind below 1 m/s, and no broad precipitation-clearing signal where regional mean precipitation is below 10 mm while the largest regional precipitation max/mean ratio is above 5.
- For `satellite`, compare the pre-event and event true-color images. `mean_abs_rgb_delta` is the mean absolute per-channel RGB difference, `normalized_rgb_delta = mean_abs_rgb_delta / 255`, and `smoke_delta_pct_points` is the event-minus-pre-event percentage-point change in smoke-like pixels. A smoke-like pixel has HSV value above 0.45, HSV saturation below 0.35, `abs(R-G) < 35`, and `abs(G-B) < 35`.
- `persistence_score = source_flags + transport_flags + clearing.pass_count + satellite_change_pass`, where `satellite_change_pass` is 1 when `normalized_rgb_delta >= 0.05`.

Set `answer` to `source_plus_transport_smoke_persistence` only if `persistence_score >= 9`, `smoke_family_hits >= 4`, and `transport_source_ratio >= 1`; otherwise set it to `source_or_clearing_only_fails_threshold`.
