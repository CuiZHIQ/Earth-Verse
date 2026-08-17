# Correct Answer

```json
{
  "brightness_delta": 10.86,
  "blue_water_drop_pp": 6.04,
  "tan_dust_gain_pp": 3.78,
  "dust_veil_index": 4.49,
  "surface_change_ratio": 0.41,
  "point_rainfall_max_mm": 2.37,
  "pass_count": 6,
  "conclusion": "dust_veil_not_surface_or_rainfall"
}
```

Exact deterministic answer anchor: `{'brightness_delta': 10.86, 'blue_water_drop_pp': 6.04, 'tan_dust_gain_pp': 3.78, 'dust_veil_index': 4.49, 'surface_change_ratio': 0.41, 'point_rainfall_max_mm': 2.37, 'pass_count': 6, 'conclusion': 'dust_veil_not_surface_or_rainfall'}`.

# Key Computations

The pre-event RGB scene has mean brightness 93.4253, blue-water fraction 0.120547, and tan-dust fraction 0.014174. The event RGB scene has mean brightness 104.2857, blue-water fraction 0.060176, and tan-dust fraction 0.052006. These fractions are computed over all RGB pixels in each package scene as delivered, with no separate no-data mask.

The image deltas are therefore `104.2857 - 93.4253 = 10.86`, `100 * (0.120547 - 0.060176) = 6.04` percentage points, and `100 * (0.052006 - 0.014174) = 3.78` percentage points. The dust-veil index is `10.86 / 10 + 6.04 / 4 + 3.78 / 2 = 4.49`.

The annual AlphaEarth surface-change mean is 0.0081677 and the standard deviation is 0.0070244, so `surface_change_ratio = max(0.0081677, 0.0070244) / 0.02 = 0.41`. The POWER and Open-Meteo event precipitation totals are 2.37 mm and 1.60 mm, so `point_rainfall_max_mm = 2.37`. These two values are confounder gates only; they do not relocate or redefine the dust-veil scene.

# Reasoning Path

All three RGB deltas cross their image gates: brightness increased by more than 8 units, blue-water fraction fell by more than 4 percentage points, and tan-dust fraction rose by more than 2 percentage points. Their combined index is also above the 4.0 cutoff.

The two confounder gates stay below their cutoffs: the surface-change ratio is below 1 and the maximum point rainfall total is below 5 mm. The six gate results are therefore `true, true, true, true, true, true`, giving `pass_count = 6`.

# Computed Consequence

The compact consequence is an atmospheric dust-veil signal, not a persistent surface-change or rainfall-driven signal.

# Scoring Rubric

- 3 points: Returns the requested JSON fields with numeric values, an integer pass count, and the expected conclusion label.
- 5 points: Computes RGB brightness, blue-water fraction, tan-dust fraction over all RGB pixels in each package scene as delivered, and the three event-minus-pre-event deltas with correct units and rounding.
- 4 points: Applies `dust_veil_index = brightness_delta / 10 + blue_water_drop_pp / 4 + tan_dust_gain_pp / 2` and reports 4.49 with the correct pass state.
- 4 points: Computes `surface_change_ratio = 0.41` and `point_rainfall_max_mm = 2.37`, then applies the two confounder gates correctly.
- 3 points: Reports six passing gates and the final label `dust_veil_not_surface_or_rainfall`.
- 1 point: Keeps the interpretation to the computed consequence and does not add durable damage, losses, or rainfall causation.
