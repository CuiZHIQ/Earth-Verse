# Early-Season Heat-Stress Numeric Diagnosis

A heat-risk review team is checking the March 1 to May 15, 2022 India-Pakistan pre-monsoon heatwave for a compact index-based diagnosis. The question is whether the event is better characterized by persistent early-season dry heat with poor night recovery, by humid heat approaching a wet-bulb ceiling, or by a short isolated hot-day spike.

Compute a numeric ledger for the event window and use it to make the mechanism diagnosis. Treat the package-local Open-Meteo daily/hourly series as the representative point sequence for these numeric heat-stress calculations; broader package products are context only unless they contain the required fields. Use these definitions:

- `peak_tmax_c`: maximum daily maximum temperature.
- `run_tmax_ge40_d`: longest consecutive run of days with daily maximum temperature at or above 40 C.
- `warm_nights_ge25`: count of nights with daily minimum temperature at or above 25 C.
- `peak_wbt_c`: maximum estimated hourly wet-bulb temperature.
- `acclim_anom_c`: maximum 3-day mean daily temperature minus the preceding 30-day mean, with daily mean temperature defined as `(Tmax + Tmin) / 2`.

Apply these gates: persistent heat passes if `run_tmax_ge40_d >= 7`; warm-night recovery loss passes if `warm_nights_ge25 >= 20`; early-season jump passes if `acclim_anom_c >= 4.0`; wet-bulb ceiling passes only if `peak_wbt_c >= 28.0`; isolated-spike framing passes only if `run_tmax_ge40_d <= 2`.

Return compact JSON only:

```json
{
  "target_family": "numeric_diagnosis",
  "metrics": {
    "peak_tmax_c": 0.0,
    "run_tmax_ge40_d": 0,
    "warm_nights_ge25": 0,
    "peak_wbt_c": 0.0,
    "acclim_anom_c": 0.0
  },
  "gates": {
    "persistent_heat": false,
    "warm_night_recovery_loss": false,
    "early_season_jump": false,
    "wet_bulb_ceiling": false,
    "isolated_spike": false
  },
  "answer": "<mechanism_label>",
  "rejected_alternative": "<one short label>",
  "computed_consequence": "<one short sentence tied to the ledger>"
}
```
