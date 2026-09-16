# Coupled-Rupture Numeric Ledger

Using the local CSX-235 data package for the 28 September 2018 Sulawesi earthquake and tsunami near Palu, compute a single score from package values. Find magnitude `M`, maximum MMI, ShakeMap PGA in `g`, hypocentral depth `D`, finite-fault length `L` and width `FW`, liquefaction and landslide population alert values, their aggregate hazard alert values, Palu wave height `H`, and mean precipitation from GPM, CHIRPS, and ERA5-Land. For shaking values, use the event-level MMI in the main USGS event GeoJSON and the first listed `shakemap` product's `maxpga` property as the primary PGA source.

Compute:

`S = mean(M/7.0, MMI/8.0, PGA_g/0.5, 30.0/D)`

`G = sqrt((liq_pop/landslide_pop) * (liq_hazard/landslide_hazard))`

`R = L/FW`

`T = 1 + H/D`

`P = 1 + mean(GPM_mean, CHIRPS_mean, ERA5_mean)/10`

`C = S * ln(G) * R * T / P`

Return a compact JSON object with `answer` equal to `C` rounded to three decimals, plus rounded `S`, `G`, `R`, `T`, and `P`.
