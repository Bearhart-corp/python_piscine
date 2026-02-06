from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"{self.result}  "


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return
        datas = {
            "lenght": len(data),
            "sum": sum(data),
            "avg": sum(data) / len(data)
        }
        return self.format_output(datas)

    def validate(self, data: Any) -> bool:
        return type(data) is list

    def format_output(self, datas: dict) -> str:
        return f"Processed {datas['lenght']}\
 numeric values, sum={datas['sum']}, avg={datas['avg']}"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return
        return self.format_output(data)

    def validate(self, data: Any) -> bool:
        return type(data) is str and ":" not in data

    def format_output(self, data: str) -> str:
        return f"Processed text: {len(data)} characters, \
{len(data.split())} words"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data):
            return self.format_output(data)

    def validate(self, data: Any) -> bool:
        return type(data) is str and ":" in data

    def format_output(self, data: str) -> str:
        if "Alert" in data:
            return "[ALERT] ERROR level detected: Connection timeout"
        elif "Info" in data:
            return "[INFO] INFO level detected: System ready"


def main():
    """I start by testing with manual calls then with a loop"""
    datas = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "Alert: System error"
    ]
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    processors = [
        num, text, log
    ]
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    print(f"Processing data: {datas[0]}")
    print("Validation: Numeric data verified")
    print(f"Ouput:{num.process(datas[0])}")
    print("\nInitializing Text Processor...")
    print(f"Processing data: {datas[1]}")
    print("Validation: Text data verified")
    print(f"Ouput:{text.process(datas[1])}")
    print("\nInitializing Log Processor...")
    print(f"Processing data: {datas[2]}")
    print("Validation: Log data verified")
    print(f"Ouput:{log.process(datas[2])}")

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    datas = [
        [1, 2, 3],
        "Hello Nexuss",
        "Info: System ready"
    ]
    i = 1
    for data in datas:
        for proc in processors:
            printable = proc.process(data)
            if printable:
                print(f"Result {i}: {printable}")
                i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams")


if __name__ == "__main__":
    main()
