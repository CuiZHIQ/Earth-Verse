# Dust Mobility Wetness Index

During the March 2021 East Asia dust storm, a forecast analyst wants a compact physical index to decide whether the short event window favored continued dust mobility under limited wet removal, or whether rainfall-driven washout should dominate the interpretation.

Use this event-specific index:

`dust_mobility_wetness_index = peak_10m_wind_kmh / (1 + wettest_event_mean_precip_mm)`

where `peak_10m_wind_kmh` is the strongest daily 10 m wind value available in the event-window daily weather diagnostics, and `wettest_event_mean_precip_mm` is the largest event-window mean or point-total precipitation value among the precipitation diagnostics. Also count how many event-window days have daily wind at least 18 km/h and daily precipitation at most 1 mm.

Return your response as compact JSON:

```json
{
  "answer": "<interpretation_label>",
  "index": "<one_decimal_value>",
  "peak_wind_kmh": "<one_decimal_value>",
  "wettest_mean_precip_mm": "<one_decimal_value>",
  "dry_windy_days": "<integer>",
  "diagnosis": "<one_sentence>"
}
```
