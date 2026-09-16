# Dust-Veil Consistency Calculation

For the September 2009 Australian dust storm in eastern Australia, compute a deterministic dust-veil consistency check from the pre-event and event-window RGB scene pair plus event-window package point weather. Use the point-weather values as a dry-wind comparator, not as complete Sydney or eastern-Australia corridor wind evidence.

Use these formulas:

- `mean_luminance = mean((R + G + B) / 3)`
- `tan_fraction = count(R > G > B and R > 120 and G > 90 and B < 170) / pixel_count`
- `red_excess = mean(R - B)`
- `luminance_delta = event_mean_luminance - pre_mean_luminance`
- `tan_fraction_delta = event_tan_fraction - pre_tan_fraction`
- `red_excess_delta = event_red_excess - pre_red_excess`
- `dry_wind_index = max_point_wind_m_s / (1 + point_precip_total_mm)`
- `dust_veil_score` is the count of passed tests: `luminance_delta >= 25`, `tan_fraction_delta >= 0.02`, `red_excess_delta >= 2`, and `point_precip_total_mm <= 0.5` with `dry_wind_index >= 10`.

Return compact JSON:

```json
{
  "answer": {
    "pre_mean_luminance": 0.0,
    "event_mean_luminance": 0.0,
    "luminance_delta": 0.0,
    "tan_fraction_delta": 0.0,
    "red_excess_delta": 0.0,
    "dry_wind_index": 0.0,
    "dust_veil_score": 0,
    "classification": "<dry_wind_tan_brightening_dust_veil or mixed_or_weak_dust_signal>"
  },
  "interpretation": "<one short computed consequence>"
}
```
