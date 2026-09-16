# Correct Answer

The expected compact answer is:

```json
{
  "answer": "persistent_heat_load_dominant_with_hydrologic_low_water_support",
  "target_family": "heat_drought_mechanism_dominance_ranking",
  "computed_values": {
    "tmax35_run_days": 17,
    "tmin28_run_days": 11,
    "app40_run_days": 16,
    "vpd_aug7_23_pm_mean_kpa": 2.77,
    "vpd_max_kpa": 3.54,
    "poyang_drop_m": 3.03,
    "early_dry_days": 100,
    "rain_gap_days": 45
  },
  "mechanism_scores": {
    "persistent_heat_load": 96,
    "hydrologic_low_water_timing": 90,
    "evaporative_demand": 82,
    "precipitation_deficit_only": 42,
    "reported_loss_or_exposure_only": 8
  },
  "ranked_mechanisms": [
    "persistent_heat_load",
    "hydrologic_low_water_timing",
    "evaporative_demand",
    "precipitation_deficit_only",
    "reported_loss_or_exposure_only"
  ],
  "dominant_mechanism": "persistent_heat_load",
  "rejected_mechanism": "reported_loss_or_exposure_only",
  "reasoning_path": "Heat persistence is strongest: 17d Tmax>=35C, 11d Tmin>=28C, 16d apparent>=40C. VPD amplifies demand during Aug7-23, while Poyang drops 3.03m and dry season arrives about 100d early. Rain grids end 45d before Aug30 low-water, and reported losses are consequences, not mechanisms."
}
```

One acceptable sentence after the JSON is: the ranking treats rainfall and reported losses as contextual evidence, while the dominant explanation is persistent heat load with hydrologic low-water corroboration.

# Key Computations

Heat persistence from the daily weather series:

- Longest run of daily maximum temperature at or above 35C: 17 days, from 2022-08-07 through 2022-08-23.
- Longest run of daily minimum temperature at or above 28C: 11 days, from 2022-08-12 through 2022-08-22.
- Longest run of daily maximum apparent temperature at or above 40C: 16 days, from 2022-08-08 through 2022-08-23.
- Total hot days: 20 with Tmax >= 35C, and heat-degree load above 35C is 21.8 C-days.
- Peak daily and hourly apparent temperature: 44.0C.

Evaporative-demand calculation from hourly temperature and relative humidity:

- Vapor pressure deficit is computed as `0.6108 * exp(17.27 * T / (T + 237.3)) * (1 - RH / 100)`.
- Across the 2022-08-07 to 2022-08-23 heat run, mean VPD is 1.846 kPa and the 90th percentile is 2.817 kPa.
- During 12:00-17:00 over that heat run, mean VPD is 2.774 kPa, the 90th percentile is 3.299 kPa, and 27 afternoon hours reach at least 3 kPa.
- Maximum event-window VPD is 3.539 kPa, occurring during the hottest part of the heat run.

Hydrologic low-water timing from the Poyang Lake report:

- Highest reported water level of the year occurred on 2022-06-23.
- Water level on 2022-08-06: 11.99 m.
- Water level on 2022-08-30: 8.96 m.
- Drop: 11.99 - 8.96 = 3.03 m over 24 days, or about 0.126 m/day.
- The dry-season threshold arrived roughly 100 days earlier than usual and was the earliest such date since records began in 1951.

Precipitation and remote-sensing context:

- GPM and CHIRPS precipitation summaries both cover 2022-06-01 through 2022-07-16.
- The lake low-water anchor is 2022-08-30, so the precipitation-summary end date is 45 days earlier.
- Mean accumulated precipitation is 519.7 mm for GPM and 387.6 mm for CHIRPS over that earlier window.
- Sentinel-2 dNBR and annual satellite-embedding change are useful context but do not outrank the weather and hydrologic timing signals.

# Ranking Logic

The mechanism score is not an impact-priority score. It estimates explanatory dominance for the heat-drought diagnosis.

`persistent_heat_load` ranks first with 96 because it has the strongest direct quantitative support: a 17-day Tmax run, an 11-day warm-night run, a 16-day apparent-heat run, and substantial heat-degree load.

`hydrologic_low_water_timing` ranks second with 90 because the Poyang evidence shows a large, rapid lake-level fall, an unusually early dry-season threshold, and an earliest-since-1951 timing anchor. It is the strongest drought outcome/timing mechanism, but it is not the leading atmospheric driver.

`evaporative_demand` ranks third with 82. VPD is high during the heat run, especially in the afternoon, so it is a strong amplifier of water stress. It is kept below the first two mechanisms because it is derived from the heat and humidity series rather than an independent endpoint.

`precipitation_deficit_only` ranks fourth with 42. The report identifies lack of rain, but the available gridded precipitation summaries end 45 days before the August 30 low-water anchor and show accumulated rainfall over an earlier window. It is context, not a sufficient sole explanation.

`reported_loss_or_exposure_only` ranks last with 8. Reported disruptions and affected populations are consequences and context, not a physical mechanism.

# Reasoning Path

The dominant chain is persistent heat load over the event window, reinforced by humidity-derived evaporative demand and confirmed by rapid, unusually early Poyang low-water timing. A rainfall-only explanation is demoted by the timing gap between available precipitation summaries and the August low-water minimum. A loss/exposure-only explanation is rejected because it describes outcomes rather than physics.

# Scoring Rubric

Total: 20 points.

- 4 points: Final ranking and dominant mechanism. Full credit requires `persistent_heat_load` first, `hydrologic_low_water_timing` second, `evaporative_demand` third, `precipitation_deficit_only` fourth, `reported_loss_or_exposure_only` fifth, and the answer label `persistent_heat_load_dominant_with_hydrologic_low_water_support`. Partial credit: 2-3 points if persistent heat is first but the second and third mechanisms are reversed; 1 point for a heat-drought ranking without the specified labels.
- 4 points: Heat persistence calculations. Full credit requires 17 days of Tmax >= 35C, 11 days of Tmin >= 28C, 16 days of apparent temperature max >= 40C, and heat-degree support. Partial credit: 2-3 points for correct heat and warm-night runs with missing apparent-heat detail; 1 point for only counting hot days.
- 3 points: Evaporative-demand calculations. Full credit requires the VPD formula, heat-run afternoon mean near 2.77 kPa, heat-run VPD p90 near 2.82 kPa, and maximum VPD near 3.54 kPa. Partial credit: 1-2 points for a humidity or apparent-heat proxy without the correct VPD calculation.
- 4 points: Hydrologic low-water timing. Full credit requires 11.99 m on 2022-08-06, 8.96 m on 2022-08-30, the 3.03 m drop over 24 days, about 0.126 m/day, and roughly 100 days early dry-season timing. Partial credit: 2-3 points for the drop without complete timing; 1 point for only noting that Poyang Lake was low.
- 2 points: Precipitation-only demotion. Full credit requires the 2022-07-16 precipitation-summary end date, the 2022-08-30 low-water date, the 45-day gap, and the conclusion that precipitation deficit alone is contextual rather than dominant. Partial credit: 1 point for mentioning rainfall context without the phase-gap calculation.
- 3 points: Rejected non-mechanism and output discipline. Full credit requires rejecting `reported_loss_or_exposure_only`, avoiding AOI/population/exposure dependencies, avoiding response-priority advice, and returning compact JSON with the requested top-level keys. Partial credit: 1-2 points for the right physical stance with extra impact-triage language.
