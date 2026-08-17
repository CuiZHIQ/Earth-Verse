# Final Answer

Correct answer: `consistent_local_land_stage_not_offshore_core`.

```json
{
  "target_family": "gonu_muscat_land_stage_numeric_consistency_ledger",
  "ledger": [
    {
      "row_id": "rainfall_concentration",
      "formulae": [
        "wettest24_event_ratio = wettest_24h_mm / event_precip_mm",
        "wettest72_event_ratio = wettest_72h_mm / event_precip_mm"
      ],
      "values": {
        "event_precip_mm": 170.2,
        "wettest_24h_mm": 152.6,
        "wettest24_event_ratio": 0.9,
        "wettest_72h_mm": 170.2,
        "wettest72_event_ratio": 1.0,
        "heavy_precip_hours_ge_5mm": 12,
        "peak_hourly_precip_mm": 15.7
      },
      "verdict": "Rainfall was highly concentrated, with 90% of the event total inside the wettest 24 hours."
    },
    {
      "row_id": "wind_pressure_signature",
      "formulae": [
        "gust_to_wind_ratio = peak_gust_kmh / peak_wind_kmh"
      ],
      "values": {
        "peak_gust_kmh": 109.1,
        "peak_wind_kmh": 53.0,
        "gust_to_wind_ratio": 2.06,
        "min_pressure_hpa": 991.8,
        "pressure_fall_hpa": 14.6,
        "gust_hours_ge_75kmh": 17,
        "gust_hours_ge_100kmh": 4
      },
      "verdict": "The local point shows strong gustiness with a clear pressure drop."
    },
    {
      "row_id": "official_local_contrast",
      "formulae": [
        "official_wind_to_local_gust_ratio = official_peak_wind_kmh / local_peak_gust_kmh"
      ],
      "values": {
        "official_peak_wind_kt": 127,
        "official_peak_wind_kmh": 235.2,
        "official_min_pressure_hpa": 920,
        "official_coastal_rainfall_max_mm": 610,
        "official_muscat_wind_kmh": 100,
        "official_wind_to_local_gust_ratio": 2.16
      },
      "verdict": "The official cyclone peak was about 2.16 times the local peak gust, so the local point is not offshore-core-equivalent."
    },
    {
      "row_id": "precip_product_contrast",
      "formulae": [
        "openmeteo_to_nasa_event_precip_ratio = openmeteo_event_precip_mm / nasa_event_precip_mm",
        "local_precip_to_official_coastal_max_ratio = local_event_precip_mm / official_coastal_rainfall_max_mm",
        "gpm_to_chirps_max_ratio = gpm_max_mm / chirps_max_mm"
      ],
      "values": {
        "openmeteo_event_precip_mm": 170.2,
        "nasa_event_precip_mm": 69.54,
        "nasa_peak_daily_precip_mm": 50.68,
        "nasa_peak_daily_precip_date": "20070606",
        "era5_max_mean_mm": [46.62, 40.26],
        "gpm_max_mean_mm": [84.43, 53.43],
        "chirps_max_mean_mm": [59.54, 45.48],
        "openmeteo_to_nasa_event_precip_ratio": 2.45,
        "local_precip_to_official_coastal_max_ratio": 0.28,
        "gpm_to_chirps_max_ratio": 1.42
      },
      "verdict": "The point total is wetter than the NASA daily total but far below the official coastal maximum."
    },
    {
      "row_id": "receptor_density_check",
      "formulae": [
        "buildings_per_1000_people = buildings / population * 1000"
      ],
      "values": {
        "population": 10576,
        "osm_total_elements": 1000,
        "osm_buildings": 973,
        "osm_roads": 20,
        "osm_schools": 4,
        "buildings_per_1000_people": 92.0
      },
      "verdict": "The receptor count gives a local density check, not a damage total."
    }
  ],
  "final_label": "consistent_local_land_stage_not_offshore_core",
  "failed_label": "offshore_core_equivalent_local_point"
}
```

# Key Computations

