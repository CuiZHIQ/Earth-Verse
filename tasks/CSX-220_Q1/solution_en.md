# Final Answer

```json
{
  "mechanism_label": "quick_clay_landslide",
  "footprint": {
    "runout_width_m": 300,
    "runout_length_m": 700,
    "rectangle_area_ha": 21.0,
    "debris_flow_area_ha": 9
  },
  "rainfall": {
    "antecedent_5_day_precip_mm": 72.2,
    "event_day_precip_mm": 8.9,
    "wetness_index_mm_day": 14.44,
    "event_day_fraction": 0.1233
  },
  "change_signal": {
    "radar_abs_mean": 0.6378,
    "optical_abs_mean": 0.3457,
    "embedding_mean": 0.0912,
    "dominant_mean_signal": "radar_abs_mean",
    "radar_to_optical_ratio": 1.845
  },
  "exposure_context": {
    "population_sum_rounded": 1059042,
    "population_millions": 1.059
  },
  "diagnosis_label": "large_quick_clay_footprint_wet_context_radar_dominant"
}
```

# Key Computations

The CSX-220 record identifies the 30 December 2020 Ask/Gjerdrum event as a quick-clay landslide in Norway.

The report extract states a flow-off footprint of 300 by 700 metres and an additional 9 hectares affected by debris flow. The rectangular footprint proxy is:

`300 * 700 / 10000 = 21.0 ha`

The five-day precipitation window is 2020-12-26 through 2020-12-30:

- 2020-12-26: 7.7 mm
- 2020-12-27: 31.6 mm
- 2020-12-28: 16.2 mm
- 2020-12-29: 7.8 mm
- 2020-12-30: 8.9 mm

The five-day total is `7.7 + 31.6 + 16.2 + 7.8 + 8.9 = 72.2 mm`. The wetness index is `72.2 / 5 = 14.44 mm/day`. The event-day fraction is `8.9 / 72.2 = 0.1233`.

The rounded mean-change values are:

- radar absolute mean backscatter change: `abs(0.6378) = 0.6378`
- optical absolute mean surface-change index: `abs(0.3457) = 0.3457`
- coarse annual embedding mean change: `0.0912`

The largest mean-change magnitude is `radar_abs_mean`. The radar-to-optical ratio is `0.6378 / 0.3457 = 1.845`.

The rounded population exposure context is 1,059,042 people, or `1059042 / 1000000 = 1.059` million.

# Reasoning Path

The answer is a numeric diagnosis rather than a general landslide explanation. The mechanism label is `quick_clay_landslide` because the event record identifies the Ask/Gjerdrum failure as quick-clay mass movement.

The footprint values establish the scale of the ground failure: a 300 m by 700 m flow-off footprint gives a 21.0 ha rectangular proxy, and the report separately gives 9 ha of debris-flow affected area. These values support the `large_quick_clay_footprint_wet_context_radar_dominant` diagnosis label.

The rainfall ledger supplies context, not a trigger proof. The five-day total of 72.2 mm and 14.44 mm/day wetness index indicate a wet antecedent window, while the event day accounts for only 0.1233 of the five-day total.

The remote-change ledger is a numeric magnitude comparison. Radar has the largest mean-change magnitude and is about 1.845 times the optical mean-change value, so the surface-change diagnosis is radar-dominant by the stated rule; the embedding value remains coarse annual context rather than event-timed proof.

Population is included only as exposure context. It is not a loss estimate and is not used to infer casualties, destroyed structures, or emergency decisions.

# Computed Interpretation

The compact result is a large quick-clay landslide footprint with wet antecedent context and radar-dominant surface-change evidence; rainfall and population values should remain contextual numeric anchors.

# Scoring Rubric

Total: 20 points.

- Output schema and final diagnosis label: 3 points. Full credit for returning the requested six-key JSON object with `mechanism_label` and `diagnosis_label` equal to the expected quick-clay, wet-context, radar-dominant diagnosis; partial credit for a valid but incomplete object or a generic landslide label.
- Footprint calculation: 3 points. Full credit for 300 m width, 700 m length, 21.0 ha rectangular footprint proxy, and 9 ha debris-flow area; partial credit for correct source values with a missing or miscomputed rectangle-area conversion.
- Rainfall ledger: 4 points. Full credit for the five daily values, 72.2 mm total, 8.9 mm event-day precipitation, 14.44 mm/day wetness index, and 0.1233 event-day fraction; partial credit for the correct window with minor rounding errors.
- Change-signal comparison: 4 points. Full credit for 0.6378 radar, 0.3457 optical, 0.0912 coarse annual embedding context, `radar_abs_mean` as the dominant mean signal, and 1.845 radar-to-optical ratio; partial credit for identifying radar as largest without all supporting values.
- Exposure context: 2 points. Full credit for 1,059,042 rounded population and 1.059 million; partial credit for one of the two values or a small rounding mistake.
- JSON-implied formula consistency: 2 points. Full credit when the returned JSON values are internally consistent with the area, wetness, event-day fraction, and radar-to-optical formulas; no prose or formula strings outside the JSON are required. Partial credit when most values are correct but one derived value is not formula-consistent.
- Overclaim control: 2 points. Full credit for avoiding claims that rainfall proves the trigger or that population exposure is confirmed loss; partial credit for one correct caution with another extra escalation.
