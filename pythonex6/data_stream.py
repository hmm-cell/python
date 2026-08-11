from abc import ABC, abstractmethod
from typing import Any

#Abstract base class that defines the polymorphism for the data processors
class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[str] = []
        self._rank: int = 0
        self._processed: int = 0

    def _add_to_queue(self, item: str) -> None:
        self._processed += 1
        self._queue.append(item)
        
    #verify if input data is appropriate for this data procesor
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    #ingest input data after validation, converting and storing internally
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    #it will extract the first in data(FIFO) alongside with its rank
    def output(self) -> tuple[int, str]:
        if not self.queue:
            raise IndexError("there is no data available")

class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        
    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        success = False;
        for proc in self._processors:
            if proc.validatelf._processors(proc)

class NumericProcessor(DataProcessor):
    name = "Numeric Processor"
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
            return all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        #converts numbers into strings
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._add_to_queue(str(item))
        else:
                self._add_to_queue(str(data))

class TextProcessor(DataProcessor):
    name = "Text Processor"
    #Processes strings or list with strings
    def validate(self, data: Any) -> bool:
        #check if data is a string data type or a list only containing strings
        if isinstance(data, str):
            return True

        #return True if each item in list is str
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        #ingests data into the internal queue
        if not self.validate(data):
            raise ValueError("Improper string data")

        if isinstance(data, list):
            for item in data:
                self._add_to_queue(item)
        else:
            self._add_to_queue(data)

class LogProcessor(DataProcessor):
    name = "Log Processor"
    #Processes dictionary with strings both as keys and values
    #or List with multiple
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
        #check if it is a dict, if it is send to helper to check the dict inside
            return self.isvalid_log_dict(data)
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, dict) and self._is_valid_log_dict(item)
                for item in data)

        return False

    #helper function to check dict for strs
    def _is_valid_log_dict(self, d: dict[Any, Any]) -> bool:
        return all(isinstance(key, str) and isinstance(val, str) for key, val in d.items())

    def _format_log(self, log_dict: dict[str, str]) -> str:
        #converts unformated log data into a single str
        if "log_level" in log_dict and "log_message" in log_dict:
            level = log_dict["log_level"]
            msg = log_dict["log_message"]
            return level + ": " + msg
        else:
            #if dict doesnt have exact key names, fallback to "join"
            val_list = []
            for val in log_dict.values():
                val_list.append(str(val))
            return ": ".join(val_list)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> bool:
        #ingests log dicts. converts them into formated strs if theyre true
        if not validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                self._add_to_queue(self._format_log(item))
        else:
            self._add_to_queue(self._format_log(data))
    log_proc.ingest(log_data)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")
