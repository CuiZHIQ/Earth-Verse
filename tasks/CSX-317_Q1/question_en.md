# Lake Palcacocha Rapid-Impact Priority

A mountain-hazards team in Ancash, Peru, is preparing a rapid briefing for
Huaraz based on the Lake Palcacocha glacial-lake flood record. The team needs a
compact mechanism diagnosis and a downstream emergency-planning priority class,
with enough numerical support to distinguish a glacier/lake outburst threat from
weather-driven flooding.

Use the incident record's supported values for threatened city population,
estimated flood travel time to Huaraz, historical fatalities from the earlier
lake-overflow disaster, and same-day precipitation context. Compute:

`priority_index = log10(threatened_city_population) + historical_fatalities / 1000 + max(0, 60 - flood_arrival_minutes) / 10`

Assign `priority_class` as `critical` if the index is at least 15, `high` if it
is at least 10, `moderate` if it is at least 5, and `low` otherwise. Choose the
best compact mechanism label from:

- `glacier_collapse_lake_outburst_downvalley_flood`
- `rainfall_only_river_flood`
- `wind_driven_coastal_surge`
- `slow_seasonal_snowmelt_rise`

Return your answer as:

```json
{
  "answer": "<compact_mechanism_label>",
  "priority_class": "<class>",
  "priority_index": "<value rounded to 2 decimals>",
  "key_metrics": {
    "threatened_city_population": "<value>",
    "flood_arrival_minutes": "<value>",
    "historical_fatalities": "<value>",
    "event_precipitation_mm": "<value>"
  },
  "impact_chain": ["<trigger>", "<process>", "<impact>"]
}
```

Base the response on the incident record and do not add unsupported modern
casualty, inundation-depth, or discharge estimates.
