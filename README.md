<p align="center">
  <img src="assets/figures/earthverse-logo.png" alt="EarthVerse" width="680">
</p>

<h1 align="center">Benchmarking scientific agents across dynamic Earth systems and natural hazards</h1>

<p align="center">
  <strong>Zhiqing Cui</strong><sup>1,2</sup>, Xinxiang Yin<sup>3</sup>, Yihong Tang<sup>4</sup>, Xinglang Zhang<sup>5</sup>, Yuanzhe Hu<sup>6</sup>, Siru Zhong<sup>5</sup>, Weidong Tang<sup>7</sup>, Tao Yu<sup>8</sup>, Tianyue Zhou<sup>1</sup>,<br>
  Qu Ao<sup>1</sup>, Hanqing Wang<sup>5</sup>, Yuxuan Liang<sup>5</sup>, Weijia Li<sup>9</sup>, Ming Jin<sup>10</sup>, Shirui Pan<sup>10</sup>, Yuhao Kang<sup>11</sup>, Dingyi Zhuang<sup>1,&dagger;</sup>, Jinhua Zhao<sup>1</sup>
</p>

<p align="center"><sub>
  <sup>1</sup>Massachusetts Institute of Technology &nbsp; <sup>2</sup>University of Reading &nbsp; <sup>3</sup>The University of Hong Kong &nbsp; <sup>4</sup>McGill University &nbsp; <sup>5</sup>The Hong Kong University of Science and Technology (Guangzhou) &nbsp; <sup>6</sup>Georgia Institute of Technology<br>
  <sup>7</sup>National University of Singapore &nbsp; <sup>8</sup>University of Waterloo &nbsp; <sup>9</sup>Tsinghua University &nbsp; <sup>10</sup>Griffith University &nbsp; <sup>11</sup>The University of Texas at Austin &nbsp; <sup>&dagger;</sup>Corresponding author
</sub></p>

<p align="center">
  <a href="https://cuizhiq.github.io/EarthVerse/">Project page</a> ·
  <a href="assets/paper/EarthVerse.pdf">Paper</a> ·
  <a href="https://drive.google.com/drive/folders/1Fi4XkTTwwx9B45Egfh7DNt5rYKZHnt26">Data</a> ·
  <a href="https://huggingface.co/datasets/miracle10/EarthVerse">Hugging Face</a>
</p>

<p align="center">
  <img alt="Tasks" src="https://img.shields.io/badge/tasks-405-195c55">
  <img alt="Event packages" src="https://img.shields.io/badge/event_packages-199-3078a5">
  <img alt="Hazard families" src="https://img.shields.io/badge/hazard_families-19-bb6b37">
  <img alt="Evidence files" src="https://img.shields.io/badge/evidence_files-6%2C709-6c718c">
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-3b6f8f">
</p>

## Overview

EarthVerse tests whether a research agent can turn a local Earth-event archive into a checkable scientific answer. Its 405 tasks cover 199 documented disasters and extreme events across 19 hazard families. Agents must find relevant observations, run the required calculations, resolve disagreements between sources, and state what the evidence supports.

The public release includes the task prompts, evaluation harness, scoring prompts, reference answers, structured ground truth, scientific tools, and submission validator. It does not prescribe a tool order or require agents to reproduce a reference trajectory.

<p align="center">
  <img src="assets/figures/global-event-investigations.png" alt="Global event coverage and representative EarthVerse investigations" width="920">
</p>

## 📰 News

