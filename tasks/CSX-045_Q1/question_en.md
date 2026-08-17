# Cold Surge Phase-Chain Inference

Using the supplied event package for the January 2016 East Asia and subtropical Asia cold wave, infer the most defensible event label from the data: a cold-only anomaly, a precipitation-dominated winter storm, or a compound cold-surge and winter-weather phase-chain.

Base the brief on the timing agreement among the hourly cold series, daily snowfall, wind gusts, local winter-weather observations, and the image records. The goal is a concise data-reasoning answer, not a hazard-management memo.

Return a compact JSON object with:

- `answer`: 2-3 sentences with the final diagnosis.
- `quantitative_anchors`: the cold minimum, longest below-zero run, event snowfall total, strongest gust, and local observatory low temperature.
- `reasoning_chain`: 3-5 short phrases that connect the cold surge, persistence, wind, and frozen or freezing precipitation.
- `image_use`: one sentence describing the image records' limited analytic role.
- `less_consistent_labels`: one sentence explaining why cold-only and precipitation-only labels fit less well.
