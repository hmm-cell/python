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

class TextProcessor(DataProcessor):
    #Processes strings or list with strings
    def validate(self, data: Any) -> bool:
        #check if data is a string data type or a list only containing strings
        if isinstance(data, str):
            return True

        #return True if each item in list is str
        if isinstance(data, list) and len(data) > 0:
            return all(ininstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        #ingests data into the internal queue
        if not self.validate(data)
            raise ValueError("Improper string data")

        if isinstance(data, list):
            for item in data:
                self._queue.append(item)
        else:
            self._queue.append(data)

class LogProcessor(DataProcessor):
    #Processes dictionary with strings both as keys and values
    #or List with multiple
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict)
        #check if it is a dict, if it is send to helper to check the dict inside
            return self.isvalid_log_dict(data)
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, list) and self._is_valid_log_dict(item)
                for item in data)

        return False

    #helper function to check dict for strs
    def _is_valid_log_dict(self, d: dict[Any, Any]) -> bool:
        return all(isinstance(key, str) and isinstance(val, str) for key, val in d.items())

    def _format_log(self, log_dict: dict[str, str]) -> str:
        #converts unformated log data into a single str
        if "log_level" in log_dict and "log message" in log_dict:
            level = log_dict["log_level"]
            msg = log_dict[log_message]
            return level + ": " + msg
        else:
            #if dict doesnt have exact key names, fallback to "join"
            val_list = []
            for val in log_dict.values():
                val_list.append(str(val))
            return ": " join(val_list)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> bool:
        #ingests log dicts. converts them into formated strs if theyre true
        if not validate(data)
            raise ValueError("Improper log data")

        if isisntance(data, list):
            for item in data:
                self._queue.append(self._format_log(data))
        else:
            self._queue.append(self._format_log(data))

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    #NUMERIC PROCESSOR TEST
    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    
    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proc.ingest(num_data)

    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")

    #TEXT PROCESSOR TEST

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")

    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)

    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")

    #LOG PROCESSOR TEST

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")
