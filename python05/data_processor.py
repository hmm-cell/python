from abc import ABC, abstractmethod
from typing import Any


# Abstract base class that defines the common interface for data processors
class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[str] = []
        self._rank: int = 0

    # Verify if input data is appropriate for this data processor
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    # Ingest input data after validation, storing it internally
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # Extract the oldest data (FIFO) along with its rank
    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise IndexError("there is no data available")
        rank = self._rank
        self._rank += 1
        value = self._queue.pop(0)
        return rank, value


class NumericProcessor(DataProcessor):
    # Processes numeric data: int, float, or non-empty lists of either
    def validate(self, data: Any) -> bool:
        # bool is a subclass of int in Python, so reject it explicitly
        if isinstance(data, bool):
            return False

        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )

        return False

    def ingest(self, data: Any) -> None:
        # Convert numbers into strings and store each item separately
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._queue.append(str(item))
        else:
            self._queue.append(str(data))


class TextProcessor(DataProcessor):
    # Processes strings or non-empty lists of strings
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper string data")

        if isinstance(data, list):
            for item in data:
                self._queue.append(item)
        else:
            self._queue.append(data)


class LogProcessor(DataProcessor):
    # Processes a dict of str: str pairs, or a non-empty list of such dicts
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._is_valid_log_dict(data)

        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(item, dict) and self._is_valid_log_dict(item)
                for item in data
            )

        return False

    # Helper to verify all keys and values are strings
    def _is_valid_log_dict(self, d: dict[Any, Any]) -> bool:
        return all(
            isinstance(key, str) and isinstance(val, str)
            for key, val in d.items()
        )

    def _format_log(self, log_dict: dict[str, str]) -> str:
        # Convert log dictionary into a single formatted string
        if "log_level" in log_dict and "log_message" in log_dict:
            level = log_dict["log_level"]
            msg = log_dict["log_message"]
            return f"{level}: {msg}"

        val_list: list[str] = []
        for val in log_dict.values():
            val_list.append(str(val))
        return ": ".join(val_list)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                self._queue.append(self._format_log(item))
        else:
            self._queue.append(self._format_log(data))


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # NUMERIC PROCESSOR TEST
    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print(
        "Test invalid ingestion of string 'foo' without prior validation:"
    )
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

    # TEXT PROCESSOR TEST
    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")

    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)

    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")

    # LOG PROCESSOR TEST
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
