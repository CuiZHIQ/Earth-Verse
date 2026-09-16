# Correct Answer

```json
{"answer":22.445,"S":1.356,"G":9.937,"R":7.184,"T":1.35,"P":1.345}
```

# Calculation

The package values are `M=7.5`, `MMI=8.367`, `PGA_g=0.903`, `D=20.0 km`, `L=264.0 km`, `FW=36.75 km`, `liq_pop=140000`, `landslide_pop=5800`, `liq_hazard=450.0`, `landslide_hazard=110.0`, `H=7 m`, and precipitation means `4.425479`, `3.668446`, and `2.262971 mm`. The MMI is taken from the event GeoJSON top-level `properties.mmi`, and the PGA is taken from the first listed `products.shakemap[0].properties.maxpga` value to avoid ambiguity across multiple ShakeMap products.

`S = mean(7.5/7.0, 8.367/8.0, 0.903/0.5, 30.0/20.0) = 1.355826`

`G = sqrt((140000/5800) * (450.0/110.0)) = 9.937106`

`R = 264.0/36.75 = 7.183673`

`T = 1 + 7/20.0 = 1.35`

`P = 1 + mean(4.425479, 3.668446, 2.262971)/10 = 1.345230`

`C = 1.355826 * ln(9.937106) * 7.183673 * 1.35 / 1.345230 = 22.444598`, so the rounded answer is `22.445`.

# Scoring Rubric

Total: 20 points.

- 4 points: Retrieves the required local numeric anchors with correct units, uses event-level `properties.mmi`, uses the first listed `products.shakemap[0].properties.maxpga` as the primary ShakeMap PGA source, and converts PGA as a value in `g`.
- 5 points: Computes `S`, `G`, `R`, `T`, and `P` from the stated formulas with correct arithmetic.
- 4 points: Computes the final natural-log score `C` and rounds the reported value to three decimals.
- 4 points: Shows enough intermediate ratios, especially `140000/5800`, `450.0/110.0`, `264.0/36.75`, and the three-mean precipitation term, to make the ledger auditable.
- 3 points: Returns the requested compact JSON shape and keeps numeric precision consistent across the fields.
