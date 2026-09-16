# ENSO-Linked Wet-Season Exposure Stress Model

Use only the local CSX-267 event package. Select package-relative evidence for every value you use.

Treat the package as a basin-scale 2023-2024 El Nino event with a regional early-wet-season West African/Gulf of Guinea data slice. Build a compact disaster-science model that connects the emerging ENSO signal to regional rainfall loading, exposed population, and operational monitoring confidence.

Compute the following:

1. Event and teleconnection timing:
   - event start and end dates;
   - ONI anomalies for AMJ, MJJ, and JJA 2023;
   - mean of those three early ONI anomalies;
   - maximum ONI anomaly from MJJ 2023 through MAM 2024;
   - number of overlapping three-month ONI steps from JJA 2023 to that maximum;
   - amplification from JJA 2023 ONI to the maximum;
   - SOI month count, mean, minimum, negative-month count, and negative-month fraction for June 2023 through May 2024.

2. Regional wet-load diagnostics from the three event-accumulated precipitation products:
   - common rainfall window and inclusive day count;
   - each product mean total;
   - mean of product means, mean daily intensity, product range, and coefficient of variation using the population standard deviation;
   - largest grid-cell/event maximum among the products;
   - localized-extreme ratio = largest product maximum / mean of product means.

3. Exposure and monitoring context:
   - population in millions;
   - approximate AOI area using the package polygon bounding box, with `width_km = 111.32 * lon_width * cos(mid_lat)` and `height_km = 110.574 * lat_height`;
   - population density;
   - whether the OSM exposure extraction has a data-gap remark and the number of OSM elements returned;
   - annual satellite embedding 1-minus-cosine mean and maximum.

4. Process model:

```text
rainfall_load_norm = clip(mean_product_precip_mm / 350, 0, 1)
localized_extreme_norm = clip(localized_extreme_ratio / 4, 0, 1)
teleconnection_norm =
  0.45 * clip(mean_AMJ_MJJ_JJA_2023_ONI / 1.0, 0, 1)
  + 0.35 * clip(peak_ONI_MJJ2023_to_MAM2024 / 2.0, 0, 1)
  + 0.20 * SOI_negative_fraction
population_load_norm = clip(population_millions / 5, 0, 1)
monitoring_gap_norm =
  0.60 * OSM_gap_flag
  + 0.40 * clip(satellite_1_minus_cosine_mean / 0.02, 0, 1)

regional_wet_exposure_stress =
  100 * (0.30 * rainfall_load_norm
       + 0.20 * localized_extreme_norm
       + 0.20 * teleconnection_norm
       + 0.20 * population_load_norm
       + 0.10 * monitoring_gap_norm)
```

5. Scenario test:
   - increase each precipitation-product mean by 15%;
   - increase the largest local rainfall maximum by 10%;
   - keep the teleconnection, population, and monitoring terms fixed;
   - recompute the stress score and the change from baseline.

Classify both baseline and scenario as `very_high` if score >= 85, `high` if >= 70, `elevated` if >= 55, otherwise `watch`. Classify product agreement as `strong` when precipitation coefficient of variation <= 0.05, `moderate` when <= 0.10, otherwise `weak`.

Return one JSON object with keys `source_paths`, `process_model`, `computed_metrics`, `scenario_analysis`, and `final_interpretation`. Round displayed scores, mm values, area, and density to 2 decimals; fractions and normalized components to 4 decimals; population in millions to 3 decimals. The final interpretation should be one concise sentence grounded in the computed mechanism chain.
