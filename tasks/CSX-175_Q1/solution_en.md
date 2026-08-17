# Final Answer

The final answer is `severe_regional_smoke_burden`.

```json
{
  "aod_excess_load": 3.2,
  "station_exceedance_count": 2,
  "station_exceedance_fraction": 1.0,
  "grand_forks_clear_sky_multiplier": 46.0,
  "grand_forks_vs_goddard_mean_ratio": 2.3,
  "grand_forks_peak_to_mean_ratio": 1.3,
  "burned_area_baseline_ha": 47800,
  "diagnosis": "severe_regional_smoke_burden"
}
```

The AOD ledger is consistent with a severe regional smoke-burden episode, and the local dNBR and AlphaEarth change summaries cannot be converted into PM2.5 exposure hours.

# Key Computations

The NASA Earth Observatory anchor report gives the clear-sky upper bound as AOD less than 0.05, so the threshold is 0.05. The two station-day mean AOD values are about 1.0 at NASA Goddard/Greenbelt and 2.3 at Grand Forks. The Grand Forks peak value is close to 3.0 and is used only for the peak-to-mean ratio.

```text
aod_excess_load = (1.0 - 0.05) + (2.3 - 0.05) = 3.20
station_exceedance_count = 2
station_exceedance_fraction = 2 / 2 = 1.00
grand_forks_clear_sky_multiplier = 2.3 / 0.05 = 46.00
grand_forks_vs_goddard_mean_ratio = 2.3 / 1.0 = 2.30
grand_forks_peak_to_mean_ratio = 3.0 / 2.3 = 1.30
burned_area_baseline_ha = 478000 / 10 = 47800
```

Supporting surface-change context is consistent with fire and smoke interpretation but not with a PM2.5 exposure-duration calculation: Sentinel-2 dNBR mean is about 0.355 and AlphaEarth annual 1-minus-cosine change mean is about 0.045.

# Reasoning Path

Both station-day mean AOD values exceed the clear-sky threshold, and the exceedances are large: 0.95 above threshold at Goddard and 2.25 above threshold at Grand Forks. Their sum gives the requested AOD excess-load ledger value of 3.20.

The ratios reinforce the same diagnosis. Grand Forks mean AOD is 46 times the clear-sky threshold and 2.3 times the Goddard mean. The peak-to-mean ratio is computed as 3.0 divided by 2.3, not as another station-day exceedance.

The burned-area statement is a separate anomaly calculation: 478,000 hectares is 10 times the average area burned for that point in the season, so the implied baseline is 47,800 hectares. This supports the event context without replacing the AOD ledger.

# Computed Interpretation

The computed ledger points to regionally severe smoke loading in the reported station observations. The local satellite-change metrics can support fire or surface-change context, but they are not an exposure-hours series and should not be treated as PM2.5 duration, health burden, or city-outcome counts.

# Scoring Rubric

Total: 20 points.

- 4 points: returns the exact requested JSON fields with rounded numeric values and one concise consistency sentence. Partial credit: 2-3 points if the JSON is mostly complete but has one missing or misrounded field; 1 point for a recognizable ledger with several format errors.
- 5 points: extracts the core AOD inputs correctly: clear-sky threshold 0.05, Goddard mean AOD about 1.0, Grand Forks mean AOD 2.3, and Grand Forks nominal peak AOD 3.0. Partial credit: up to 3 points for recovering two or three of the four AOD inputs; subtract credit for using the Grand Forks peak as a station-day mean.
- 4 points: computes the smoke-load and exceedance ledger correctly: AOD excess load 3.20, station exceedance count 2, and exceedance fraction 1.00. Partial credit: 2-3 points if the exceedance count and fraction are correct but the excess load has a small arithmetic or rounding error.
- 3 points: computes the concentration ratios correctly: Grand Forks clear-sky multiplier 46.00, Grand Forks/Goddard mean ratio 2.30, and peak/mean ratio 1.30. Partial credit: 1 point for each correctly computed ratio with the intended numerator and denominator.
- 2 points: computes the burned-area baseline as 47,800 ha from 478,000 ha divided by the 10x anomaly factor. Partial credit: 1 point if the answer uses the correct inputs but gives an unrounded value, wrong unit label, or minor arithmetic slip.
- 2 points: interprets the AOD ledger as severe regional smoke burden while avoiding PM2.5-hour, clinical-outcome, or extra-data impact overclaims. Partial credit: 1 point if the answer gives the severe smoke-burden diagnosis but omits the satellite-to-PM2.5 limitation, or states the limitation without tying it to the AOD ledger.
