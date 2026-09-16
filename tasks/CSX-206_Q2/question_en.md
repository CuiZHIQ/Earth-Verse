# Southern Africa Smoke Transport Ledger

During the August-September 2000 biomass-burning smoke and aerosol episode over southern Africa, compute a numeric pattern, source, transport, and precipitation ledger for the smoke label.

Use the pre-event and event true-color satellite scenes, the event text, the fire-catalog returns, the wind aggregates, and the precipitation summaries. Return only the calculation ledger, with no health-impact language or action guidance.

Definitions:

- Satellite smoke load: in the 1024 x 768 true-color scenes, use the fixed ROI with zero-indexed rows 450-729 and columns 300-819. A valid pixel has `mean_rgb > 10` and is not all channels `< 8`. A haze pixel is valid with `60 <= mean_rgb <= 210` and saturation `(max_rgb - min_rgb) / max(max_rgb, 1) <= 0.20`. Compute the pre-event haze fraction, event haze fraction, event/pre ratio, and whether `ratio >= 1.25` and delta is at least 20 percentage points.
- Source/fire count: count the named heavy-burning zones in the event source passage; count the local EONET wildfire events returned for the event; compute `catalog_gap_ratio = eonet_wildfire_events / reported_heavy_burning_zones`.
- Wind transport: from the mean 10 m ERA5 wind components, compute speed and the transport bearing from north as `degrees(atan2(u_mean, v_mean)) mod 360`. The transport test passes when `u_mean > 0`, `v_mean > 0`, and the bearing is 67.5-112.5 degrees.
- Precipitation clearing: from the daily point precipitation support period, count days with precipitation `>= 10 mm`, compute the wet-day fraction, and mark rain clearing as dominant only if that fraction is at least 0.50 or the longest consecutive `>= 10 mm` run is at least 5 days. Also compute the event-mean precipitation ratio `GPM_mean / CHIRPS_mean`; the cross-product test passes when the ratio is 0.90-1.10.
- Consistency score: count the five passes: smoke load, source count, wind transport, rain clearing not dominant, and GPM/CHIRPS ratio.

Return compact JSON:

```json
{
  "satellite_smoke_load": {
    "pre_pct": 0,
    "event_pct": 0,
    "ratio": 0,
    "threshold_pass": false
  },
  "source_fire_count": {
    "reported_heavy_burning_zones": 0,
    "eonet_wildfire_events": 0,
    "catalog_gap_ratio": 0,
    "threshold_pass": false
  },
  "wind_transport": {
    "u_mean_mps": 0,
    "v_mean_mps": 0,
    "bearing_deg": 0,
    "threshold_pass": false
  },
  "precip_clearing": {
    "wet_days": 0,
    "support_days": 0,
    "wet_fraction": 0,
    "gpm_chirps_mean_ratio": 0,
    "rain_clearing_dominant": false
  },
  "consistency_score": 0,
  "diagnosis": ""
}
```