- Rainfall concentration: `152.6 / 170.2 = 0.90`; `170.2 / 170.2 = 1.00`; 12 hours reached at least 5 mm, and the peak hourly precipitation was 15.7 mm.
- Wind-pressure signature: `109.1 / 53.0 = 2.06`; the minimum pressure was 991.8 hPa after a 14.6 hPa fall, with 17 hours at or above 75 km/h gusts and 4 hours at or above 100 km/h.
- Official-local contrast: `127 kt * 1.852 = 235.2 km/h`; `235.2 / 109.1 = 2.16`; the official report also gives 920 hPa minimum pressure, 610 mm coastal rainfall maximum, and 100 km/h winds in Muscat.
- Precipitation product contrast: `170.2 / 69.54 = 2.45`; `170.2 / 610 = 0.28`; `84.43 / 59.54 = 1.42`.
- Receptor density: `973 / 10576 * 1000 = 92.0` buildings per 1000 people, with 20 roads and 4 schools in the local OpenStreetMap extract.

# Reasoning Path

The rainfall row first checks whether the local event total is spread over the full window or concentrated in a short wet phase. A 0.90 wettest-24-hour ratio and a 1.00 wettest-72-hour ratio show that the rainfall signal is sharply concentrated.

The wind-pressure row then tests whether the local point registered a cyclone passage signature. The gust-to-wind ratio of 2.06, the 14.6 hPa pressure fall, and the 4 hours above 100 km/h gusts support a strong local land-stage signal.

The official-local row prevents copying the offshore cyclone maximum into the local point. The official 235.2 km/h peak wind is 2.16 times the local 109.1 km/h gust, so the local record is severe but not offshore-core-equivalent.

The precipitation comparison row checks product consistency. The local point total is 2.45 times the NASA daily event total but only 0.28 of the official coastal maximum, while GPM and CHIRPS maxima differ by a 1.42 ratio. These values support a wet Muscat record without forcing all products to the same magnitude.

The receptor row adds a computed local density check. The correct answer should use the population and OSM counts as receptor context while keeping the final label tied to the calculated weather and comparison ratios.

# Computed Interpretation

The computed ledger supports `consistent_local_land_stage_not_offshore_core`: Muscat had concentrated rainfall, strong gust-pressure behavior, and measurable receptor density, but the local point values remain below the official offshore-core cyclone maximum.

# Scoring Rubric

- 3 points: Returns the requested JSON shape with the target family, all five row IDs, formulas, values, `final_label`, and `failed_label`. Partial: 1-2 points if the answer has most required rows but omits formulas, values, or one final label.
- 4 points: Correctly computes the rainfall concentration row: 170.2 mm event precipitation, 152.6 mm wettest 24-hour precipitation, ratios 0.90 and 1.00, 12 heavy-precipitation hours, and 15.7 mm peak hourly precipitation. Partial: up to 3 points for mostly correct values with minor rounding or one missing metric.
- 4 points: Correctly computes the wind-pressure row: 109.1 km/h peak gust, 53.0 km/h peak wind, ratio 2.06, 991.8 hPa minimum pressure, 14.6 hPa pressure fall, and 17/4 gust-threshold hours. Partial: up to 3 points for mostly correct values with one or two omissions.
- 3 points: Correctly separates the official cyclone values from the local point: 127 kt, 235.2 km/h, 920 hPa, 610 mm, 100 km/h Muscat wind, and official/local gust ratio 2.16. Partial: 1-2 points for correct official values with weak contrast logic.
- 3 points: Correctly compares precipitation products: Open-Meteo 170.2 mm, NASA 69.54 mm, NASA peak 50.68 mm on 20070606, ERA5 46.62/40.26, GPM 84.43/53.43, CHIRPS 59.54/45.48, ratios 2.45, 0.28, and 1.42. Partial: 1-2 points for a partial product comparison or missing ratios.
- 3 points: Correctly handles receptor density: population 10576, 1000 OSM elements, 973 buildings, 20 roads, 4 schools, and 92.0 buildings per 1000 people, without turning these counts into damage totals. Partial: 1-2 points for correct receptor counts without the density calculation or with an overextended damage claim.
