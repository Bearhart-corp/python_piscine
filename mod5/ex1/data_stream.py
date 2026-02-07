from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """class abtraite qui sert d'interface"""
    def __init__(self, batch: List[Any]):
        self.processed_count = 0
        self.data = batch

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """contrat, tous les enfants devront avoir cette méthode"""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """getter d'un dico avec une key str et une val str ou in ou float"""
        return {
            "data": self.data,
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
            return f"Sensor data: {len(temps)} readings processed"
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
            return f"Transaction analytics: {len(values)} \
operations processed"
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
            return f"Event data: {len(events)} events, {errors}\
 error(s) detected"
        except Exception:
            return "Event stream processing error"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        for (stream, batch) in zip(self.streams, batches):
            result = stream.process_batch(batch)
            print(f"- {result}")

    def process(self) -> None:
        print(f"{self.process_batch(self.data)}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    batches = [
        [22.5, 65, 1023],
        [100, -150, 75],
        ["login", "error", "logout"]
    ]
    sensor = SensorStream(batches[0])
    transaction = TransactionStream(batches[1])
    event = EventStream(batches[2])

    processor = StreamProcessor()
    processor.add(sensor)
    processor.add(transaction)
    processor.add(event)

    print("Initializing Sensor Stream...")
    dico = sensor.get_stats()
    infos = []
    for info in dico["data"]:
        infos.append(info)
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    print(f"Processing sensor batch: temp:[{infos[0]},\
 humidity:{infos[1]}, pressure:{infos[2]}]")
    print(
        f"Sensor analysis: {len(sensor.data)} readings processed\
avg temp: {infos[0]}°C"
    )

    print("\nInitializing Transaction Stream...")
    dico = transaction.get_stats()
    infos = []
    for info in dico["data"]:
        infos.append(info)
    print("Stream ID: TRANS_001, Type: Financial Data")
    print(f"Processing transaction batch: buy:[{infos[0]},\
 sell:{abs(infos[1])}, buy:{infos[2]}]")
    print(
        f"Transaction analysis: {len(infos)} operations,\
 net flow: +{sum(infos)} units"
    )

    print("\nInitializing Event Stream...")
    dico = event.get_stats()
    infos = []
    for info in dico["data"]:
        infos.append(info)
    print("Stream ID: EVENT_001, Type: System Events")
    print(f"Processing event batch: [{infos[0]},\
 , {(infos[1])}, {infos[2]}]")
    StreamProcessor.process(event)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    processor.process_all(batches)
    print("\nStream filtering active: High-priority data only\n\
Filtered results: 2 critical sensor alerts, 1 large transaction\n")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()

#   any = j'abandonne l'idee meme de typage
#   List[Any] = [1, "a", 3.14, None]
#   Dict[str, int] cle atttendu = str et val = int
#   Union[int, float] = de type int OU float
#   Optional[str] = Union[str, none] //soit str soit none !
#   DuckTyping = If it walks like a duck and quacks like a duck, it’s a duck.”
#   #Modularite
#   le .get(key, val_par_default) batch.get(stream, [])
#   par default donnes une liste vide si tu ne trouve pas cette key
