# Final Answer

```json
{
  "longest_subzero_run_h": 60,
  "subzero_load_c_h": 177.4,
  "apparent_stress_c_h": 149.4,
  "snow_subzero_share": 0.809,
  "precipitation_spread_ratio": 0.851,
  "image_white_delta": 0.0179,
  "consistency_index": 95.5,
  "answer": "persistent_cold_wave_consistency_pass"
}
```

# Key Computations

The hourly temperature series has 60 consecutive hours with `T < 0`. Its
subzero cold load is:

```text
sum(max(0, -T)) = 177.4 C-h
```

Using the wind-chill formula from the prompt gives a minimum wind chill of about
`-17.1 C`. The load below the `-10 C` apparent-temperature line is:

```text
sum(max(0, -10 - WC)) = 149.4 C-h
```

The hourly snowfall total is `9.87 cm`, with `7.98 cm` occurring during
subzero hours:

```text
snow_subzero_share = 7.98 / 9.87 = 0.809
```

The event-mean precipitation summaries are `24.03 mm`, `7.37 mm`, and
`3.58 mm`, so their normalized spread is:

```text
(24.03 - 3.58) / 24.03 = 0.851
```

For the RGB images, the pre-event bright-white pixel fraction is `0.3050` and
the event fraction is `0.3229`, giving:

```text
image_white_delta = abs(0.3229 - 0.3050) = 0.0179
```

# Reasoning Path

The component scores are capped where the formula specifies a cap:

```text
duration score = min(60 / 48, 1) = 1.000
subzero-load score = min(177.4 / 150, 1) = 1.000
apparent-cold score = min(149.4 / 120, 1) = 1.000
snow phase score = 0.809
precipitation spread score = 0.851
image stability score = 1 - 0.0179 = 0.9821
```

The final index is therefore:

```text
100 * (0.25*1.000 + 0.25*1.000 + 0.20*1.000
       + 0.15*0.809 + 0.10*0.851 + 0.05*0.9821)
= 95.5
```

Because `95.5 >= 75.0`, the deterministic label is
`persistent_cold_wave_consistency_pass`. The high score comes from a long
subzero run, large cumulative cold load, strong apparent-cold load, and snowfall
mostly coincident with freezing conditions. The precipitation summaries and
small image-white shift do not replace the thermal diagnosis.

# Computed Interpretation

The event record supports a persistent cold-wave diagnosis: the thermal and
wind-chill loads alone reach their capped component scores, snowfall mostly
coincides with freezing hours, and the small image-white change is only a
secondary consistency check.

# Scoring Rubric (20 points)

- 3 points: Returns compact JSON with exactly the requested fields and the final
  deterministic label. Partial credit for correct fields with minor rounding or
  ordering differences.
- 4 points: Computes temperature persistence and cold load correctly: `60`
  consecutive subzero hours and `177.4 C-h` within tolerance. Partial credit for
  one correct metric or a correct formula with arithmetic error.
- 4 points: Applies the wind-chill formula correctly and obtains the
  `149.4 C-h` apparent-cold load below `-10 C`. Partial credit for using the
  correct formula but missing the load threshold.
- 4 points: Computes the snow phase share, precipitation spread ratio, and
  image-white delta correctly: `0.809`, `0.851`, and `0.0179`. Partial credit
  for two of the three metrics.
- 4 points: Combines the six component scores with the stated weights and
  obtains `95.5`, then applies the `75.0` threshold correctly. Partial credit
  for the right threshold result with a small weighted-sum error.
- 1 point: Gives a concise interpretation that keeps the diagnosis tied to the
  calculated cold, wind, snow, precipitation, and image metrics without adding
  uncomputed damage amounts or image-only severity statements.
