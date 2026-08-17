# Correct Answer

```json
{
  "process_model": {
    "event_window": {
      "start": "2015-06-01",
      "end": "2016-05-31"
    },
    "drought_stress_index": 84.24,
    "response_priority_score": 78.05,
    "severity_class": "severe_teleconnected_livelihood_crisis"
  },
  "computed_metrics": {
    "teleconnection_norm": 1.0,
    "rainfall_crop_failure_norm": 0.625,
    "landscape_degradation_norm": 0.785,
    "livelihood_response_pressure_norm": 0.862,
    "precipitation_uncertainty_norm": 0.966,
    "facility_access_norm": 0.826
  },
  "scenario_analysis": {
    "continued_stress_drought_index": 87.87,
    "continued_stress_response_priority": 82.24,
    "drought_index_delta": 3.63,
    "response_priority_delta": 4.19
  },
  "mechanism_chain": [
    "A very strong 2015-2016 El Nino teleconnection raised the likelihood of failed rainy seasons over Ethiopia.",
    "Reported rainfall deficits, crop loss, livestock pressure, and food insecurity show that climate stress translated into livelihood failure.",
    "Image browning, precipitation-product spread, and mapped facilities indicate high operational pressure for response targeting."
  ],
  "source_paths": [
    "metadata/event.json",
    "data/event_reports/event_reports_002_Locked_event_anchor_2015-2016_El_Nino_and_Ethiopia_drought-food-security_crisis.json",
    "data/event_reports/event_reports_001_Locked_anchor_NOAA_Climate.gov.html",
    "data/event_catalogs/event_catalogs_001_FAO_Ethiopia_El_Nino_drought_response.html",
    "data/physical_hazard/physical_hazard_006_NOAA_CPC_ONI_ASCII.txt",
    "data/physical_hazard/physical_hazard_008_NOAA_PSL_SOI_data.data",
    "data/physical_hazard/physical_hazard_009_ERA5-Land_hourly_aggregate_stats.json",
    "data/physical_hazard/physical_hazard_010_GPM_IMERG_V07_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_011_CHIRPS_daily_event_accumulated_precipitation.json",
    "data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json",
    "data/exposure_impact/exposure_impact_005_OpenStreetMap_Overpass_bounded_AOI_slice.json",
    "data/remote_sensing/remote_sensing_002_pre.jpg",
    "data/remote_sensing/remote_sensing_003_event.jpg"
  ],
  "final_interpretation": "The package supports a severe teleconnected livelihood crisis in which a record-strength El Nino coincided with Ethiopian rainfall and crop failure, visible landscape stress, high food-security need, and elevated response-priority demand."
}
```

# Key Computations

The event window comes from the package event anchor: 2015-06-01 to 2016-05-31. The 2015-2016 CPC ONI record has peak anomaly 2.75 C and six seasons at or above 2.0 C; the monthly SOI series has a minimum of -3.6. The teleconnection component is therefore clipped to `1.000`.

The report evidence gives broad Ethiopian highland rainfall at 50%-90% of normal, so the midpoint deficit is `1 - 0.70 = 0.300`; the northeastern highland value is as little as 30% of normal, so the severe deficit is `0.700`. The FAO response report states crop production dropped by 50%-90% in some regions and failed completely in the east, giving crop-loss midpoint `0.700` and east failure flag `1`. Thus `rainfall_crop_failure_norm = 0.625`.

The package-derived paired images give `green_drop_pp = 7.972`, `dark_gain_pp = 7.826`, and `excess_green_drop = 1.541`; after normalization and weighting, `landscape_degradation_norm = 0.785`. The three event precipitation means are 193.597 mm, 203.734 mm, and 256.770 mm, giving `precip_spread_ratio = 0.290` and `precipitation_uncertainty_norm = 0.966`.

FAO reports 10.2 million people food insecure, a $50 million response plan, and a target of 1.8 million farmers and livestock keepers. NOAA reports more than 8 million people requiring food aid. This yields `livelihood_response_pressure_norm = 0.862`. The package-derived mapped-access products have population 905,846.853, 163 critical facilities, 517 highway features, and 311 building features, giving `facility_access_norm = 0.826`; these mapped-access quantities are operational indicators, not national population or infrastructure totals.

Baseline indices:

```text
drought_stress_index =
100 * (0.28*1.000 + 0.24*0.625 + 0.18*0.785 + 0.18*0.862 + 0.12*0.966)
= 84.24

response_priority_score =
100 * (0.30*0.625 + 0.25*0.862 + 0.20*0.785 + 0.15*0.826 + 0.10*0.966)
= 78.05
```

In the continued-stress scenario, the rainfall/crop component rises to `0.695`, landscape degradation to `0.864`, livelihood-response pressure to `0.869`, and precipitation uncertainty clips to `1.000`. The resulting indices are `87.87` and `82.24`, with deltas of `3.63` and `4.19`.

# Scoring Rubric

- 3 points: Uses self-directed package discovery and cites package-relative paths spanning reports, climate indices, precipitation products, exposure/infrastructure, and imagery.
- 3 points: Extracts the event window and teleconnection inputs correctly, including peak ONI, the count of very strong ONI seasons, and minimum SOI.
- 3 points: Converts report statements into rainfall and crop-failure fractions correctly, including broad midpoint deficit, severe deficit, crop-loss midpoint, and east crop-failure flag.
- 3 points: Computes the package-derived paired-image landscape degradation terms and the precipitation uncertainty ratio with correct units, clipping, and rounding.
- 3 points: Computes humanitarian and response-pressure values from food-insecurity, food-aid, response-target, and response-plan figures.
- 2 points: Computes package-derived mapped facility/access rates from population, critical facilities, roads, and buildings without treating them as national totals.
- 2 points: Applies the baseline drought-stress and response-priority formulas and assigns the correct severity class.
- 1 point: Applies the continued-stress scenario perturbations, clipping, and deltas correctly.
