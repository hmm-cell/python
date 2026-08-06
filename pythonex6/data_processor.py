from abc import ABC, abstractmethod
from typing import Any

#Abstract base class that defines the polymorphism for the data processors
class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: lsit[str] = []
        self._rank: int = 0

    #verify if input data is appropriate for this data procesor
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    #ingest input data after validation, converting and storing internally
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    #it will extract the first in data(FIFO) alongside with its rank
    @abstractmethod
    def output(self) -> tuple[int, str]:
        if not self.queue:
            raise IndexError("there is no data available")

class NumericProcessor(DataProcessor):
    #processes numeric type data. including int, float or lists of it
    def validate(self, data: Any) -> bool:
        #verify if its a bool, since in python a bool inherits from int
        #explicitly reject bool because we only want numeric data types
        if isinstance(data, bool):
            return False
            
        if isinstance(data, (int, float)):
            return True

        #if data len > 0, item in list is int or float and not bool, return true.
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, (int, float)) and not instance(item, bool) for item in data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        #converts numbers into strings
        if not self.validate(data)
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._queue.append(str(item))
        else:
                self._queue.append(str(data))

