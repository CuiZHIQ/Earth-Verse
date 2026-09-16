# Wildfire-Smoke Threshold Ledger

During the 2023 Canadian wildfires and smoke episode affecting Canada and the downwind United States, a smoke-analysis team is checking whether a compact threshold ledger is internally consistent with a wildfire-smoke event family rather than a rainfall-centered signal.

Return a compact JSON object with these rounded values:

1. `grand_forks_clear_sky_ratio`: Grand Forks average AOD divided by the clear-sky AOD reference, rounded to 1 decimal.
2. `grand_forks_sun_reference_percent`: Grand Forks average AOD as a percent of the AOD level that would make the Sun difficult to see, rounded to 1 decimal percent.
3. `implied_average_burned_hectares`: implied average burned area for that time of year, in hectares, from the reported burned hectares and reported multiple, rounded to the nearest hectare.
4. `estimated_out_of_control_fires`: estimated Alberta fires out of control on May 16, from active fires and the reported fraction, rounded to the nearest whole fire.
5. `burn_signal_check`: dNBR mean and maximum, plus annual 1-minus-cosine embedding-change mean and maximum, each rounded to 3 decimals.
6. `exposure_counts`: rounded population, OSM highway elements, and total critical amenities counted as schools + hospitals + police + fire stations + shelters.
7. `precip_window_check`: spread between the largest and smallest accumulated-precipitation mean across the gridded May 1-June 15 summaries, in mm, rounded to 1 decimal, plus the inclusive length of the locked event window in days.
8. `computed_interpretation`: two or three sentences connecting the ledger to the event family.

Keep the interpretation tied to the numbers. Do not add casualty, medical-visit, property-loss, facility-outage, or continent-wide exposure claims.
