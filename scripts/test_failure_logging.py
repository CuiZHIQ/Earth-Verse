import http.client
import io
import json
import tempfile
import urllib.error
import unittest
from pathlib import Path
from unittest.mock import patch

import run_agent


class FailureLoggingTests(unittest.TestCase):
    def test_forced_finalization_cannot_promote_a_tool_request_to_an_answer(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            task = root / 'tasks/CSX-001_Q1'
            package = root / 'packages/CSX-001'
            task.mkdir(parents=True)
            package.mkdir(parents=True)
            request = json.dumps({'action': 'tool_call', 'tool': 'read_text_file',
                                  'args': {'path': 'evidence.txt'}})
            with patch.object(run_agent, 'ROOT', root), \
                 patch.object(run_agent, 'build_initial_messages', return_value=[{'role': 'user', 'content': 'question'}]), \
                 patch.object(run_agent, 'call_model_with_retries', return_value=({'usage': {'total_tokens': 7}}, request)), \
                 patch.object(run_agent, 'run_tool', return_value={'ok': True, 'output': 'evidence'}):
                run_agent.solve_one(task, 'mock', root / 'packages', root / 'out',
                                    {'max_agent_turns': 1, 'max_research_seconds': 0,
                                     'max_task_wall_seconds': 0}, 'mock', 'unused', False)
            run_dir = root / 'out/mock/CSX-001_Q1'
            trajectory = json.loads((run_dir / 'trajectory.json').read_text())
            conversation = json.loads((run_dir / 'raw_conversation.json').read_text())
            self.assertEqual(trajectory['final_answer']['status'], 'budget_exhausted')
            self.assertIsNone(trajectory['final_answer']['answer'])
            self.assertEqual(trajectory['termination_reason'], 'round_limit_fallback')
            errors = [entry for entry in conversation['transcript'] if 'finalization_error' in entry]
            self.assertEqual(errors[0]['raw_content'], request)
            self.assertIn('tool request', errors[0]['finalization_error'])

    def test_http_failure_preserves_provider_error_and_redacts_key(self):
        body = json.dumps({'error': {'code': 'InvalidEndpointOrModel.NotFound',
                                    'message': 'Unavailable model; secret-test-key'},
                           'request_id': 'request-123'}).encode()
        error = urllib.error.HTTPError('https://example.invalid/chat/completions',
                                       404, 'Not Found', {}, io.BytesIO(body))
        with patch.object(run_agent.urllib.request, 'urlopen', side_effect=error), \
             self.assertRaises(urllib.error.HTTPError) as caught:
            run_agent.call_chat_completion([{'role': 'user', 'content': 'test'}],
                                            'test-model', 'https://example.invalid',
                                            'secret-test-key', 1, None, None, False)
        self.assertEqual(caught.exception.code, 404)
        self.assertIn('InvalidEndpointOrModel.NotFound', str(caught.exception))
        self.assertIn('request-123', str(caught.exception))
        self.assertNotIn('secret-test-key', str(caught.exception))
        self.assertIn('[REDACTED]', str(caught.exception))

    def test_unreadable_http_body_keeps_original_error(self):
        for cause in (OSError('body lost'), http.client.IncompleteRead(b'partial')):
            with self.subTest(read_error=type(cause).__name__):
                error = urllib.error.HTTPError('https://example.invalid/chat/completions',
                                               503, 'Service Unavailable', {}, None)
                with patch.object(error, 'read', side_effect=cause), \
                     patch.object(run_agent.urllib.request, 'urlopen', side_effect=error), \
                     self.assertRaises(urllib.error.HTTPError) as caught:
                    run_agent.call_chat_completion([{'role': 'user', 'content': 'test'}],
                                                    'test-model', 'https://example.invalid',
                                                    'test-key', 1, None, None, False)
                self.assertIs(caught.exception, error)
                self.assertEqual(caught.exception.code, 503)

    def test_protocol_failure_preserves_full_response_tools_usage_and_time(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            task = root / 'tasks/CSX-001_Q1'
            package = root / 'packages/CSX-001'
            task.mkdir(parents=True)
            package.mkdir(parents=True)
            invalid = '{"broken":' + 'x' * 6000
            replies = [({'usage': {'total_tokens': 12}}, json.dumps({
                'action': 'tool_call', 'tool': 'read_text_file', 'args': {'path': 'x'}})),
                ({'usage': {'total_tokens': 7}}, invalid)]
            with patch.object(run_agent, 'ROOT', root), \
                 patch.object(run_agent, 'build_initial_messages', return_value=[{'role': 'user', 'content': 'question'}]), \
                 patch.object(run_agent, 'call_model_with_retries', side_effect=replies), \
                 patch.object(run_agent, 'run_tool', return_value={'ok': True, 'output': 'evidence'}), \
                 patch.object(run_agent.time, 'perf_counter', side_effect=[100., 100., 102.5]):
                result = run_agent.solve_one(task, 'mock', root / 'packages', root / 'out',
                                            {'max_agent_turns': 5, 'max_parse_repairs': 0}, 'mock', 'unused', False)
            self.assertEqual(result['status'], 'error')
            self.assertEqual(result['latency_s'], 2.5)
            path = root / 'out/mock/CSX-001_Q1'
            trajectory = json.loads((path / 'trajectory.json').read_text())
            conversation = json.loads((path / 'raw_conversation.json').read_text())
            self.assertEqual(len(trajectory['tool_calls']), 1)
            self.assertEqual(sum(x['total_tokens'] for x in trajectory['raw_usage']), 19)
            self.assertEqual(conversation['transcript'][-1]['raw_content'], invalid)
            self.assertIn('ValueError', (path / 'failure_details.json').read_text())



if __name__ == '__main__':
    unittest.main()
