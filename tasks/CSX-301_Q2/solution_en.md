# Final Answer

The correct answer is `high_dust_mobility_low_wet_removal`.

A compact valid response is:

```json
{
  "answer": "high_dust_mobility_low_wet_removal",
  "index": 6.5,
  "peak_wind_kmh": 22.1,
  "wettest_mean_precip_mm": 2.4,
  "dry_windy_days": 2,
  "diagnosis": "The event-window data combine a dust-storm hazard label, a 22.1 km/h peak daily wind, low event precipitation, and two dry windy days, so wet removal is not the dominant interpretation."
}
```

## Key Computations

Hidden records used:

- `metadata/event.json`: confirms the event name and dust or sandstorm hazard family.
- `data/physical_hazard/physical_hazard_002_Open-Meteo_archive_point_sample.json`: provides daily 10 m wind, daily precipitation, and the dry windy day count.
- `data/physical_hazard/physical_hazard_001_NASA_POWER_daily_point_sample.json`: provides an independent daily point wind and precipitation check.
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`: provides event-window gridded precipitation context.
- `data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json`: provides event-window satellite precipitation context.
- `data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json`: provides another event-window precipitation context.
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`: checks that annual structural land-surface change is not the primary explanation.

Ignored or secondary files:

- Exposure files are not needed because this question is about the physical dust-mobility and wet-removal index, not exposed population or response priority.
- Event catalogs and broad report searches are not decisive because the computation depends on local meteorology and precipitation summaries.
- Preview images are useful context but are not needed for deterministic scoring.

## Text Claims/Package Claims

- The package metadata identifies the event as the March 2021 East Asia dust storm with hazard family `dust_sandstorm_extreme`.
- The daily point-sample weather contains a peak 10 m wind of 22.1 km/h.
- The local precipitation summaries are low over the event window; the largest candidate used for the denominator is 2.4 mm.
- Two daily point-sample days meet the dry windy condition: wind at least 18 km/h and precipitation at most 1 mm.
- The annual embedding-change mean is about 0.026, so this index should not be reinterpreted as a long-term land-cover damage measure.

`compute_gt.py` reads the local package files and calculates:

- peak wind as the maximum daily 10 m wind from Open-Meteo and NASA POWER after converting POWER wind from m/s to km/h;
- precipitation candidates from Open-Meteo point total, NASA POWER point total, ERA5-Land area mean, GPM IMERG area mean, and CHIRPS area mean;
- the wettest event mean or point-total precipitation as the largest precipitation candidate;
- dry windy days from the Open-Meteo daily series using wind at least 18 km/h and precipitation at most 1 mm;
- the index `peak_wind_kmh / (1 + wettest_event_mean_precip_mm)`;
- a deterministic interpretation label.

The script writes `computed_gt.json` in the task directory.

## Intermediate Values

```json
{
  "peak_wind_kmh": 22.1,
  "peak_wind_source": "Open-Meteo daily point sample",
  "wettest_mean_precip_mm": 2.4,
  "wettest_mean_source": "open_meteo_point_total_mm",
  "dry_windy_days": 2,
  "dry_windy_day_dates": ["2021-03-15", "2021-03-16"],
  "dust_mobility_wetness_index": 6.5,
  "mean_annual_embedding_change": 0.026,
  "mean_precip_candidates_mm": {
    "chirps_aoi_mean_mm": 0.785,
    "era5_land_aoi_mean_mm": 1.659,
    "gpm_imerg_aoi_mean_mm": 1.274,
    "open_meteo_point_total_mm": 2.4,
    "power_point_total_mm": 2.12
  }
}
```

## Reasoning Chain

1. The hazard family is a dust or sandstorm, so the physical diagnosis should emphasize dust transport and atmospheric loading unless the local metrics show strong wet removal.
2. The strongest daily 10 m wind is 22.1 km/h, which exceeds the 18 km/h dry windy day threshold used by this task.
3. The wettest precipitation candidate is only 2.4 mm, so the denominator remains small: `22.1 / (1 + 2.4) = 6.5`.
4. Two days meet the dry windy criterion, which supports continued dust mobility during the short event window.
5. The annual embedding-change mean is low, so the index is best interpreted as an acute dust-mobility and wet-removal signal rather than a structural land-cover change signal.
6. The resulting classification is `high_dust_mobility_low_wet_removal`.

## Reasoning Path

The core computation is deterministic: the strongest 10 m wind is 22.1 km/h and the wettest precipitation candidate is only 2.4 mm, so the index is `22.1 / (1 + 2.4) = 6.5`. That value exceeds the high-mobility threshold, and two days meet the dry-windy criterion. Because the event is a dust/sandstorm and annual embedding change is low, the index should be interpreted as acute dust mobility with limited wet removal, not hydrologic washout or structural land-cover damage.

## Unsupported Overclaims

- Do not claim measured PM concentration, exact visibility distance, airport closure counts, or hospital admissions from these files.
- Do not claim the 22.1 km/h point-sample wind is the maximum wind anywhere in the regional dust storm.
- Do not claim all precipitation products measure the same footprint or have the same spatial meaning.
- Do not treat the annual embedding-change statistic as direct aerosol optical depth or direct dust concentration.
- Do not infer a rainfall-driven disaster mechanism from these low precipitation values.

## Scoring Rubric

Total: 20 points.

- 3 points: Gives `high_dust_mobility_low_wet_removal` or an equivalent compact interpretation.
- 4 points: Computes the index near 6.5 using `22.1 / (1 + 2.4)`.
- 3 points: Reports the peak wind near 22.1 km/h and identifies it as the controlling wind term.
- 3 points: Reports the wettest precipitation candidate near 2.4 mm and explains why it implies limited wet removal.
- 2 points: Counts two dry windy days under the stated wind and precipitation thresholds.
- 2 points: Correctly ties the diagnosis to dust transport and low wet removal rather than hydrologic washout.
- 1 point: Notes that annual embedding change is not direct evidence of structural damage or dust concentration.
- 2 points: Avoids unsupported claims about PM concentration, confirmed direct impacts, or regional maximum winds.

## Disaster Interpretation

This task tests a compact physical consistency check for dust mobility. A moderate event-window wind signal paired with very low precipitation means that wet scavenging or rainfall washout is not the leading explanation for the short window. The two dry-windy days reinforce persistence of airborne dust risk. The index is not a direct air-quality concentration, visibility distance, or population-impact metric; it is a mechanism diagnostic that supports continued dust transport under limited wet removal.
