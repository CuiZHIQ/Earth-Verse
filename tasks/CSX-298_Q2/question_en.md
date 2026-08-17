# Godzilla Dust-Veil Consistency Test

A technical review team is checking the June 14-28, 2020 Saharan dust "Godzilla" outbreak across the Sahara, Atlantic, and Caribbean. Test whether the June 21 RGB scene satisfies a computed atmospheric dust-veil signal while the surface-change and point-rainfall confounder gates remain below their cutoffs.

For the paired pre-event and event RGB scenes, compute the image fractions over all RGB pixels in each package scene as delivered; no separate no-data mask is applied:

- `brightness = mean((R + G + B) / 3)`
- `blue_water_fraction = fraction of pixels with B > R + 15, B > G + 5, and B > 80`
- `tan_dust_fraction = fraction of pixels with R > G > B, R >= 95, G >= 85, R - B >= 15, and G - B >= 5`

Then compute:

- `brightness_delta = event_brightness - pre_brightness`
- `blue_water_drop_pp = 100 * (pre_blue_water_fraction - event_blue_water_fraction)`
- `tan_dust_gain_pp = 100 * (event_tan_dust_fraction - pre_tan_dust_fraction)`
- `dust_veil_index = brightness_delta / 10 + blue_water_drop_pp / 4 + tan_dust_gain_pp / 2`
- `surface_change_ratio = max(annual_surface_change_mean, annual_surface_change_stddev) / 0.02`, used only as a durable-surface-change confounder gate
- `point_rainfall_max_mm = max(point_weather_event_precip_total_1, point_weather_event_precip_total_2)`, used only as a package point-rainfall confounder gate

The six gates pass when `brightness_delta >= 8`, `blue_water_drop_pp >= 4`, `tan_dust_gain_pp >= 2`, `dust_veil_index >= 4`, `surface_change_ratio < 1`, and `point_rainfall_max_mm < 5`.

Return compact JSON with exactly these fields:

```json
{
  "brightness_delta": 0,
  "blue_water_drop_pp": 0,
  "tan_dust_gain_pp": 0,
  "dust_veil_index": 0,
  "surface_change_ratio": 0,
  "point_rainfall_max_mm": 0,
  "pass_count": 0,
  "conclusion": ""
}
```

Round the first six numeric fields to two decimals. Use an integer for `pass_count` and a short computed label for `conclusion`.
