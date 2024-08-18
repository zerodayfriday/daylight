import yaml
from src.abstract.rule_converter import AbstractRuleConverter
from sigma.backends.splunk import SplunkBackend
from sigma.configuration import SigmaConfiguration
from sigma.collection import SigmaCollection

class SplunkRuleConverter(AbstractRuleConverter):
    def __init__(self, config_file):
        with open(config_file, 'r') as config_yaml:
            self.config = SigmaConfiguration(yaml.safe_load(config_yaml))
        self.backend = SplunkBackend(self.config)

    def convert_rule(self, rule_content):
        rule = SigmaCollection(yaml.safe_load(rule_content))
        return self.backend.generate(rule)

    def bulk_convert_rules(self, rules_directory):
        # Implementation for bulk conversion
        pass