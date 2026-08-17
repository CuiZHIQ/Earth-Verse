# Smoke-Plume Threshold Ledger

For the September-October 2015 Singapore haze, reconstruct a compact assessment ledger that checks whether the event record passes a CO-rich smoke-plume exposure label while not assigning a burn-scar map label.

Select package-relative evidence for the event window, hazard family, atmospheric signal, exposed-population context, burn-change context, precipitation context, and paired visual context.

Compute:

- `window` = locked start/end as `YYYY-MM-DD/YYYY-MM-DD`.
- `window_days` = inclusive day count.
- `co_ratio` = peak surface CO ppb / ordinary CO ppb, rounded to one decimal.
- `co_excess_ppb` = peak surface CO ppb - ordinary CO ppb.
- `exposed_population` = WorldPop population sum rounded to the nearest whole person.
- `sentinel_scene_total` = Sentinel-2 dNBR `pre_count + post_count`.
- `precip_products_present` = count of the available GPM IMERG and CHIRPS event-accumulation JSON summaries that exist and contain a `stats` object; treat this as an availability check for the package precipitation summaries, not as a full-window rainfall-clearing calculation.
- `final_label` = `co_plume_exposure_supported_no_burnscar_map` only if `hazard_family == "air_pollution_smoke_heat"`, `co_ratio >= 10.0`, `exposed_population > 0`, `sentinel_scene_total == 0` with dNBR status `no_sufficient_scenes`, both true-color image files are valid openable images with positive dimensions and nonzero pixel variation, and `precip_products_present == 2`; otherwise use `ledger_incomplete_for_co_plume_exposure`.

Return only compact JSON with these fields:

```json
{
  "window": "YYYY-MM-DD/YYYY-MM-DD",
  "window_days": 0,
  "co_ratio": 0.0,
  "co_excess_ppb": 0,
  "exposed_population": 0,
  "sentinel_scene_total": 0,
  "precip_products_present": 0,
  "final_label": "<label>"
}
```
