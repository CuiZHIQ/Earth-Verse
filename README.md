# EarthVerse

This anonymous review release contains the evaluation code, scientific tools, and all 405 tasks with reference answers and structured ground truth.

## Example evidence

We include 10 complete event packages, covering 22 tasks, so reviewers can try the benchmark with the evidence at hand. The full collection is about 969 MB uncompressed; we include this subset to keep the repository download manageable. These examples contain about 80 MB of evidence and metadata. The remaining 189 event packages are not included.

The packages retain their evidence and source records. We removed access credentials embedded in saved third-party web pages and updated the affected file checksums. The examples cover Pakistan's 2022 floods, the 2013 Uttarakhand floods, Storm Ciaran, Canadian wildfire smoke over the northeastern United States, the Atami debris flow, the Turkiye-Syria earthquakes, China's 2022 heat wave and drought, the Hunga Tonga eruption, the Mendenhall glacier outburst flood, and global coral bleaching.

Evidence is under `event_packages/standard_event_packages/packages/<event_id>/`. The matching task IDs are in `task_sets/example10.txt`.

## Setup

Use Python 3.10 or newer. From the repository directory:

```bash
python -m pip install -r requirements.txt
```

Set `OPENAI_API_KEY` and, if needed, `OPENAI_BASE_URL`. Set the model name in `configs/evaluation.json`.

## Run the examples

```bash
python scripts/run_agent.py --config configs/evaluation.json --task-file task_sets/example10.txt
python scripts/validate_submission.py --submission-dir outputs/agent/your-model --task-file task_sets/example10.txt --strict
python scripts/judge.py --submission-dir outputs/agent/your-model --out-dir reports/judge --task-file task_sets/example10.txt
python scripts/report.py --judge-csv reports/judge/per_task_judge_scores.csv --out-dir reports/final
```

Replace `your-model` with the configured model name. Each task produces `answer.md`, `trajectory.json`, `tool_trace.md`, and `run_notes.md`.

To evaluate all 405 tasks, first add the remaining event packages, then use `task_sets/orig405.txt` in place of `task_sets/example10.txt`. The example subset is for inspecting and trying the benchmark; its scores do not reproduce the full benchmark results in the paper.

The main score is the mean of answer correctness and process rubric scores. Strict Accuracy@95 measures the share of tasks with answer-unit scores of at least 95. Runtime and cost are reported separately.

## Files

- `event_packages/`: evidence and source metadata for the 10 examples.
- `tasks/`: all 405 questions, reference solutions, and structured ground truth.
- `task_sets/`: task lists and capability labels.
- `configs/`: evaluation settings and dimension schema.
- `scripts/`: agent and direct runners, validation, judging, and reporting.
- `tools/`: scientific tools and specialist environments.
- `integrations/earthverse_mcp_server.py`: tool access for external agents.

Agents may read only the question and its event package. Reference solutions and ground truth are reserved for evaluation. `MANIFEST.json` lists the prompt locations and entry points.

For GIS, raster, PDF, meteorological, or MCP support:

```bash
python -m pip install -r requirements-tools.txt
python -m tools.earthverse_tools.cli --list
```

See `LICENSE.md` and each package's source records for the terms governing software, annotations, and third-party evidence.
