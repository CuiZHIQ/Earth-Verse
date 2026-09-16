# Final Answer

```json
{
  "total_heat_load_c_day": 11.8,
  "peak_day_heat_share": 0.466,
  "non_peak_heat_load_c_day": 6.3,
  "hot_run_days": 4,
  "warm_night_share_in_hot_run": 0.75,
  "wet_bulb_margin_to_24c": 2.0,
  "diagnosis": "persistence_recovery_dry_heat_signature"
}
```

The decomposition shows a distributed dry-heat persistence pattern: non-peak days contribute more heat load than the single hottest day, the hot run lasts four days, most hot-run nights stay warm, and the peak wet-bulb value remains below 24 C.

# Key Computations

- Daily maximum temperatures for 2021-06-25 through 2021-07-01 are 27.3, 30.1, 32.2, 34.0, 35.5, 26.7, and 22.3 C.
- Heat-load terms above 30 C are 0.0, 0.1, 2.2, 4.0, 5.5, 0.0, and 0.0 C-days, giving `total_heat_load_c_day = 11.8`.
- The peak-day heat-load term is 5.5 C-days on 2021-06-29, so `peak_day_heat_share = 5.5 / 11.8 = 0.466` and `non_peak_heat_load_c_day = 11.8 - 5.5 = 6.3`.
- The longest `Tmax >= 30 C` run is 2021-06-26 through 2021-06-29, or 4 days.
- Within that four-day run, Tmin reaches at least 16 C on 2021-06-27, 2021-06-28, and 2021-06-29, so `warm_night_share_in_hot_run = 3 / 4 = 0.75`.
- The maximum Stull wet-bulb temperature from the hourly series is about 22.0 C, so `wet_bulb_margin_to_24c = 24.0 - 22.0 = 2.0 C`.

# Reasoning Path

The calculation decomposes heat burden by time rather than relying on the maximum air temperature alone. A single-day spike would have most of the total heat load concentrated on the peak day. Here, the peak day contributes 46.6% of the cumulative exceedance, while the remaining hot days contribute 6.3 C-days, which is more than the peak-day contribution.

The hot sequence also has a recovery component. The four-day `Tmax >= 30 C` run contains three warm nights at or above 16 C, so the daily heat signal is paired with limited overnight cooling through most of the run. The wet-bulb margin stays positive relative to 24 C, which keeps the computed pattern in dry persistence and recovery space rather than a humidity-threshold crossing.

# Computed Interpretation

The computed signature is `persistence_recovery_dry_heat_signature`. It is supported by three linked numeric facts: heat load is distributed beyond the peak day, the hot run persists for four consecutive days, and warm nights occur on 75% of the hot-run dates while the maximum wet-bulb temperature remains about 2 C below 24 C.

# Scoring Rubric

Total: 20 points.

- 4 points: Correctly computes cumulative heat load as 11.8 C-days above 30 C from the daily Tmax series. Partial credit: 2-3 points for using the correct exceedance formula with one daily term or rounding error; 1 point for recognizing a 30 C exceedance load but summing the wrong window.
- 3 points: Correctly computes the peak-day heat share as about 0.466 and the non-peak heat load as about 6.3 C-days. Partial credit: 2 points for one correct split metric; 1 point for identifying the 2021-06-29 peak term but using incorrect division or subtraction.
- 3 points: Correctly identifies the longest hot run as 4 consecutive days with Tmax at or above 30 C. Partial credit: 2 points for the correct dates with an off-by-one count; 1 point for applying the 30 C threshold but including a non-hot day.
- 3 points: Correctly computes the hot-run warm-night share as 0.75 using Tmin at or above 16 C within the longest hot run. Partial credit: 2 points for the correct warm-night count with an incorrect denominator; 1 point for using Tmin and the 16 C threshold but applying it to the full event window.
- 3 points: Correctly computes the Stull wet-bulb maximum near 22.0 C and the margin to 24 C as about 2.0 C. Partial credit: 2 points for a wet-bulb maximum within tolerance but a wrong margin sign or rounding; 1 point for using hourly temperature and humidity but not the Stull approximation.
- 2 points: Gives the diagnosis `persistence_recovery_dry_heat_signature` and explains it using the numeric decomposition rather than a generic heat-wave statement. Partial credit: 1 point for the right label without tying it to the four rule checks, or for a correct qualitative conclusion with a slightly wrong label.
- 2 points: Returns the requested JSON fields with sensible rounding and adds one concise explanatory sentence. Partial credit: 1 point for all required values in a readable structure with minor formatting omissions or an overly long explanation.
