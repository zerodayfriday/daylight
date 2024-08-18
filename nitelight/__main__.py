import os
import json
from src.implementations.splunk.rule_converter import SplunkRuleConverter
from src.implementations.splunk.search_backend import SplunkSearchBackend
from src.rule_tester import RuleTester

def main():
    config_file = '/path/to/sigma_splunk_config.yml'
    rule_converter = SplunkRuleConverter(config_file)
    search_backend = SplunkSearchBackend('localhost', 8000, 'admin', 'password')
    
    tester = RuleTester(rule_converter, search_backend)
    
    rule_file = 'rules/application/sus_process/rule.yml'
    test_cases_dir = 'rules/application/sus_process/test_cases'
    
    results = tester.test_rule(rule_file, test_cases_dir)
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()