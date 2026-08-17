# Final Answer

The correct answer is `coupled_summit_drainage_lerz_effusion`.

The physical index is `summit_collapse_to_lava_flow_volume_ratio = 1.0`. This means the summit-collapse volume and lava-flow volume are roughly equivalent, supporting a coupled-system diagnosis rather than an isolated lower-rift or isolated summit interpretation.

## Key Computations

Hidden records used:

- `metadata/event.json`: confirms package identity, event name, and volcanic hazard family.
- `data/event_reports/event_reports_003_Locked_event_anchor_2018_Kilauea_eruption.json`: confirms the local event lock and temporal window.
- `data/event_reports/event_reports_004_USGS_Kilauea_2018_summit_collapse_and_Lower_East_Rift_Zone_eruption.html`: provides the event-specific physical mechanism and numeric measurements used for the index.

Files not selected:

- Precipitation, exposure, catalog, and generic search files are not needed for this mechanism-index question.
- Remote-sensing preview images are not needed because the requested diagnosis is supported directly by the local event mechanism text and quantitative volume statement.

## Text Claims/Package Claims

- The package identifies the event as the 2018 Kilauea eruption in the `volcano_ash_lahar` hazard family.
- The local event anchor gives the window from 2018-05-03 to 2018-08-04 in Hawaii.
- The USGS report describes the event as the largest lower East Rift Zone eruption and caldera collapse in at least 200 years.
- After the Pu'u 'O'o vent collapsed on 30 April, magma propagated downrift and eruptive fissures opened in the lower East Rift Zone on 3 May.
- Fissures eventually extended about 6.8 km, lava erupted at rates exceeding 100 cubic meters per second, and lava covered 35.5 square kilometers.
- The summit magma system partially drained and produced near-daily collapses with energy equivalent to Mw 4.7 to 5.4 earthquakes.
- Summit-collapse and lava-flow volume estimates are described as roughly equivalent, about 0.8 cubic kilometers.

`compute_gt.py` reads only local package files. It:

- Parses `metadata/event.json` and the locked event anchor JSON.
- Converts the USGS HTML report into plain ASCII text.
- Extracts fissure length, minimum lava rate, lava-covered area, main earthquake magnitude, summit-collapse energy range, and the about 0.8 cubic kilometer volume statement.
- Computes `summit_collapse_to_lava_flow_volume_ratio` as summit-collapse volume divided by lava-flow volume.
- Scores the coupled-system diagnosis using downrift magma propagation, summit partial drainage, equivalent volumes, high lava rate, fissure extent, and collapse-energy evidence.
- Writes `computed_gt.json` deterministically.

## Intermediate Values

```json
{
  "fissure_length_km": 6.8,
  "minimum_lava_rate_m3_s": 100.0,
  "lava_area_sq_km": 35.5,
  "main_earthquake_mw": 6.9,
  "summit_collapse_energy_mw_range": [4.7, 5.4],
  "summit_collapse_volume_km3": 0.8,
  "lava_flow_volume_km3": 0.8,
  "summit_collapse_to_lava_flow_volume_ratio": 1.0,
  "coupled_score": 10
}
```

## Reasoning Chain

1. A purely lower-rift interpretation explains fissures, lava rate, and lava area, but it does not explain partial summit magma-system drainage and near-daily summit collapses.
2. A purely summit-collapse interpretation explains caldera-collapse behavior, but it does not explain downrift magma propagation, lower East Rift Zone fissures, and high-rate lava effusion.
3. A rainfall-triggered interpretation is not supported by the mechanism text for this question.
4. The volume index is decisive: the summit-collapse and lava-flow volumes are both about 0.8 cubic kilometers, giving a ratio of 1.0.
5. A ratio near 1, combined with downrift magma propagation and partial summit drainage, supports a coupled summit-drainage and lower-rift effusion diagnosis.
6. The operational implication is that the event should be reasoned about as a linked volcanic plumbing-system crisis, not as one isolated surface hazard.

## Reasoning Path

The answer hinges on whether lower-rift effusion and summit collapse are separate stories or a coupled volcanic plumbing-system response. Downrift magma propagation and lower East Rift Zone fissures explain the surface effusion, while summit partial drainage and near-daily collapses explain the caldera response. The physical index links the two: summit-collapse volume and lava-flow volume are both about 0.8 km3, so their ratio is 1.0. That near-equivalence makes the coupled diagnosis stronger than isolated lower-rift, isolated summit, or rainfall-triggered interpretations.

## Unsupported Overclaims

- Do not claim exact casualty totals, evacuation totals, or destroyed-structure counts from this evidence.
- Do not claim that the volume ratio proves a complete magma budget; it is a package-supported diagnostic index, not a full petrologic accounting.
- Do not infer detailed lava chemistry, gas concentration, ashfall thickness, or vent-by-vent chronology unless supported by additional local files.
- Do not convert this into a package-quality or event-existence task.

## Scoring Rubric

Total: 20 points.

- 4 points: Gives the diagnosis `coupled_summit_drainage_lerz_effusion` or an equivalent coupled summit-drainage and lower-rift effusion diagnosis.
- 3 points: Identifies the physical index as the summit-collapse to lava-flow volume ratio.
- 4 points: Computes or reports the index value as 1.0 from roughly equal 0.8 km3 summit-collapse and lava-flow volumes.
- 3 points: Uses downrift magma propagation, lower East Rift Zone fissure opening, 6.8 km fissure extent, high lava rate, or 35.5 km2 lava coverage as lower-rift evidence.
- 3 points: Uses summit partial drainage, near-daily collapses, Mw 4.7 to 5.4 collapse-energy evidence, or Mw 6.9 earthquake context as summit-system evidence.
- 2 points: Rejects isolated rift-only, isolated summit-only, and rainfall-triggered interpretations for mechanism-based reasons.
- 1 point: Avoids unsupported claims about casualties, evacuation totals, lava chemistry, gas concentration, ashfall thickness, or a complete magma budget.

## Disaster Interpretation

This is a linked volcanic-system diagnosis. The lower East Rift Zone eruption and the summit-collapse sequence should be analyzed together because the physical volume index and mechanism text connect summit drainage to downrift magma propagation and effusion. The ratio is not a full petrologic mass balance, but it is a compact, reproducible diagnostic showing that the summit and rift-zone components are comparable enough to reject isolated single-component explanations.
