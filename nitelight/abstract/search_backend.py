from abc import ABC, abstractmethod

class AbstractSearchBackend(ABC):
    @abstractmethod
    def run_search(self, query, time_range):
        pass

    @abstractmethod
    def ingest_test_data(self, test_data):
        pass
