import os
import json
from nitelight.plugins.splunk.rule_converter import SplunkRuleConverter
from nitelight.plugins.splunk.search_backend import SplunkSearchBackend
from nitelight.rule_tester import RuleTester

def main():
    rule_converter = SplunkRuleConverter()
    search_backend = SplunkSearchBackend('localhost', 8000, 'admin', 'password')
    
    tester = RuleTester(rule_converter, search_backend)
    
    rule_file = 'rules\\application\\sus_process\\rule.yaml'
    test_cases_dir = 'rules\\application\\sus_process\\tests'
    
    results = tester.test_rule(rule_file, test_cases_dir)
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()