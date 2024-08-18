import os
import json
from src.implementations.splunk.rule_converter import SplunkRuleConverter
from src.implementations.splunk.search_backend import SplunkSearchBackend

class RuleTester:
    def __init__(self, rule_converter, search_backend):
        self.rule_converter = rule_converter
        self.search_backend = search_backend

    def test_rule(self, rule_file, test_cases_dir):
        with open(rule_file, 'r') as f:
            rule_content = f.read()
        
        converted_query = self.rule_converter.convert_rule(rule_content)
        
        results = []
        for test_case_file in os.listdir(test_cases_dir):
            if test_case_file.endswith('.json'):
                with open(os.path.join(test_cases_dir, test_case_file), 'r') as f:
                    test_case = json.load(f)
                
                self.search_backend.ingest_test_data(test_case)
                
                search_results = self.search_backend.run_search(converted_query, test_case['time_range'])
                
                expected = 'true_positive' in test_case_file
                detected = len(search_results) > 0
                
                results.append({
                    'test_case': test_case_file,
                    'expected': expected,
                    'detected': detected,
                    'passed': expected == detected
                })
        
        return results
