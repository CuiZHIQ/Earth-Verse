# Final Answer

```json
{
  "answer": "gridded_smoke_persistence_threshold_ledger",
  "event_window": {
    "start": "2021-03-26",
    "end": "2021-04-10",
    "days": 16
  },
  "heat_block": {
    "era5_tmax_max_c": 40.51,
    "era5_tmax_mean_c": 36.63,
    "era5_tmax_min_c": 32.99,
    "heat_score": 3
  },
  "precipitation_block": {
    "era5_precip_mean_mm": 6.97,
    "gpm_precip_mean_mm": 12.14,
    "chirps_precip_mean_mm": 19.39,
    "precip_consensus_mean_mm": 12.83,
    "low_tail_flags": {
      "era5_min_le_1mm": true,
      "gpm_min_le_1mm": true,
      "chirps_min_le_1mm": true
    },
    "low_precip_tail_score": 3
  },
  "wind_block": {
    "era5_mean_u_m_s": 0.14,
    "era5_mean_v_m_s": 1.62,
    "mean_wind_speed_m_s": 1.63,
    "era5_max_u_m_s": 1.33,
    "era5_max_v_m_s": 3.5,
    "max_wind_vector_screen_m_s": 3.74,
    "mean_vent_deficit_m_s": 1.87,
    "ventilation_score": 2
  },
  "aggregate_persistence_index": 13.0,
  "threshold_flags": {
    "hot_gridded": true,
    "low_precip_tail": true,
    "weak_ventilation": true,
    "index_ge_12": true
  },
  "brief_method": "Use the locked window, ERA5 gridded heat score, ERA5/GPM/CHIRPS low-precipitation tail score, ERA5 wind-vector ventilation score, and 2-decimal aggregate index rounding."
}
```

# Key Computations

The locked incident window contains 16 inclusive dates, from 2021-03-26 through 2021-04-10.

The ERA5-Land heat block passes all three heat checks:

```text
max Tmax = 40.51 C >= 40 C
mean Tmax = 36.63 C >= 35 C
min Tmax = 32.99 C >= 32 C
heat_score = 3
```

The precipitation block uses ERA5-Land, GPM, and CHIRPS event-window summaries:

```text
precip_consensus_mean_mm = (6.97 + 12.14 + 19.39) / 3 = 12.83
```

All three products have a minimum precipitation value at or below 1 mm, so `low_precip_tail_score = 3`.

The ERA5 wind-vector block gives:

```text
mean_wind_speed = sqrt(0.14^2 + 1.62^2) = 1.63 m/s
max_wind_vector_screen = sqrt(1.33^2 + 3.50^2) = 3.74 m/s
mean_vent_deficit = 3.5 - 1.63 = 1.87 m/s
ventilation_score = 2
```

The aggregate index is:

```text
aggregate_persistence_index = 2*3 + 3 + 2*2 = 13.00
```

# Reasoning Path

This ledger uses gridded aggregate evidence rather than point-weather daily rows. The heat block checks whether the whole event window is hot in ERA5-Land. The precipitation block checks both consensus rainfall and whether all three precipitation products contain a low-precipitation tail. The wind block uses vector magnitude rather than one component alone.

All threshold flags are true, and the aggregate index is above 12, so the answer label is `gridded_smoke_persistence_threshold_ledger`.

# Computed Interpretation

The computed ledger shows gridded hot conditions, at least one low-precipitation tail in every precipitation product, and weak mean ventilation during the locked incident span. It is an aggregate weather-threshold index, not a direct pollution concentration measurement.

# Scoring Rubric

- 3 points: Uses the locked 2021-03-26 to 2021-04-10 date span and reports 16 incident-window days. partial_credit: Award 1-2 points for the right date span with one off-by-one day-count or endpoint error.
- 4 points: Reports ERA5 max, mean, and minimum Tmax values and `heat_score = 3`. partial_credit: Award 1-3 points for mostly correct temperature values with one threshold or rounding mistake.
- 4 points: Reports ERA5, GPM, CHIRPS, consensus precipitation means, all three low-tail flags, and `low_precip_tail_score = 3`. partial_credit: Award up to 3 points for correct subsets of the precipitation means, flags, and score.
- 4 points: Computes mean wind speed, maximum wind-vector screen, mean ventilation deficit, and `ventilation_score = 2`. partial_credit: Award 1-3 points for mostly correct vector calculations with one threshold or rounding mistake.
- 4 points: Computes `aggregate_persistence_index = 13.00` and all four threshold flags as true. partial_credit: Award 2-3 points for the right direction with one arithmetic or flag error.
- 1 point: Includes the requested answer label and brief method note without replacing the numeric ledger with prose. partial_credit: Award 0.5 point for a correct label or method note when the other is missing or too vague.
