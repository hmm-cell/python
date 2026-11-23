from abc import ABC, abstractmethod
from typing import Any
 
 
class DataProcessor(ABC):
    """Abstract base class defining the common processor interface."""
 
    name: str
 
    def __init__(self) -> None:
        self._queue: list[str] = []
        self._rank: int = 0
        self._processed: int = 0
 
    def _add_to_queue(self, item: str) -> None:
        self._processed += 1
        self._queue.append(item)
 
    # Verify if input data is appropriate for this data processor.
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
 
    # Ingest input data after validation, storing it internally.
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
 
    # Extract the oldest data (FIFO) along with its extraction rank.
    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise IndexError("there is no data available")
        rank = self._rank
        self._rank += 1
        value = self._queue.pop(0)
        return rank, value
 
 
class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
 
    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
 
    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            success = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    success = True
                    break
            if not success:
                print(
                    "DataStream error - Can't process element in "
                    f"stream: {item}"
                )
 
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
        for proc in self._processors:
            remaining = len(proc._queue)
            print(
                f"{proc.name}: total {proc._processed} items "
                f"processed, remaining {remaining} on processor"
            )
 
 
class NumericProcessor(DataProcessor):
    name = "Numeric Processor"
 
    # Processes numeric data: int, float, or lists of either.
    def validate(self, data: Any) -> bool:
        # bool is a subclass of int in Python, so it must be
        # explicitly rejected here.
        if isinstance(data, bool):
            return False
 
        if isinstance(data, (int, float)):
            return True
 
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(item, (int, float))
                and not isinstance(item, bool)
                for item in data
            )
 
        return False
 
    def ingest(self, data: int | float | list[int | float]) -> None:
        # Converts numbers into strings before storing them.
        if not self.validate(data):
            raise ValueError("Improper numeric data")
 
        if isinstance(data, list):
            for item in data:
                self._add_to_queue(str(item))
        else:
            self._add_to_queue(str(data))
 
 
class TextProcessor(DataProcessor):
    name = "Text Processor"
 
    # Processes strings or lists of strings.
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
 
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, str) for item in data)
 
        return False
 
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper string data")
 
        if isinstance(data, list):
            for item in data:
                self._add_to_queue(item)
        else:
            self._add_to_queue(data)
 
 
class LogProcessor(DataProcessor):
    name = "Log Processor"
 
    # Processes a dict of str:str pairs, or a list of such dicts.
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._is_valid_log_dict(data)
 
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(item, dict) and self._is_valid_log_dict(item)
                for item in data
            )
 
        return False
 
    # Helper: checks that every key and value in the dict is a str.
    def _is_valid_log_dict(self, d: dict[Any, Any]) -> bool:
        return all(
            isinstance(key, str) and isinstance(val, str)
            for key, val in d.items()
        )
 
    def _format_log(self, log_dict: dict[str, str]) -> str:
        # Converts a raw log dict into a single formatted string.
        if "log_level" in log_dict and "log_message" in log_dict:
            level = log_dict["log_level"]
            msg = log_dict["log_message"]
            return level + ": " + msg
 
        # Fallback for dicts without the expected keys.
        return ": ".join(str(val) for val in log_dict.values())
 
    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
 
        if isinstance(data, list):
            for item in data:
                self._add_to_queue(self._format_log(item))
        else:
            self._add_to_queue(self._format_log(data))
 
 
if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
 
    ds = DataStream()
    ds.print_processors_stats()
 
    log_proc = LogProcessor()
    text_proc = TextProcessor()
    num_proc = NumericProcessor()
 
    print("Registering Numeric Processor")
    ds.register_processor(num_proc)
 
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead',
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected',
            },
        ],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {batch}")
 
    ds.process_stream(batch)
    ds.print_processors_stats()
 
    print("Registering other data processors")
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)
 
    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()
 
    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        rank, val = num_proc.output()
    for _ in range(2):
        rank, val = text_proc.output()
    for _ in range(1):
        rank, val = log_proc.output()
 
    ds.print_processors_stats()
