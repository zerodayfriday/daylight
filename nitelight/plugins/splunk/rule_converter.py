import yaml
from nitelight.abstract.rule_converter import AbstractRuleConverter
from sigma.backends.splunk import SplunkBackend
from sigma.collection import SigmaCollection
from sigma.exceptions import SigmaError

class SplunkRuleConverter(AbstractRuleConverter):
    def __init__(self):
        self.backend = SplunkBackend()

    def convert_rule(self, rule_content):
        rule = SigmaCollection.from_yaml(rule_content)
        return self.backend.convert(rule)

    def bulk_convert_rules(self, rules_directory):
        # Implementation for bulk conversion
        pass
