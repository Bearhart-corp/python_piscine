from abc import ABC, abstractmethod
from typing import Any


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        pass

    @abstractmethod
    def filter_data(self, data_batch: list[Any]) -> list[Any]:
        pass

    @abstractmethod
    def get_stats(self) -> dict[str, union[str, int, float]]:
        pass


class StreamManager(DataStream):
    pass


class AvancedFeatures(DataStream):
    pass


def main():
    datas = {
        "ID": [
            "SENSOR_001",
            "TRANS_001",
            "EVENT_001"
        ],
        "Type": [
            "Environmental Data"
            "Finacial Data"
            "System Events"
        ],
        "Process": {
            "sensor": {
                "temp": 22.5,
                "humidity": 65,
                "pressure": 1013
            },
            "transaction": {
                "buy": 100,
                "sell": 150,
                "buy2": 75
            },
            "event": [
                "login",
                "error",
                "logout"
            ]
        },
        "Analytics": {
            "sensor": {
                "reading_process": 3,
                "avg_temp": 22.5
            },
            "Transaction": {
                "op": 3,
                "net_flow": 25
            },
            "event": {
                "events": 3,
                "error": 1
            }
        }

    }
    print(datas)


if __name__ == "__main__":
    main()
