"""Offline regressions for judge arithmetic, retries, and resume."""
import copy
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import judge


def valid_result(task_id="T1"):
    return {
        "task_id": task_id,
        "scores": {"answer_correctness_score": 75, "llm_rubric_score": 75},
        "answer_units": {"total": 4, "correct": 3},
        "rubric_points": {
            "total": 20, "earned": 15,
            "criteria": [
                {"name": "a", "max_points": 10, "earned_points": 10},
                {"name": "b", "max_points": 10, "earned_points": 5},
            ],
        },
    }


class ConsistencyTests(unittest.TestCase):
    def test_consistent_scores_and_rounding(self):
        row = valid_result()
        self.assertEqual(judge.validate_judge_result("T1", row)["mean_score"], 75)
        row = valid_result()
        row["rubric_points"]["criteria"][1]["earned_points"] = 4.334
        row["rubric_points"]["earned"] = 14.334
        row["scores"]["llm_rubric_score"] = 71.67
        self.assertEqual(judge.validate_judge_result("T1", row)["scores"]["llm_rubric_score"], 71.67)

    def test_rejects_inconsistent_totals_and_percentages(self):
        for field, value in [("earned", 14), ("total", 21)]:
            with self.subTest(field=field):
                row = valid_result()
                row["rubric_points"][field] = value
                with self.assertRaises(ValueError):
                    judge.validate_judge_result("T1", row)
        row = valid_result()
        row["scores"]["llm_rubric_score"] = 80
        with self.assertRaises(ValueError):
            judge.validate_judge_result("T1", row)
        row = valid_result("another_task")
        with self.assertRaises(ValueError):
            judge.validate_judge_result("T1", row)

    def test_rejects_invalid_raw_values_before_clamping(self):
        for value in [float("nan"), float("inf"), -1, 21, True, "invalid"]:
            with self.subTest(earned=value):
                row = valid_result()
                row["rubric_points"]["earned"] = value
                with self.assertRaises(ValueError):
                    judge.validate_judge_result("T1", row)
        for field, value in [("max_points", 11), ("max_points", -1),
                             ("earned_points", 11), ("earned_points", -1),
                             ("earned_points", float("inf"))]:
            with self.subTest(field=field, value=value):
                row = valid_result()
                row["rubric_points"]["criteria"][0][field] = value
                with self.assertRaises(ValueError):
                    judge.validate_judge_result("T1", row)

    def test_resume_keeps_only_valid_rows_and_solver_zeros(self):
        good = judge.validate_judge_result("T1", valid_result())
        original = copy.deepcopy(good)
        bad = valid_result("T2")
        bad["rubric_points"]["earned"] = 14
        missing = valid_result("T3")
        missing.pop("answer_units")
        zero = judge.solver_error_zero_result("T4", {})
        error = judge.judge_error_result("T5", ValueError("mock error"))
        self.assertEqual(judge.completed_result_ids([good, bad, missing, zero, error]), {"T1", "T4"})
        self.assertEqual(judge.completed_result_ids([good], {"T1"}), set())
        self.assertEqual(good, original)

    def test_arithmetic_validation_is_inside_retry_loop(self):
        bad = valid_result()
        bad["rubric_points"]["earned"] = 14
        messages = [{"role": "user", "content": "Original assessment request"}]
        with patch.object(judge, "collect_metadata", return_value={"run_status": "ok"}), \
             patch.object(judge, "build_messages", return_value=messages), \
             patch.object(judge.time, "sleep"), \
             patch.object(judge, "call_openai_compatible_raw", side_effect=[bad, valid_result()]) as api:
            result = judge.judge_one(Path("T1"), Path("."), "mock", "unused", "unused", 1, True, 2)
        self.assertEqual(api.call_count, 2)
        self.assertEqual(result["judge_call_count"], 2)
        self.assertEqual(result["mean_score"], 75)
        self.assertEqual(len(result["judge_failed_attempts"]), 1)
        self.assertEqual(result["judge_failed_attempts"][0]["response"], bad)
        self.assertEqual(api.call_args_list[0].args[0], api.call_args_list[1].args[0])

    def test_invalid_shape_exhausts_retries_and_preserves_response(self):
        invalid = valid_result()
        invalid.pop("answer_units")
        with patch.object(judge, "collect_metadata", return_value={"run_status": "ok"}), \
             patch.object(judge, "build_messages", return_value=[]), \
             patch.object(judge.time, "sleep"), \
             patch.object(judge, "call_openai_compatible_raw", return_value=invalid) as api:
            result = judge.judge_one(Path("T1"), Path("."), "mock", "unused", "unused", 1, True, 2)
        self.assertEqual(api.call_count, 3)
        self.assertEqual(result["verdict"], "judge_error")
        self.assertEqual(result["judge_call_count"], 3)
        self.assertEqual(len(result["judge_failed_attempts"]), 3)
        self.assertEqual(result["judge_failed_attempts"][-1]["response"], invalid)

    def test_resume_rejudges_conflict_without_changing_good_row(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            tasks, out = root / "tasks", root / "judge"
            out.mkdir()
            good = judge.validate_judge_result("T1", valid_result())
            bad = copy.deepcopy(good)
            bad["task_id"] = "T2"
            bad["rubric_points"]["earned"] = 14
            for task_id in ["T1", "T2"]:
                (tasks / task_id).mkdir(parents=True)
                (tasks / task_id / "computed_gt.json").write_text("{}", encoding="utf-8")
            (out / "per_task_judge_scores.jsonl").write_text(
                "\n".join(json.dumps(row) for row in [good, bad]), encoding="utf-8")
            argv = ["judge.py", "--task-dir", str(tasks), "--out-dir", str(out), "--resume"]
            with patch.object(sys, "argv", argv), patch.dict(os.environ, {"OPENAI_API_KEY": "mock"}), \
                 patch.object(judge, "collect_metadata", return_value={"run_status": "ok"}), \
                 patch.object(judge, "build_messages", return_value=[]), \
                 patch.object(judge, "call_openai_compatible_raw", return_value=valid_result("T2")) as api, \
                 redirect_stdout(io.StringIO()):
                judge.main()
            saved = judge.load_existing_results(out / "per_task_judge_scores.jsonl")
            self.assertEqual(api.call_count, 1)
            self.assertEqual(len(saved), 2)
            self.assertEqual(next(row for row in saved if row["task_id"] == "T1"), good)
            self.assertEqual(judge.completed_result_ids(saved), {"T1", "T2"})


if __name__ == "__main__":
    unittest.main()
