# Storm-Surface Consistency Ledger

Use the CSX-285 event package for the 6-18 September 2024 Typhoon Yagi and southwest monsoon case. Build a numeric ledger that measures whether event-period rainfall and image darkening dominate over the annual durable-change signal.

Compute these package-derived values:

- GPM event accumulated precipitation mean and maximum, in mm.
- CHIRPS event accumulated precipitation mean and maximum, in mm.
- Pre-event and event image mean brightness after resizing each RGB image to 256 x 192 pixels with bilinear resampling, with brightness defined as `(R+G+B)/3`.
- Pre-event and event dark-pixel fraction after the same bilinear resize, where a dark pixel has brightness `<60`.
- `brightness_delta` in the returned anchors is `pre_brightness - event_brightness`, so positive values mean event-window darkening.
- Annual Google Satellite Embedding `1-cosine` mean.

Then apply this capped component ledger:

```text
gpm_c = min(gpm_mean_mm / 150, 1)
chirps_c = min(chirps_mean_mm / 120, 1)
brightness_c = min((pre_brightness - event_brightness) / 12, 1)
dark_c = min((event_dark_fraction - pre_dark_fraction) / 0.07, 1)
annual_c = 1 - min(annual_change_mean / 0.05, 1)
storm_surface_score = 0.30*gpm_c + 0.30*chirps_c + 0.20*brightness_c + 0.10*dark_c + 0.10*annual_c
```

Round anchors to the precision implied by the package summaries and image method, round components and `storm_surface_score` to three decimals, and set `classification` to `storm_window_transient_signal_dominant` when `storm_surface_score >= 0.75` and `annual_change_mean < 0.05`; otherwise use `durable_change_or_low_consistency`.

Return JSON:

```json
{
  "anchors": {
    "gpm_mean_mm": 0,
    "gpm_max_mm": 0,
    "chirps_mean_mm": 0,
    "chirps_max_mm": 0,
    "brightness_delta": 0,
    "dark_fraction_delta": 0,
    "annual_change_mean": 0
  },
  "components": {
    "gpm_c": 0,
    "chirps_c": 0,
    "brightness_c": 0,
    "dark_c": 0,
    "annual_c": 0
  },
  "storm_surface_score": 0,
  "classification": ""
}
```
