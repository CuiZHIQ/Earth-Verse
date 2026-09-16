# Solution

## Final Answer

The correct answer is `pyroconvective_smoke_injection_priority`.

## Key Computations

- The package anchor frames the event as a compound heat, drought, wildfire, and smoke event over Australia from 2019-09-01 through 2020-02-29.
- The NASA report describes Victoria and New South Wales as experiencing severe fires after months of unusually hot, dry weather.
- The report explains that fires can create superheated updrafts, pyrocumulus, and pyrocumulonimbus, which can behave as fire-generated thunderstorms.
- The report states that smoke reached roughly 15 to 19 kilometers, high enough to reach the stratosphere.
- The report links the smoke to severe air-quality issues in New Zealand and long-distance transport across the Pacific and beyond.

`compute_gt.py` calculates:

- Daily heat persistence from Open-Meteo Tmax, including days at or above 40 C and longest run.
- Daily dryness persistence from Open-Meteo precipitation, including the longest zero-precipitation run and dry-day fraction.
- Wind support from days with maximum 10 m wind speed at or above 35 km/h.
- Hot-windy co-occurrence from days meeting both heat and wind thresholds.
- Burn or land-surface change context from Sentinel-2 dNBR and AlphaEarth annual embedding change.
- Population exposure from the WorldPop sum.
- Smoke-escalation flags from report text for pyrocumulonimbus, firestorms, stratospheric smoke, 15 to 19 km smoke height, long-distance transport, and air-quality impacts.
- A compound priority index that weights heat, dryness, wind, burn/change, smoke escalation, and population exposure.

The classification rule returns `pyroconvective_smoke_injection_priority` when the smoke-escalation score is high and the combined pyroconvective priority index exceeds the fuel-burn-only index.

The priority index uses the explicit weighted formula:

```text
100 * (0.20*heat_dryness + 0.15*dryness + 0.10*wind + 0.15*burn + 0.30*smoke + 0.10*exposure)
```

The point-weather series spans the full event window, while ERA5-Land, GPM, and CHIRPS end on 2019-10-16 and the Sentinel-2 dNBR post window ends on 2019-11-30. Those gridded and burn-change products are therefore bounded context rather than complete full-season coverage.

## Intermediate Values

```json
{
  "priority_index": 96.9,
  "heat_days_ge_40c": 38,
  "longest_dry_run_days": 79,
  "wind_days_ge_35kmh": 14,
  "hot_windy_days": 6,
  "peak_tmax_c": 46.0,
  "peak_tmax_date": "2019-12-24",
  "peak_wind_kmh": 49.2,
  "peak_wind_date": "2020-01-10",
  "sentinel2_dnbr_mean": 0.123,
  "sentinel2_dnbr_max": 0.974,
  "alphaearth_change_mean": 0.03,
  "population_exposed": 344722,
  "smoke_escalation_flags": 6,
  "evidence_scope": {
    "point_weather": "full event-window heat, dryness and wind support",
    "gridded_products": "2019-09-01 to 2019-10-16 bounded early-season context",
    "dnbr": "2019-09-01 to 2019-11-30 burn/land-surface context, not a full-season burn map",
    "population": "exposure context, not direct-harm count"
  }
}
```

Component indices:

```json
{
  "pyroconvective_priority_index": 96.9,
  "fuel_burn_index": 94.6,
  "rainfall_index": 21.6,
  "exposure_only_index": 100.0
}
```

The exposure-only index is high because population context is substantial, but it is not a mechanism. It does not override the mechanism-specific pyroconvective index.

## Reasoning Path

1. The weather metrics show a long heat-dryness setup: 38 days at or above 40 C, a 79-day no-rain run at the point sample, and 14 windy days at or above 35 km/h.
2. Sentinel-2 dNBR and AlphaEarth change indicate burn or land-surface disturbance context, so a fuel-dryness and burn-severity priority is plausible.
3. The report text adds the distinguishing escalation mechanism: fire-generated convective clouds, more than ordinary surface fire behavior, smoke reaching the stratosphere, and smoke impacts far beyond the burn area.
4. Rainfall or flood is not the main priority because the event framing, daily precipitation pattern, and report mechanism emphasize heat, dryness, fire, and smoke rather than damaging rainfall.
5. Population exposure matters for response targeting, but the primary response priority is not population alone; it is the cascading fire-atmosphere and smoke-injection pathway affecting both local and distant populations.
6. Therefore, the best priority label is `pyroconvective_smoke_injection_priority`.

## Unsupported Overclaims

- Do not claim that the point-sample weather metrics represent every burned location in Australia.
- Do not infer exact national burned area, mortality, property loss, or medical caseload from this package alone.
- Do not claim a full climatological attribution or return period from these local files.
- Do not treat dNBR as a complete national burn-severity map; it is a local remote-sensing summary.
- Do not treat population exposure as a measured count of people directly harmed.

## Disaster Interpretation

This task is about the fire-atmosphere escalation within a broader heat-drought-fire event. Fuel dryness and burn severity are necessary background, but the decisive response priority is the pyrocumulonimbus and stratospheric smoke-injection pathway because it moves the hazard beyond local flame fronts into regional and long-range air-quality impacts. Population exposure amplifies the need for response targeting, yet it is not the mechanism. Rainfall and flood pathways remain weak alternatives because the dominant event chain is hot, dry, windy fire weather, burned surface context, smoke injection, and transported air-quality impacts.

## Scoring Rubric

Total: 20 points.

- 3 points: Selects `pyroconvective_smoke_injection_priority` and reports the explicit weighted priority index near 96.9.
- 4 points: Correctly uses heat, dryness, and wind metrics, including 38 days at or above 40 C, 79 dry-run days, 14 windy days, and 6 hot-windy days.
- 4 points: Identifies smoke-escalation evidence, including pyrocumulonimbus, firestorms, smoke reaching 15-19 km, stratospheric injection, long-distance transport, and air-quality impacts.
- 3 points: Uses burn or land-surface change metrics as bounded supporting context, especially dNBR mean 0.123 and max 0.974, while noting that the dNBR post window ends before the full event period and should not become the sole priority.
- 2 points: Uses population exposure as impact context without reducing the answer to exposure-only reasoning.
- 2 points: Rejects rainfall or flood as the primary mechanism and explains why the event chain is heat-drought-fire-smoke dominated.
- 2 points: Avoids unsupported national loss, mortality, full attribution, exact burned-area, or direct-harm claims.
