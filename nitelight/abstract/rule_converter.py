from abc import ABC, abstractmethod

class AbstractRuleConverter(ABC):
    @abstractmethod
    def convert_rule(self, rule_content):
        pass

    @abstractmethod
    def bulk_convert_rules(self, rules_directory):
        pass
