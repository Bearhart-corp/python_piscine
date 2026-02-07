from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """class abtraite qui sert d'interface"""
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    """contrat, tous les enfants devront avoir cette méthode"""
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        """on filtre les datas et on return data si on trouve des critères dans str"""
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [d for d in data_batch if criteria.lower() in str(d).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """getter"""
        return {
            "stream_id": self.stream_id,
            "processed": self.processed_count
        }


class SensorStream(DataStream):
    """on test le type"""
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = [
                v for v in data_batch
                if isinstance(v, (int, float))
            ]
            self.processed_count += len(temps)
            avg = sum(temps) / len(temps) if temps else 0
            return f"Sensor data: {len(temps)} readings processed, avg={avg}"
        except Exception:
            return "Sensor stream processing error"


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            values = [
                v for v in data_batch
                if isinstance(v, int)
            ]
            self.processed_count += len(values)
            net = sum(values)
            return f"Transaction data: {len(values)} operations, net flow={net}"
        except Exception:
            return "Transaction stream processing error"


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events = [
                v for v in data_batch
                if isinstance(v, str)
            ]
            self.processed_count += len(events)
            errors = len([e for e in events if "error" in e.lower()])
            return f"Event data: {len(events)} events, {errors} error(s) detected"
        except Exception:
            return "Event stream processing error"


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def register(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        for stream, batch in zip(self.streams, batches):
            result = stream.process_batch(batch)
            print(f"- {result}")


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.register(sensor)
    processor.register(transaction)
    processor.register(event)

    batches = [
        [22.5, 23.0, 21.5],
        [100, -50, -25],
        ["login", "error", "logout"]
    ]

    print("\n=== Polymorphic Stream Processing ===")
    processor.process_all(batches)

    print("\nStream statistics:")
    for s in processor.streams:
        print(s.get_stats())

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
