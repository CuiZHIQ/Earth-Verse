import json
import unittest
from run_agent import extract_json_object, normalize_agent_payload


class ProtocolTests(unittest.TestCase):
    def test_valid_envelopes(self):
        for prefix, suffix in [('', ''), ('```json\n', '\n```'), ('Here is the answer:\n', '')]:
            raw = prefix + json.dumps({'action': 'final_answer', 'final_answer': {'value': 0}}) + suffix
            self.assertEqual(normalize_agent_payload(extract_json_object(raw), True)['final_answer'], {'value': 0})
        tool = {'action': 'tool_call', 'tool': 'python_exec', 'args': {'code': 'print({})'}}
        self.assertEqual(normalize_agent_payload(extract_json_object(json.dumps(tool)), True)['action'], 'tool_call')
        for answer in (0, False, {'value': 0}):
            self.assertEqual(normalize_agent_payload({'action': 'final_answer', 'final_answer': answer}, True)['final_answer'], answer)

    def test_nested_arguments_are_not_salvaged_from_a_broken_envelope(self):
        tool = {'action': 'tool_call', 'tool': 'python_exec', 'args': {'code': 'print(1)'}}
        broken = json.dumps(tool)[:-1]
        with self.assertRaises(ValueError):
            normalize_agent_payload(extract_json_object(broken), True)

    def test_xml_inside_an_answer_is_data(self):
        answer = {'excerpt': '<function>quoted source text</function>'}
        raw = json.dumps({'action': 'final_answer', 'final_answer': answer})
        self.assertEqual(normalize_agent_payload(extract_json_object(raw), True)['final_answer'], answer)

    def test_malformed_outer_and_parameters(self):
        for raw in ['{"action":"tool_call","args":{"code":"print(1)"}',
                    '{"action":"tool_call","args":{"code":"x={}\ny=1"}}',
                    '<tool_call><parameter=args>{"path":"x"}</parameter></tool_call>',
                    '{"answer":1} {"answer":2}']:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                extract_json_object(raw)
        for obj in [{}, {'code': 'print(1)'}, {'path': 'x'}, {'action': 'final_answer'},
                    {'action': 'final_answer', 'final_answer': {}}, {'action': 'tool_call', 'args': {}},
                    {'tool': 'python_exec', 'args': '{bad'}]:
            with self.subTest(obj=obj), self.assertRaises(ValueError):
                normalize_agent_payload(obj, True)



if __name__ == '__main__':
    unittest.main()
