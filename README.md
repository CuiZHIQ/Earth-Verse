<p align="center">
  <img src="assets/figures/earthverse-logo.png" alt="EarthVerse" width="680">
</p>

<h1 align="center">Benchmarking scientific agents across dynamic Earth systems and natural hazards</h1>

<p align="center">
  <strong>Zhiqing Cui</strong>, Xinxiang Yin, Yihong Tang, Xinglang Zhang, Yuanzhe Hu, Siru Zhong, Weidong Tang, Tao Yu, Tianyue Zhou,<br>
  Qu Ao, Hanqing Wang, Yuxuan Liang, Weijia Li, Ming Jin, Shirui Pan, Yuhao Kang, Dingyi Zhuang, Jinhua Zhao
</p>

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

EarthVerse measures whether a research agent can carry an Earth-system investigation from evidence selection to a checkable scientific account. The benchmark contains 405 tasks grounded in 199 documented disasters and extreme events across 19 hazard families. A task begins with a local event archive, not a selected passage or figure. The agent must inspect the available material, choose compatible observations, perform the necessary calculations, reconcile source differences, and explain what the evidence supports.

The public evaluation protocol includes task prompts, agent instructions, scoring prompts, reference solutions, structured ground truth, tool interfaces, and submission validation. EarthVerse does not require a fixed tool order or a reference trajectory. Different research paths are valid when they establish the required quantities and preserve support for the final claims.

<p align="center">
  <img src="assets/figures/global-event-investigations.png" alt="Global event coverage and representative EarthVerse investigations" width="920">
</p>

## Release layout

The three release channels have distinct roles:

| Channel | Contents | Use |
| --- | --- | --- |
| [GitHub](https://github.com/CuiZHIQ/Earth-Verse) | Evaluation code, task prompts, reference materials, tools, configuration, and paper | Clone the harness and inspect the protocol |
| [Google Drive](https://drive.google.com/drive/folders/1Fi4XkTTwwx9B45Egfh7DNt5rYKZHnt26) | The 199 event packages in one data archive | Extract the data directly into the GitHub repository root |
| [Hugging Face](https://huggingface.co/datasets/miracle10/EarthVerse) | The GitHub release plus all event packages | Download one complete, ready-to-run mirror |

None of the public channels contains model runs, construction scripts, experimental notes, task-review records, caches, or private trajectories.

## Repository structure

```text
Earth-Verse/
  README.md
  MANIFEST.json
  LICENSE.md
  CITATION.cff
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
  tasks/
    <task_id>/
      question_en.md
      solution_en.md
      computed_gt.json
  event_packages/                  # added from Google Drive
    standard_event_packages/
      packages/<event_id>/
        README.md
        data/
        metadata/
```

## Data preparation

Clone the repository and install the base dependencies:

```bash
git clone https://github.com/CuiZHIQ/Earth-Verse.git
cd Earth-Verse
python -m pip install -r requirements.txt
```

Download `EarthVerse-data.zip` from [Google Drive](https://drive.google.com/drive/folders/1Fi4XkTTwwx9B45Egfh7DNt5rYKZHnt26) and extract it in the repository root. The archive starts with `event_packages/`, so no file moving or joining step is needed.

```text
Earth-Verse/
  event_packages/
    standard_event_packages/
      packages/<event_id>/
```

As an alternative, the Hugging Face repository already combines the code and data:

```bash
python -m pip install -U huggingface_hub
hf download miracle10/EarthVerse \
  --repo-type dataset \
  --local-dir Earth-Verse
cd Earth-Verse
python -m pip install -r requirements.txt
```

## Configuration

Set credentials for an OpenAI-compatible endpoint:

```bash
export OPENAI_API_KEY="..."
export OPENAI_BASE_URL="https://api.openai.com/v1"
```

Edit `configs/evaluation.json` to select the model and change runner limits. API keys are read from environment variables and should not be written into the configuration file.

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

## Running the evaluation

Run the common agent harness on the official 405-task list:

```bash
python scripts/run_agent.py \
  --config configs/evaluation.json \
  --task-file task_sets/orig405.txt
```

Each task submission must contain the final answer and the execution trajectory:

```text
submission/
  <task_id>/
    answer.md              # required
    trajectory.json        # required
    tool_trace.md          # optional; required by strict validation
    run_notes.md           # optional; required by strict validation
```

Validate and score the run with the public evaluator:

```bash
python scripts/validate_submission.py \
  --submission-dir submission \
  --task-file task_sets/orig405.txt \
  --strict

python scripts/judge.py \
  --submission-dir submission \
  --out-dir reports/judge \
  --task-file task_sets/orig405.txt

python scripts/report.py \
  --judge-csv reports/judge/per_task_judge_scores.csv \
  --out-dir reports/final
```

## Evaluation protocol

EarthVerse reports two official task-level scores on a 0-100 scale:

- `answer_correctness_score` checks the final response against structured answer units.
- `llm_rubric_score` checks evidence use, calculations, reasoning, and task-specific requirements in the answer and trajectory.

```text
mean_score = (answer_correctness_score + llm_rubric_score) / 2
```

Strict Accuracy@95 counts a task as correct when its answer-unit score reaches 95. Capability summaries use `task_sets/dimension_labels.csv`. Tool calls, file reads, tokens, latency, and cost are reported as diagnostics and do not change the official mean score.

<p align="center">
  <img src="assets/figures/task-evidence-trajectory.png" alt="EarthVerse task evidence and research trajectory" width="820">
</p>

## Scientific tools and external agents

The base evaluator uses `requirements.txt`. Install the wider file, GIS, raster, PDF, meteorological, and MCP dependencies when an agent needs the full research environment:

```bash
python -m pip install -r requirements-tools.txt
python -m tools.earthverse_tools.cli --list
```

Specialist environments live in `tools/meteorological_environments/environments/`. The MCP server in `integrations/earthverse_mcp_server.py` exposes the same package-scoped inspection and calculation tools to external agent clients.

## Prompt and answer boundary

During evaluation, the model may read `question_en.md` and the matching event package. It must not read `solution_en.md` or `computed_gt.json`.

The remaining protocol prompts stay in the source so the harness can be inspected:

- Agent prompt: `scripts/run_agent.py::build_initial_messages`
- Meteorological environment prompt: `tools/meteorological_environments/agent_entry.py::_tool_instructions`
- Judge prompt: `scripts/judge.py::build_messages`

`MANIFEST.json` records the release structure, prompt locations, scoring fields, and download address.

## Citation

```bibtex
@misc{cui2026earthverse,
  title        = {EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards},
  author       = {Cui, Zhiqing and Yin, Xinxiang and Tang, Yihong and Zhang, Xinglang and Hu, Yuanzhe and Zhong, Siru and Tang, Weidong and Yu, Tao and Zhou, Tianyue and Ao, Qu and Wang, Hanqing and Liang, Yuxuan and Li, Weijia and Jin, Ming and Pan, Shirui and Kang, Yuhao and Zhuang, Dingyi and Zhao, Jinhua},
  year         = {2026},
  url          = {https://cuizhiq.github.io/EarthVerse/}
}
```

Use `CITATION.cff` for citation-manager metadata. `LICENSE.md` describes the terms for the code, task annotations, and redistributed evidence.
