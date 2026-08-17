# Correct Answer

```json
{
  "answer": "compound_heat_water_stress",
  "event_window": {
    "start": "2022-06-01",
    "end": "2022-08-31",
    "days": 92
  },
  "computed_evidence": {
    "daytime_heat_load": {
      "tmax35_run_days": 17,
      "tmax35_run_window": {
        "start": "2022-08-07",
        "end": "2022-08-23"
      },
      "tmax35_excess_c_days": 21.8,
      "apparent40_run_days": 16,
      "apparent40_run_window": {
        "start": "2022-08-08",
        "end": "2022-08-23"
      },
      "supports_persistent_heat_load": true
    },
    "nighttime_recovery": {
      "tmin25_run_days": 25,
      "tmin25_run_window": {
        "start": "2022-08-01",
        "end": "2022-08-25"
      },
      "tmin28_run_days": 11,
      "tmin28_run_window": {
        "start": "2022-08-12",
        "end": "2022-08-22"
      },
      "recovery_failed": true
    },
    "poyang_storage_stress": {
      "aug06_level_m": 11.99,
      "aug30_level_m": 8.96,
      "drop_m": 3.03,
      "drop_rate_m_per_day": 0.126,
      "early_dry_days": 100,
      "supports_storage_stress": true
    },
    "proxy_evidence_check": {
      "dnbr_mean": -0.016,
      "annual_embedding_mean_change": 0.021,
      "image_or_burn_change_primary_rejected": true
    }
  },
  "mechanism_chain": [
    {
      "stage": "persistent_daytime_heat_load",
      "evidence": {
        "tmax35_run_days": 17,
        "tmax35_excess_c_days": 21.8,
        "apparent40_run_days": 16
      },
      "process_role": "Sustained daytime and apparent-heat loading defines a persistent heat forcing rather than an isolated peak."
    },
    {
      "stage": "failed_nocturnal_recovery",
      "evidence": {
        "tmin25_run_days": 25,
        "tmin28_run_days": 11
      },
      "process_role": "Warm nights reduce physiological and environmental recovery, strengthening the compound heat-stress interpretation."
    },
    {
      "stage": "lake_storage_drawdown",
      "evidence": {
        "poyang_drop_m": 3.03,
        "drop_rate_m_per_day": 0.126,
        "early_dry_days": 100
      },
      "process_role": "The Poyang Lake level drop links the heat episode to water-storage stress rather than heat exposure alone."
    },
    {
      "stage": "weak_image_proxy_exclusion",
      "evidence": {
        "dnbr_mean": -0.016,
        "annual_embedding_mean_change": 0.021
      },
      "process_role": "Weak mean image-change values rule out an image-only or burn-change-primary explanation for this task."
    }
  ],
  "evidence_weighting": {
    "decisive": [
      "17-day Tmax >= 35 C run with 21.8 C-days of heat excess",
      "25-day Tmin >= 25 C run and 11-day Tmin >= 28 C run showing failed night recovery",
      "3.03 m Poyang Lake drawdown over 24 days with dry-season level about 100 days early"
    ],
    "contextual": [
      "Sentinel-2 dNBR mean and annual embedding mean change as proxy checks",
      "event metadata identifying a heat-wave drought setting"
    ],
    "insufficient_as_primary": [
      "single peak heat value without persistence",
      "image or burn-change proxy without strong mean change"
    ]
  },
  "counterfactual_tests": [
    {
      "hypothesis": "peak_only_heat_episode",
      "ruling": "rejected",
      "reason": "The 17-day Tmax >= 35 C run, 16-day apparent-temperature >= 40 C run, and 21.8 C-days of exceedance show persistent load rather than a single peak."
    },
    {
      "hypothesis": "image_or_burn_change_primary",
      "ruling": "rejected",
      "reason": "Mean dNBR is -0.016 and annual embedding mean change is 0.021, both weak enough to keep image change contextual rather than primary."
    },
    {
      "hypothesis": "heat_without_water_storage_stress",
      "ruling": "rejected",
      "reason": "Poyang Lake fell from 11.99 m to 8.96 m, a 3.03 m drop at 0.126 m/day, and reached dry-season level about 100 days early."
    }
  ],
  "bounded_interpretation": "The package supports a coupled heat-water stress process, but these values do not by themselves quantify casualties, economic losses, crop loss, or complete basin-wide drought severity.",
  "source_paths": [
    "metadata/event.json",
    "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
    "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json",
    "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json",
    "data/other/other_003_01_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html.html"
  ]
}
```

# Solving Path

1. Use the event metadata and Open-Meteo daily series to establish the 92-day June-August 2022 analysis window.
2. Compute the heat process evidence: the longest `Tmax >= 35 C` run is 17 days, the heat excess over 35 C is 21.8 C-days, and the longest apparent-temperature run at or above 40 C is 16 days.
3. Compute nighttime recovery evidence: `Tmin >= 25 C` persists for 25 days and `Tmin >= 28 C` persists for 11 days, so the event is not just a daytime peak.
4. Extract Poyang Lake levels from the NASA report: Xingzi Station falls from 11.99 m on August 6 to 8.96 m on August 30. The drop is 3.03 m, or 0.126 m/day across 24 days, and the dry-season level arrived about 100 days early.
5. Use dNBR and annual embedding change only as proxy checks. Their means, -0.016 and 0.021, are too weak to make image change or burn change the primary explanation.
6. Combine the evidence into a compound mechanism chain and reject the peak-only, image-only, and heat-without-water-storage alternatives.

# Scoring Rubric

Total: 20 points.

- 3 points: Correct mechanism-diagnosis JSON shape and answer `compound_heat_water_stress`.
- 4 points: Correct daytime heat evidence, including the 17-day `Tmax >= 35 C` run, 21.8 C-days of heat excess, and 16-day apparent-temperature run.
- 3 points: Correct nighttime recovery evidence, including the 25-day `Tmin >= 25 C` run and 11-day `Tmin >= 28 C` run.
- 4 points: Correct Poyang storage-stress evidence: 11.99 m, 8.96 m, 3.03 m drop, 0.126 m/day, and about 100 days early.
- 3 points: Correct counterfactual rejection for peak-only heat, image-or-burn-primary, and heat-without-water-storage explanations.
- 2 points: Correct proxy-evidence weighting for dNBR and embedding change.
- 1 point: Bounded interpretation without unsupported casualty, loss, crop-loss, or basin-wide severity claims.
