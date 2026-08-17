# Peat-Smoke Haze Severity Ledger

During the 2015 Southeast Asia haze from Indonesian fires, an air-quality science team is checking whether the event record supports a peat-smoke severity ledger rather than a burn-scar or rainfall-only summary.

Compute a compact JSON ledger with exactly these eight fields:

- `psi_ratio_min`: reported PSI floor divided by the hazardous PSI threshold, rounded to 3 decimals.
- `surface_co_ratio`: near-surface carbon monoxide peak divided by typical near-surface carbon monoxide, rounded to 3 decimals.
- `aerosol_factor`: particle increase factor reported for Palangkaraya.
- `max_vertical_signal_km`: maximum reported vertical smoke or carbon-monoxide signal height in kilometers.
- `dry_day_shares`: object with `open_meteo` and `nasa_power`, each equal to days below 1 mm precipitation divided by days in that local daily-weather window, rounded to 3 decimals.
- `dnbr_pre_post_counts`: two-element array `[pre_count, post_count]`.
- `candidate_scores`: object with `peat_smoke`, `rainfall_only`, and `burn_scar` integer scores. Give 1 peat-smoke point for each satisfied test: both dry-day shares are at least 0.30; peat carbon-monoxide and methane multipliers are at least 3 and 10; `psi_ratio_min` is at least 5; `surface_co_ratio` is at least 10; `aerosol_factor` is at least 5; `max_vertical_signal_km` is at least 5. Give rainfall-only 1 point only for the dry-day test, and burn-scar 1 point only if both dNBR scene counts are positive.
- `final_label`: `peat_smoke_haze_pass` if the peat-smoke score is 6 and the other two scores are lower; otherwise `ledger_not_confirmed`.

Return only the JSON object, with no prose outside it.
