# Kedarnath Rainfall-Concentration Ledger

In mid-June 2013, extreme monsoon rainfall struck Kedarnath and the upper Mandakini valley in Uttarakhand, India. A technical review team is testing whether the event record supports a concentrated mountain-rainfall exposure diagnosis rather than a diffuse regional-flood label.

Compute a compact numeric ledger for the June 15-18, 2013 window. Use the point rainfall series, the two gridded accumulated-rainfall summaries, and the package mapped-context transport and service-feature counts to test the following rule:

- point rainfall total must be at least 300 mm;
- the June 16-17 rainfall share of the four-day point total must be at least 0.85;
- the smaller gridded rainfall maximum divided by the larger gridded rainfall maximum must be at least 0.98;
- bridge elements per 100 highway elements must be at least 15;
- hospitals plus shelters plus tourism hotels must be at least 40.

Return only compact JSON with these fields:

`event_window`, `point_total_mm`, `peak_2day_share`, `grid_max_mm`, `grid_pair_ratio`, `bridge_per_100_highway`, `service_node_count`, and `final_state`.

Use `passes_concentrated_mountain_exposure_test` only if all five tests pass; otherwise use `does_not_pass`.
