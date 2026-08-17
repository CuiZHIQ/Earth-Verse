# Nepal 2024 Flood-Landslide Anchor Diagnostic

A hydrometeorology review team is checking the September 27-29, 2024 Nepal floods and landslides. The question is whether the quantitative diagnosis should rest on a joined local rainfall, river-stage, and record-station-cluster signal, or whether gridded rainfall, public warning volume, or image change should be treated as the leading anchor.

Compute the threshold diagnostic using inclusive dates for the event window. For the station rainfall weighted mean, use the midpoint of each PDF precipitation bin multiplied by that bin's station count, including 550 mm as the representative midpoint for the open-ended `More than 500 mm` bin. Return only compact JSON with the fields shown below.

Use these pass rules:

- `station_rainfall_cluster`: pass when `station_max_to_weighted_mean_ratio >= 2.0`, `three_day_share_above_200mm >= 0.50`, and `three_day_station_count >= 150`.
- `river_historic_exceedance`: pass when `rivers_above_historic_count / rivers_checked >= 0.60` and `max_river_exceedance_m >= 2.0`.
- `record_station_cluster`: pass when `record_stations_in_approx_1000km2 >= 15`, `record_station_density_per_1000km2 >= 15`, and `approx_record_station_spacing_km <= 8.5`.
- `gridded_rainfall_primary`: pass when `GPM_max / station_max >= 0.50` and at least one gridded rainfall maximum reaches half the station maximum.
- `public_warning_volume_primary`: pass when `sms_alerts_per_1000_worldpop >= 1000`.
- `image_change_primary`: pass when `abs(mean_Sentinel1_VV_change_db) >= 3.0` and `AlphaEarth_change_max >= 0.8`.

Set `final_label` to `station_river_slope_joint_anchor` when the first three tests pass and the last three tests fail. Otherwise set it to `mixed_or_secondary_anchor`.

```json
{
  "score_ledger": {
    "<test_id>": {
      "pass": true,
      "supporting_values": {"<metric>": 0},
      "reason": "<one sentence tied to the threshold>"
    }
  },
  "final_label": "<derived label>",
  "failed_primary_candidates": [
    {
      "test_id": "<test_id>",
      "deciding_value": "<number or compact object>",
      "reason": "<one sentence tied to the threshold>"
    }
  ],
  "computed_interpretation": "<one sentence>"
}
```
