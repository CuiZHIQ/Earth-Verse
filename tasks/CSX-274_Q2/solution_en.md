# Final Answer

Canonical answer: `JAS_1997_to_JFM_1998_7_windows_9_months`.

```json
{
  "qualifying_window_count": 7,
  "first_window": "JAS_1997",
  "last_window": "JFM_1998",
  "calendar_span": "1997-07_to_1998-03",
  "calendar_span_months": 9,
  "tight_boundary_windows": ["JAS_1997", "OND_1997"],
  "near_miss_windows": ["JJA_1997", "FMA_1998"],
  "diagnosis": "The double-threshold ledger reconstructs a mature coupled El Nino interval from July 1997 through March 1998."
}
```

# Key Computations

The calculation uses these local package files:

- `data/physical_hazard/physical_hazard_006_NOAA_CPC_ONI_ASCII.txt`
- `data/physical_hazard/physical_hazard_008_NOAA_PSL_SOI_data.data`

For each three-month window from MJJ_1997 through MAM_1998, `compute_gt.py` reads the ONI anomaly for the named season and averages the three monthly SOI values over the same calendar months. A window passes only when:

```text
ONI anomaly >= 1.5 C
mean SOI <= -2.0
```

The qualifying windows are:

```text
JAS_1997, ASO_1997, SON_1997, OND_1997, NDJ_1997, DJF_1998, JFM_1998
```

This is one continuous run. JAS_1997 begins in July 1997 and JFM_1998 ends in March 1998, so the inclusive calendar span is `1997-07_to_1998-03`, or 9 months.

Boundary checks:

- `JAS_1997`: ONI = 1.90 C and mean SOI = -2.0000, so it exactly meets the SOI condition.
- `OND_1997`: ONI = 2.40 C and mean SOI = -2.0000, so it also exactly meets the SOI condition.

Nearest single-condition misses:

- `JJA_1997`: ONI = 1.60 C passes, but mean SOI = -1.9667 misses the SOI condition by about 0.033.
- `FMA_1998`: mean SOI = -3.2667 passes, but ONI = 1.44 C misses the ocean condition by 0.06 C.

The result is a threshold diagnostic for the mature coupled ENSO interval. It should not be treated as an exact local loss, rainfall, flood-depth, or damage measurement.

# Scoring Rubric

Total: 20 points.

- Final threshold reconstruction (4 points): Reports JAS_1997 through JFM_1998, with 7 qualifying windows and a 9-month calendar span. Partial credit: 2-3 points for the right interval with one count or span error; 1 point for identifying only a winter-centered coupled interval.
- ONI extraction (3 points): Uses the CPC ONI anomaly for each three-month season from MJJ_1997 through MAM_1998 and applies the >= 1.5 C condition correctly. Partial credit: 1-2 points for using the right file and values but making a minor threshold or season-label error.
- SOI averaging (4 points): Averages the three monthly SOI values for each matching calendar window and applies the <= -2.0 condition before rounding. Partial credit: 1-3 points for correct SOI extraction with a small averaging, sign, or boundary-condition error.
- Boundary and near-miss diagnostics (3 points): Identifies JAS_1997 and OND_1997 as exact SOI-boundary passes, plus JJA_1997 and FMA_1998 as the nearest single-condition misses. Partial credit: 1-2 points for naming only the boundary passes or only the near misses.
- Calendar continuity (2 points): Converts the first and last qualifying seasons to the inclusive July 1997 through March 1998 calendar span. Partial credit: 1 point for giving the right endpoints but not the inclusive month count.
- Physical interpretation and limits (2 points): Explains that the ledger diagnoses a mature coupled El Nino interval relevant to winter storm and flood context without turning it into exact local impact totals. Partial credit: 1 point for a correct ENSO interpretation that lacks the caution about exact local impacts.
- Structured concise response (2 points): Returns compact JSON-style fields with the requested count, endpoints, span, boundary windows, near misses, and diagnosis. Partial credit: 1 point for recoverable content with minor formatting or concision problems.