- **2026-08:** EarthVerse code and evaluation framework released.
- **2026-08:** Full event data released on [Hugging Face](https://huggingface.co/datasets/miracle10/EarthVerse) and [Google Drive](https://drive.google.com/drive/folders/1Fi4XkTTwwx9B45Egfh7DNt5rYKZHnt26).

## 🚀 Get started

Clone the evaluation code and install the base dependencies:

```bash
git clone https://github.com/CuiZHIQ/Earth-Verse.git
cd Earth-Verse
python -m pip install -r requirements.txt
```

Download `EarthVerse-data.zip` from [Google Drive](https://drive.google.com/drive/folders/1Fi4XkTTwwx9B45Egfh7DNt5rYKZHnt26) and extract it in the repository root. The archive already starts with `event_packages/`.

For a single download containing both code and data, use the Hugging Face mirror:

```bash
python -m pip install -U huggingface_hub
hf download miracle10/EarthVerse \
  --repo-type dataset \
  --local-dir Earth-Verse
cd Earth-Verse
python -m pip install -r requirements.txt
```

<details>
<summary>Repository structure</summary>

```text
Earth-Verse/
  README.md
  MANIFEST.json
  LICENSE.md
  requirements.txt
  requirements-tools.txt
  assets/
    figures/
    paper/EarthVerse.pdf
  configs/
    evaluation.json
    dimension_schema.json
  scripts/
    run_agent.py
    run_direct.py
    validate_submission.py
    judge.py
    report.py
  integrations/
    earthverse_mcp_server.py
  tools/
    earthverse_tools/
    meteorological_environments/
  task_sets/
    orig405.txt
    dimension_labels.csv
  tasks/<task_id>/
    question_en.md
    solution_en.md
    computed_gt.json
  event_packages/standard_event_packages/packages/<event_id>/
    README.md
    data/
    metadata/
```

</details>

Set the API credentials in your environment, then choose a model in `configs/evaluation.json`:

```bash
export OPENAI_API_KEY="..."
export OPENAI_BASE_URL="https://api.openai.com/v1"
```

```json
{
  "api_key_env": "OPENAI_API_KEY",
  "base_url_env": "OPENAI_BASE_URL",
  "models": [
    {
      "name": "your-model",
      "workers": 1
    }
  ]
}
```

## 📊 Run and evaluate

Run the agent harness on all 405 tasks:

```bash
python scripts/run_agent.py \
  --config configs/evaluation.json \
  --task-file task_sets/orig405.txt
```

The runner writes each model to `outputs/agent/<model>/`. Every task needs `answer.md` and `trajectory.json`; strict validation also requires `tool_trace.md` and `run_notes.md`.

```text
outputs/agent/<model>/<task_id>/
  answer.md
  trajectory.json
  tool_trace.md
  run_notes.md
```

Validate, judge, and build the final report:

```bash
python scripts/validate_submission.py \
  --submission-dir outputs/agent/your-model \
  --task-file task_sets/orig405.txt \
  --strict

python scripts/judge.py \
  --submission-dir outputs/agent/your-model \
  --out-dir reports/judge \
  --task-file task_sets/orig405.txt

python scripts/report.py \
  --judge-csv reports/judge/per_task_judge_scores.csv \
  --out-dir reports/final
```

EarthVerse reports two task-level scores from 0 to 100:

- `answer_correctness_score` measures correctness against the structured answer units.
- `llm_rubric_score` applies the task's 20-point rubric to the answer and trajectory.

```text
mean_score = (answer_correctness_score + llm_rubric_score) / 2
```

Strict Accuracy@95 is the share of tasks whose answer-unit score reaches 95. Tool calls, file reads, latency, tokens, and cost are diagnostics; they do not change the official mean score. Capability summaries use `task_sets/dimension_labels.csv`.

<p align="center">
  <img src="assets/figures/benchmark-coverage-wheel.png" alt="EarthVerse task capabilities and hazard-family coverage" width="600">
</p>

## 🧰 Tools and external agents

The base evaluator uses `requirements.txt`. Agents that need GIS, raster, PDF, meteorological, or MCP support can install the wider tool set:

```bash
python -m pip install -r requirements-tools.txt
python -m tools.earthverse_tools.cli --list
```

The MCP server at `integrations/earthverse_mcp_server.py` exposes the same package-scoped tools to external agent clients. Specialist environments live under `tools/meteorological_environments/environments/`.

During evaluation, a model may read only `question_en.md` and the matching event package. It must not read `solution_en.md` or `computed_gt.json`. The agent, meteorological environment, and judge prompts remain in the source for inspection; `MANIFEST.json` records their locations.

## License

See [LICENSE.md](LICENSE.md) for the terms covering the code, task annotations, and redistributed evidence.
