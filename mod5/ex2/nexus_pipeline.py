from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol
import time
from collections import deque


# =========================
# STAGE INTERFACE (Protocol)
# =========================

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


# =========================
# PIPELINE BASE (ABC)
# =========================

class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.processed = 0
        self.errors = 0
        self.total_time = 0.0

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run(self, data: Any) -> Any:
        start = time.time()
        try:
            for stage in self.stages:
                data = stage.process(data)
            self.processed += 1
            return self.process(data)
        except Exception:
            self.errors += 1
            return "Pipeline error – recovery engaged"
        finally:
            self.total_time += time.time() - start

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def stats(self) -> Dict[str, Union[str, int, float]]:
        efficiency = (
            (self.processed / (self.processed + self.errors)) * 100
            if self.processed + self.errors > 0 else 0
        )
        return {
            "pipeline_id": self.pipeline_id,
            "processed": self.processed,
            "errors": self.errors,
            "efficiency": efficiency,
            "time": round(self.total_time, 3)
        }


# =========================
# PIPELINE STAGES
# =========================

class InputStage:
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid input")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data["validated"] = True
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        return data


# =========================
# ADAPTER PIPELINES
# =========================

class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        if isinstance(data, dict):
            return f"Processed JSON payload: {data}"
        return "Invalid JSON data"


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        if isinstance(data, str):
            fields = data.split(",")
            return f"CSV processed: {len(fields)} fields"
        return "Invalid CSV data"


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        if isinstance(data, list):
            avg = sum(data) / len(data) if data else 0
            return f"Stream summary: {len(data)} readings, avg={round(avg, 2)}"
        return "Invalid Stream data"


# =========================
# NEXUS MANAGER
# =========================

class NexusManager:
    def __init__(self):
        self.pipelines: deque[ProcessingPipeline] = deque()

    def register(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def chain_process(self, data: Any) -> Any:
        for pipeline in self.pipelines:
            data = pipeline.run(data)
        return data

    def report(self) -> None:
        for p in self.pipelines:
            print(p.stats())


# =========================
# MAIN DEMO
# =========================

def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    json_pipeline = JSONAdapter("JSON_PIPE")
    csv_pipeline = CSVAdapter("CSV_PIPE")
    stream_pipeline = StreamAdapter("STREAM_PIPE")

    for p in (json_pipeline, csv_pipeline, stream_pipeline):
        p.add_stage(InputStage())
        p.add_stage(TransformStage())
        p.add_stage(OutputStage())

    manager = NexusManager()
    manager.register(json_pipeline)
    manager.register(csv_pipeline)
    manager.register(stream_pipeline)

    print("\n=== Multi-Format Data Processing ===")
    print(manager.chain_process({"sensor": "temp", "value": 23.5, "unit": "C"}))
    print(manager.chain_process("user,action,timestamp"))
    print(manager.chain_process([21.0, 22.5, 23.2, 21.7]))

    print("\n=== Performance Report ===")
    manager.report()

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
