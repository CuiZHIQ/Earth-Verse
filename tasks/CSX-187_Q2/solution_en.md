# Final Answer

The correct answer is `ledger_complete`.

```json
{
  "grand_forks_clear_sky_ratio": 46.0,
  "grand_forks_sun_reference_percent": 76.7,
  "implied_average_burned_hectares": 47800,
  "estimated_out_of_control_fires": 22,
  "burn_signal_check": {
    "sentinel2_dnbr_mean": 0.355,
    "sentinel2_dnbr_max": 1.417,
    "alphaearth_mean": 0.045,
    "alphaearth_max": 0.792
  },
  "exposure_counts": {
    "population": 58882,
    "highway_elements": 947,
    "critical_amenities": 53
  },
  "precip_window_check": {
    "precip_mean_spread_mm": 57.4,
    "event_window_days": 153
  },
  "computed_interpretation": "The computed ledger supports a wildfire-smoke threshold classification: the Grand Forks AOD ratios are extreme relative to clear-sky and Sun-visibility references, and the burned-area, active-fire, dNBR, and embedding-change values provide a consistent source-side check. Rainfall remains a context variable in the ledger, not the controlling event-family signal."
}
```

# Key Computations

Grand Forks average aerosol optical depth is 2.3. The clear-sky reference is 0.05, so the clear-sky ratio is:

`2.3 / 0.05 = 46.0`

The Sun-visibility reference is AOD 3.0, so the Grand Forks percent of that reference is:

`2.3 / 3.0 * 100 = 76.7%`

The reported burned area is 478000 ha and the report states this was 10 times the average area burned for that time of year. The implied average is:

`478000 ha / 10 = 47800 ha`

The Alberta fire-status statement reports 87 wildland fires, with 25 percent out of control. The estimated count is:

`87 * 0.25 = 21.75`, rounded to `22` fires.

The burn-signal cross-check uses the local burn-index and embedding-change summaries: dNBR mean `0.355`, dNBR maximum `1.417`, annual 1-minus-cosine mean `0.045`, and annual 1-minus-cosine maximum `0.792`.

The compact local exposure slice contains rounded population `58882`, OSM highway elements `947`, and critical amenities `53`, computed as `38 schools + 5 hospitals + 4 police + 4 fire stations + 2 shelters`.

The precipitation means over May 1-June 15 are ERA5-Land `139.9480 mm`, GPM IMERG `82.5455 mm`, and CHIRPS `86.9229 mm`. The spread is:

`139.9480 - 82.5455 = 57.4 mm`

The locked event window is May 1 through September 30, 2023. Inclusive counting gives:

`153` days.

# Reasoning Path

The ledger is a threshold and consistency check rather than a broad event narrative. The AOD tests dominate the smoke diagnosis: an average AOD of 2.3 at Grand Forks is 46.0 times the clear-sky reference and 76.7 percent of the Sun-visibility reference. Those values are too large to treat rainfall as the main signal in this task.

The fire-source checks agree with the smoke threshold tests. A reported 478000 ha burned area implies a normal-time comparison value of only 47800 ha, and the May 16 Alberta count gives about 22 out-of-control fires. The dNBR and annual embedding-change statistics add an independent burn-signal cross-check, with high maximum values showing that the source-area signal is not just a rainfall or cloud artifact.

The exposure and precipitation numbers serve bounded ledger roles. The population, highway, and amenity counts describe the compact local slice requested by the task. The precipitation spread of 57.4 mm shows inter-product variability over the May 1-June 15 accumulated-precipitation summaries, but it does not overturn the AOD and active-fire source checks. The 153-day window fixes the temporal denominator for the locked event span.

# Computed Interpretation

The computed ledger supports a wildfire-smoke threshold classification: the Grand Forks AOD ratios are extreme relative to clear-sky and Sun-visibility references, and the burned-area, active-fire, dNBR, and embedding-change values provide a consistent source-side check. Rainfall remains a context variable in the ledger, not the controlling event-family signal.

# Scoring Rubric

Total: 20 points.

- AOD threshold calculations, 4 points: full credit for computing both Grand Forks ratios from 2.3, 0.05, and 3.0, rounding to 46.0 and 76.7%, and labeling the quantities. Partial credit: 2 points for one correct ratio, or 3 points for both formulas with one rounding or percent-unit error.
- Fire-source formula checks, 4 points: full credit for `478000 / 10 = 47800 ha` and `87 * 0.25 = 22 fires`, with units and rounding. Partial credit: 2 points for one correct fire-source value, or 3 points for both calculations with a minor rounding or unit omission.
- Burn-signal cross-check, 3 points: full credit for reporting dNBR mean 0.355 and max 1.417 plus annual 1-minus-cosine mean 0.045 and max 0.792 to three decimals. Partial credit: 1 to 2 points for two or three correct burn-signal values, or for correct values with inconsistent rounding.
- Exposure aggregation, 3 points: full credit for population 58882, highway elements 947, and critical amenities 53 from the five amenity classes. Partial credit: 1 point for one correct exposure value, or 2 points for two correct values or a correct amenity sum with one omitted class.
- Rainfall spread and event-window reconstruction, 3 points: full credit for the precipitation-mean spread of 57.4 mm and the inclusive event-window length of 153 days. Partial credit: 1 point for one correct value, or 2 points for both formulas with one arithmetic or inclusive-count error.
- Concise computed interpretation, 3 points: full credit for connecting the ledger to wildfire smoke in two or three sentences and keeping the consequence tied to the computed values. Partial credit: 1 to 2 points if the interpretation is directionally correct but misses either the rainfall cross-check role or the limit against casualty, medical, loss, outage, or continent-wide exposure claims.
