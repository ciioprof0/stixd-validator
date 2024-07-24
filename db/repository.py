from abc import ABC, abstractmethod
from typing import List

class AbstractRepository(ABC):

    @abstractmethod
    def load_entries(self) -> List:
        pass

    @abstractmethod
    def save_entry(self, entry) -> None:
        pass

    @abstractmethod
    def find_entry_by_id(self, entry_id: int):
        pass
