# Final Answer

The correct answer is `station_river_slope_joint_anchor`.

```json
{
  "score_ledger": {
    "station_rainfall_cluster": {
      "pass": true,
      "supporting_values": {
        "station_max_to_weighted_mean_ratio": 2.333,
        "three_day_share_above_200mm": 0.574,
        "three_day_station_count": 183
      },
      "reason": "All three station-rainfall thresholds are met."
    },
    "river_historic_exceedance": {
      "pass": true,
      "supporting_values": {
        "river_historic_exceedance_share": 0.714,
        "max_river_exceedance_m": 3.52
      },
      "reason": "Five of seven checked rivers exceeded historic levels, and the largest exceedance is above 2 m."
    },
    "record_station_cluster": {
      "pass": true,
      "supporting_values": {
        "record_stations_in_approx_1000km2": 16,
        "record_station_density_per_1000km2": 16.0,
        "approx_record_station_spacing_km": 7.906
      },
      "reason": "The record-station cluster clears the count, density, and spacing thresholds."
    },
    "gridded_rainfall_primary": {
      "pass": false,
      "supporting_values": {
        "gpm_max_share_of_station_max": 0.142,
        "chirps_max_share_of_station_max": 0.122,
        "era5_max_share_of_station_max": 0.094
      },
      "reason": "The gridded maxima are all below one half of the station maximum."
    },
    "public_warning_volume_primary": {
      "pass": false,
      "supporting_values": {
        "sms_alerts_per_1000_worldpop": 816.7
      },
      "reason": "The normalized warning count is below the 1000 per 1000 people threshold."
    },
    "image_change_primary": {
      "pass": false,
      "supporting_values": {
        "sentinel1_vv_change_mean_db": 0.546,
        "alphaearth_change_max": 0.599
      },
      "reason": "Neither the mean radar-change threshold nor the embedding-change threshold is met."
    }
  },
  "final_label": "station_river_slope_joint_anchor",
  "failed_primary_candidates": [
    {
      "test_id": "gridded_rainfall_primary",
      "deciding_value": {"gpm": 0.142, "chirps": 0.122, "era5_land": 0.094},
      "reason": "All gridded maxima are below one half of the station maximum."
    },
    {
      "test_id": "public_warning_volume_primary",
      "deciding_value": 816.7,
      "reason": "Warning volume per 1000 people is below the stated threshold."
    },
    {
      "test_id": "image_change_primary",
      "deciding_value": {"sentinel1_vv_change_mean_db": 0.546, "alphaearth_change_max": 0.599},
      "reason": "The radar and embedding changes both miss the primary-signal thresholds."
    }
  ],
  "computed_interpretation": "The event is best anchored by concentrated station rainfall, historic river exceedance, and a dense cluster of record rainfall stations rather than by gridded rainfall, warning volume, or image-change maxima."
}
```

# Key Computations

The event window from 2024-09-27 through 2024-09-29 is 3 inclusive days.

Station rainfall distribution:

- Weighted mean three-day station rainfall from the binned station distribution, using bin midpoints and 550 mm for the open-ended `More than 500 mm` bin: `221.585 mm`.
- Maximum three-day station rainfall: `517.0 mm`.
- Maximum-to-weighted-mean ratio: `517.0 / 221.585 = 2.333`.
- Station count: `183`.
- Share above 200 mm: `105 / 183 = 0.574`.
- Share above 300 mm: `37 / 183 = 0.202`.
- Share above 400 mm: `6 / 183 = 0.033`.

River and record-station cluster:

- Historic river exceedance share: `5 / 7 = 0.714`.
- Maximum river exceedance: `3.52 m`.
- Record stations in the approximately 1000 km2 cluster: `16`.
- Record-station density: `16 / 1000 * 1000 = 16.0 per 1000 km2`.
- Approximate record-station spacing: `sqrt(1000 / 16) = 7.906 km`.

Secondary signal checks:

- Gridded-to-station maximum ratios: GPM `73.33 / 517.0 = 0.142`, CHIRPS `63.067 / 517.0 = 0.122`, ERA5-Land `48.637 / 517.0 = 0.094`.
- Warning normalization: `4,093,795 / 5,013,000 * 1000 = 816.7` SMS messages per 1000 people.
- Image-change metrics: Sentinel-1 VV mean post-minus-pre change `0.546 dB`, Sentinel-1 VV range `34.4 dB`, AlphaEarth mean `0.025`, AlphaEarth maximum `0.599`.

# Reasoning Path

The station-rainfall test passes because the max-to-weighted-mean ratio is above `2.0`, the share of stations above 200 mm is above `0.50`, and the station count is above `150`. This shows a strong local rainfall concentration rather than a single isolated value.

The river test passes because `0.714` of checked rivers exceeded historic levels and the largest exceedance is `3.52 m`, which is above the `2.0 m` threshold. The record-station cluster also passes: `16` record stations in about `1000 km2` gives density `16.0`, and the spacing proxy of `7.906 km` is below `8.5 km`.

The three alternative primary signals fail their threshold tests. GPM, CHIRPS, and ERA5-Land maxima are only `0.142`, `0.122`, and `0.094` of the station maximum, so no gridded maximum reaches one half of the station maximum. The SMS warning normalization is `816.7`, below `1000`. The image-change test fails because `abs(0.546) < 3.0` and `0.599 < 0.8`.

Since the first three tests pass and the last three fail, the deterministic label is `station_river_slope_joint_anchor`.

# Computed Interpretation

The numbers point to a joined local rainfall, river-stage, and record-station-cluster diagnosis. The gridded rainfall, warning-volume, and image-change signals are useful supporting context, but their threshold values are too weak to become the leading quantitative anchor for this event.

# Scoring Rubric

- 4 points: Final label and diagnostic structure. Full credit for returning `score_ledger`, `final_label`, `failed_primary_candidates`, and `computed_interpretation`, with `final_label` equal to `station_river_slope_joint_anchor`. Partial credit: award 1 point for each required field that is present and usable; withhold the final-label point if the label is wrong.
- 4 points: Station rainfall calculations. Full credit for `517.0 mm`, `221.585 mm`, ratio `2.333`, station count `183`, and shares `0.574`, `0.202`, and `0.033`. Partial credit: award up to 4 points in proportion to the correctly computed station values within tolerance.
- 3 points: River exceedance calculations. Full credit for `5 / 7 = 0.714` and maximum exceedance `3.52 m`. Partial credit: award 1.5 points for the correct exceedance share and 1.5 points for the correct maximum exceedance.
- 3 points: Record-station cluster calculations. Full credit for count `16`, density `16.0 per 1000 km2`, and spacing `7.906 km`. Partial credit: award 1 point for each correct cluster value within tolerance.
- 3 points: Secondary signal calculations. Full credit for gridded ratios `0.142`, `0.122`, and `0.094`, warning normalization `816.7`, Sentinel-1 mean `0.546 dB`, and AlphaEarth max `0.599`. Partial credit: award up to 3 points for correctly computing most of these values within tolerance.
- 2 points: Threshold logic. Full credit for marking the station, river, and record-station tests as passing and the gridded, warning-volume, and image-change tests as failing. Partial credit: award 1 point for the correct three passing tests and 1 point for the correct three failing tests.
- 1 point: Concise computed interpretation. Full credit for a one-sentence interpretation tied to the computed diagnostic and no extra claims beyond the calculated event diagnosis. Partial credit: award 0.5 points if the interpretation is directionally correct but too broad.
