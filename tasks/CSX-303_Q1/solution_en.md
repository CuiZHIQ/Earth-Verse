# Final Answer

Correct answer: `celia_saharan_dust_pathway_pass`

```json
{
  "event_days": 4,
  "peak_fraction": 0.5,
  "transport_anchor_count": 6,
  "max_countermetric_ratio": 0.847,
  "dust_pathway_index": 6.653,
  "conclusion": "celia_saharan_dust_pathway_pass"
}
```

# Key Computations

The locked event window runs from 2022-03-15 through 2022-03-18, so `event_days = 4`. The reported peak spans March 15-16, giving `peak_fraction = 2 / 4 = 0.5`.

All six transport anchors are present: the hazard family is dust or sandstorm; Storm Celia and North African air are named; passage through the Sahara is named; France, Spain, and Portugal are all named; the March 15-16 peak lies inside the March 15-18 window; and air-quality plus visibility impacts are both present. Therefore `transport_anchor_count = 6`.

The non-dust countermetric ratios are:

- `rain_ratio = max(13.86 / 25, 0.4401866867 / 10) = 0.554`
- `heat_ratio = 29.1 / 35 = 0.831`
- `wind_ratio = (21.9 / 3.6) / 10 = 0.608`
- `surface_ratio = max(0.0752410210 / 0.1, 0.5082352811 / 0.6) = 0.847`

Thus `max_countermetric_ratio = 0.847`. The index is `6 + 0.5 + (1 - 0.8470588) = 6.653`.

# Threshold Result

The threshold proof passes because `transport_anchor_count == 6`, `peak_fraction = 0.5`, `max_countermetric_ratio = 0.847 < 1`, and `dust_pathway_index = 6.653 >= 6.5`. The computed consequence is a Storm Celia Saharan dust source-to-receptor pathway; the strongest countermetric remains below its threshold.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns compact JSON with exactly the six requested fields and the threshold label. Partial credit: 1-2 points for a mostly complete object with one missing field or inconsistent rounding.
- 4 points: Computes the event duration, peak days, and peak fraction correctly from the locked dates and reported March 15-16 peak. Partial credit: 2 points for correct dates but incorrect inclusive-day arithmetic.
- 3 points: Scores all six transport anchors correctly and reports `transport_anchor_count = 6`. Partial credit: 1-2 points for missing one or two anchors.
- 5 points: Computes the four countermetric ratios with the correct thresholds and unit conversion, including `rain_ratio = 0.554`, `heat_ratio = 0.831`, `wind_ratio = 0.608`, and `surface_ratio = 0.847`. Partial credit: 1 point per correct ratio plus 1 point for using the correct maximum.
- 3 points: Applies the index formula and threshold rule correctly, including `dust_pathway_index = 6.653` and the passing state. Partial credit: 1-2 points for the right formula with one arithmetic or threshold error.
- 1 point: Keeps the computed consequence concise and tied to the threshold proof.
- 1 point: Does not add measured health burden, surface cleanup, direct losses, or rainfall-driven dominance beyond the computed ratios.
