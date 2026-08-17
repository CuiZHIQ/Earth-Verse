# Saharan Dust Plume Consistency Test

A technical review team is checking a proposed diagnosis for the 18-21 January 2022 Saharan dust outbreak over the Atlantic. Test whether the supplied event data satisfy a north-weighted transported-dust signal rather than a spatially uniform haze signal or a precipitation-confounded scene.

Use the paired pre-event and event RGB scenes to compute a dust-color index for the full scene, northern half, and southern half:

`DCI = mean((R + G) / (2 * max(B, 1)))`

Only include pixels whose RGB mean brightness is greater than 20 and less than 245. For each region, compute `delta_DCI = event_DCI - pre_DCI`. Then compute `ns_contrast_DCI = north_delta_DCI - south_delta_DCI` and `contrast_to_abs_full = ns_contrast_DCI / max(abs(full_delta_DCI), 0.001)`.

Use these thresholds: the image signal is consistent with north-weighted transport only if `north_delta_DCI >= 0.02`, `south_delta_DCI < 0`, `ns_contrast_DCI >= 0.08`, and `contrast_to_abs_full >= 10`. The reported plume-length check passes at `>= 3000 km`. The precipitation-confounder check fails if the largest event-total precipitation cell maximum reaches `10 mm`.

Return compact JSON with exactly these fields:

```json
{
  "plume_length_km": 0,
  "north_delta_dci": 0,
  "south_delta_dci": 0,
  "full_delta_dci": 0,
  "ns_contrast_dci": 0,
  "contrast_to_abs_full": 0,
  "precip_largest_cell_max_mm": 0,
  "conclusion": ""
}
```

Round DCI-derived values to 6 decimals, the contrast ratio to 3 decimals, and precipitation to no more than 6 decimals. Use a short computed conclusion label.
