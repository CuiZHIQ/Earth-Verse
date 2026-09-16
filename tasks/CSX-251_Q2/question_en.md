# Haze-Dryness Score Ledger

Using the local CSX-251 package, compute a numeric ledger for the 2015 Indonesian drought, peat fires, and transboundary haze case. Work from structured fields where available; image metrics must use all RGB pixels.

Use the shared available daily interval covered by the local daily weather and precipitation products. In this package, that analysis interval is 2015-09-01 through 2015-10-16; treat it as the weather-analysis window rather than the full event window.

Definitions:
- Brightness per pixel = `(R + G + B) / 3`. For the pre-event and event images, compute mean brightness and the share of pixels whose RGB channel range is `<25` and brightness is `>120`.
- Dry day = Open-Meteo `precipitation_sum < 1.0` mm. Compute day count, dry-day count, dry share, longest consecutive dry-day run, and total point precipitation.
- Precipitation gap = GPM event mean minus CHIRPS event mean; also compute the GPM/CHIRPS ratio.
- Burn gate = `1` when Sentinel-2 dNBR `pre_count` and `post_count` are both `0`; otherwise `0`.
- AOI area = `(delta_lon * 111.320 * cos(mean_latitude)) * (delta_lat * 110.574)` square kilometers from the compact AOI polygon. Compute population density and OSM element density.
- Final index = `100 * (0.45 * min(1, brightness_delta / 15) + 0.25 * min(1, low_bright_delta_pp / 5) + 0.20 * dry_share + 0.10 * burn_gate)`.

Return JSON with `final_index`, `image`, `dryness`, `precipitation`, `burn_gate`, and `receptor_density`. Round the final index to 1 decimal, brightness to 2 decimals, shares to 4 decimals, percentage-point and precipitation values to 1 decimal, area to 2 decimals, and densities to 3 significant digits.

## Reasoning-depth requirement

Add a top-level `reasoning_depth` object to the returned JSON with exactly these string fields:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "<which evidence is decisive versus contextual>",
    "counterfactual_rejection": "<which tempting simpler explanation fails and why>",
    "uncertainty_or_scale_caveat": "<what the evidence should not be over-interpreted to prove>"
  }
}
```

For this task, use that object to make the haze-dryness score explain the difference between image dryness, rainfall support, burn-gate logic, and receptor density.

