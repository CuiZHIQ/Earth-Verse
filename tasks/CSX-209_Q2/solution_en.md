# Final Answer

Correct answer:

```json
{
  "window": "2015-09-01/2015-10-31",
  "window_days": 61,
  "co_ratio": 13.0,
  "co_excess_ppb": 1200,
  "exposed_population": 410885,
  "sentinel_scene_total": 0,
  "precip_products_present": 2,
  "final_label": "co_plume_exposure_supported_no_burnscar_map"
}
```

# Key Computations

The locked event window runs from 2015-09-01 through 2015-10-31, which is 61 inclusive days. The NASA carbon-monoxide anchor gives ordinary concentrations of about 100 ppb and event values up to nearly 1,300 ppb, so `co_ratio = 1300 / 100 = 13.0` and `co_excess_ppb = 1200`.

The WorldPop population sum is 410,884.77942285844, rounded to 410,885 people. The Sentinel-2 dNBR summary has `pre_count = 0`, `post_count = 0`, and status `no_sufficient_scenes`, so `sentinel_scene_total = 0`. Both available GPM IMERG and CHIRPS event-accumulation summaries exist with `stats` for the package precipitation window, so `precip_products_present = 2`.

# Reasoning Path

Start from the locked time span and treat every derived value as a ledger entry tied to a named packaged source. The date calculation is inclusive because the prompt asks for the locked start and end dates as event days. The CO calculation uses the two NASA anchor values directly, with one decimal place only after forming the ratio.

Next, combine availability checks rather than interpreting missing burn-scar area. The dNBR scene total is zero because both pre and post counts are zero, and the dNBR status confirms that the Sentinel summary is not usable as a burn-scar map. The precipitation products are counted only by available-summary presence plus a `stats` object, not by rainfall magnitude or full-window clearing. The true-color pair is validated as openable imagery with positive dimensions and nonzero pixel variation rather than by file size alone.

# Computed Interpretation

All requested thresholds pass: the hazard family is `air_pollution_smoke_heat`, the CO ratio is 13.0, the rounded population value is positive, the Sentinel dNBR scene total is zero with `no_sufficient_scenes`, both true-color images validate as imagery, and both precipitation summaries contain `stats`. The computed ledger therefore returns `co_plume_exposure_supported_no_burnscar_map`.

The answer should remain a compact threshold ledger. It should not add health burden, burned-area, rainfall-causation, or mapped burn-severity details that are not computed by these fields.

# Scoring Rubric

Total: 20 points.

- Returned JSON shape (3 points): includes exactly the eight requested fields with valid JSON types and no extra fields. Partial credit: 1-2 points if the ledger is recoverable but has one minor field-name or formatting issue.
- Event window and source fields (3 points): reports `2015-09-01/2015-10-31`, 61 inclusive days, and uses the locked hazard family and source summaries. Partial credit: 1-2 points for the correct window with an off-by-one day count or incomplete source use.
- Carbon-monoxide arithmetic (4 points): extracts 100 ppb and 1,300 ppb correctly, computes `co_ratio = 13.0`, and computes `co_excess_ppb = 1200`. Partial credit: 2-3 points for correct inputs with one rounding or subtraction error; 1 point for recognizing the large CO increase without correct arithmetic.
- Exposure and data-availability values (4 points): rounds the WorldPop value to 410,885, computes zero Sentinel dNBR scenes, counts two available precipitation summaries with `stats`, and validates the true-color image pair as openable images with positive dimensions and pixel variation. Partial credit: award up to 1 point each for population, Sentinel scene total/status handling, precipitation count/window awareness, and true-color image validation.
- Gate logic and final label (4 points): applies every threshold exactly and returns `co_plume_exposure_supported_no_burnscar_map`. Partial credit: 2-3 points for the right label with one missed gate, or for correct gates with a noncanonical label.
- Compact interpretation discipline (2 points): keeps the answer to the requested ledger and avoids uncomputed health, burn-area, or rainfall-causation details. Partial credit: 1 point for a correct ledger with minor extra prose that does not change the result.
