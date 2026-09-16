# Final Answer

```json
{
  "plume_length_km": 4000,
  "north_delta_dci": 0.034708,
  "south_delta_dci": -0.07372,
  "full_delta_dci": -0.003583,
  "ns_contrast_dci": 0.108428,
  "contrast_to_abs_full": 30.262,
  "precip_largest_cell_max_mm": 5.657702,
  "conclusion": "north_weighted_transported_dust_consistent"
}
```

# Key Computations

The reported dust plume length is 4000 km, so it clears the 3000 km transported-plume threshold.

For each RGB scene, valid pixels have mean brightness greater than 20 and less than 245. The dust-color index is `DCI = mean((R + G) / (2 * max(B, 1)))`.

The full-scene DCI changes from 1.132456 to 1.128873, so `full_delta_dci = -0.003583`. The northern half changes from 1.323652 to 1.358360, so `north_delta_dci = 0.034708`. The southern half changes from 0.946838 to 0.873118, so `south_delta_dci = -0.073720`.

The north-south contrast is `0.034708 - (-0.073720) = 0.108428`. The normalized contrast is `0.108428 / max(abs(-0.003583), 0.001) = 30.262`. The largest event-total precipitation cell maximum across the event precipitation summaries is 5.657702 mm, below the 10 mm wet-confounder cutoff.

# Reasoning Path

The threshold proof passes the transported-dust image test: the northern DCI increase is at least 0.02, the southern DCI decreases, the north-south contrast is above 0.08, and the contrast-to-full ratio is far above 10. A spatially uniform haze signal would require coherent positive changes across the scene, but the full-scene delta is slightly negative and the southern delta is negative. A precipitation-confounded scene is also not supported by the event-total cell maximum, which remains below 10 mm.

# Computed Consequence

The computed consequence is a north-weighted transported Saharan dust signal, not a uniform-scene haze or rainfall-driven visual artifact.

# Scoring Rubric

- 3 points: Returns the requested compact JSON fields with numeric values and the conclusion label. Partial credit: 1-2 points for mostly correct structure with missing fields or inconsistent rounding.
- 4 points: Applies the DCI formula and valid-pixel brightness filter correctly for full, northern, and southern regions. Partial credit: 2 points for using the DCI formula but omitting or misapplying the brightness filter.
- 5 points: Computes the key image anchors correctly: north delta near 0.034708, south delta near -0.073720, full delta near -0.003583, and north-south contrast near 0.108428. Partial credit: 1 point per correct image anchor, with 1 additional point for correct signs.
- 5 points: Applies the threshold proof correctly, including the 30.262 contrast-to-full ratio and the pass state for the north-weighted image signal. Partial credit: 2 points for the correct qualitative pass state with incomplete arithmetic.
- 2 points: Uses the 4000 km plume length and the 5.657702 mm precipitation maximum in the consistency test. Partial credit: 1 point for only one of these anchors.
- 1 point: Keeps the final computed consequence concise and does not assert measured aerosol concentration, surface damage, or realized impacts. Partial credit: 1 point for a correct label with one minor overstatement.
