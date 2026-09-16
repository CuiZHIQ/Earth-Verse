# Taan Fiord Threshold-Window Ledger

A data audit is checking whether the CSX-227 Taan Fiord package satisfies a compact threshold/window ledger using report anchors, Sentinel-1 pre/post sample counts and VV change, WorldPop population, and OSM mapped building features.

Compute these quantities:

- `mass_million_tons`: the report value in "sent ... million tons".
- `max_runup_m`: the report value in "as high as ... m".
- `mass_per_runup_m = mass_million_tons / max_runup_m`.
- `s1_pre_count`: the Sentinel-1 pre-event sample count.
- `s1_post_count`: the Sentinel-1 post-event sample count.
- `s1_window_min_count = min(s1_pre_count, s1_post_count)`.
- `s1_abs_peak_db = max(abs(vv_post_minus_pre_max_db), abs(vv_post_minus_pre_min_db))`.
- `mapped_population`: the WorldPop population sum.
- `osm_buildings`: the count of OSM elements with a `building` tag.

Apply these gates:

- `mass_gate`: `mass_million_tons >= 150`
- `runup_gate`: `max_runup_m >= 150`
- `s1_window_gate`: `s1_pre_count >= 5` and `s1_post_count >= 5`
- `sar_change_gate`: `s1_abs_peak_db >= 45`
- `exposure_contrast_gate`: `mapped_population < 1` and `osm_buildings >= 10`

Also compute these margins:

- `mass_margin = mass_million_tons - 150`
- `runup_margin = max_runup_m - 150`
- `s1_window_min_margin = s1_window_min_count - 5`
- `sar_change_margin_db = s1_abs_peak_db - 45`
- `population_headroom = 1 - mapped_population`
- `building_margin = osm_buildings - 10`

Use `taan_fiord_numeric_gate_pass` when all five gates pass; otherwise use `taan_fiord_numeric_gate_fail`.

Return compact JSON:

```json
{
  "target_family": "taan_fiord_mass_runup_sar_exposure_gate_ledger",
  "metrics": {
    "mass_million_tons": 0.0,
    "max_runup_m": 0.0,
    "mass_per_runup_m": 0.0,
    "s1_pre_count": 0,
    "s1_post_count": 0,
    "s1_window_min_count": 0,
    "s1_abs_peak_db": 0.0,
    "mapped_population": 0.0,
    "osm_buildings": 0
  },
  "gates": {
    "mass_gate": false,
    "runup_gate": false,
    "s1_window_gate": false,
    "sar_change_gate": false,
    "exposure_contrast_gate": false
  },
  "margins": {
    "mass_margin": 0.0,
    "runup_margin": 0.0,
    "s1_window_min_margin": 0,
    "sar_change_margin_db": 0.0,
    "population_headroom": 0.0,
    "building_margin": 0
  },
  "answer": "<label>",
  "ledger_status": "<short status>"
}
```
