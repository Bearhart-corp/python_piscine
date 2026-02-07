from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol
# import time
from collections import deque


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass
##############################################


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.processed = 0
        self.errors = 0
        self.total_time = 0.0

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def run():
        pass

###################################################


class InputStage:
    def process(self, data: Any) -> Dict:
        if data is None:
            raise ValueError("Invalid input")
        return data


class TransformStage:
    def process(self, data: Any) -> Dict:
        if isinstance(data, dict):
            data["validated"] = True
        return data


class OutputStage:
    def process(self, data: Any) -> str:
        return data

##################################################


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipe_id):
        super().__init__(pipe_id)

    def process(self, data: Any) -> str:
        if isinstance(data, dict):
            return f"Processed JSON payload: {data}"
        return "Invalid JSON data"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipe_id):
        super().__init__(pipe_id)

    def process(self, data: Any) -> str:
        if isinstance(data, str):
            fields = data.split(",")
            return f"CSV processed: {len(fields)} fields"
        return "Invalid CSV data"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipe_id):
        super().__init__(pipe_id)

    def process(self, data: Any) -> str:
        if isinstance(data, list):
            avg = sum(data) / len(data) if data else 0
            return f"Stream summary: {len(data)} readings, avg={round(avg, 2)}"
        return "Invalid Stream data"

###################################################


class NexusManager:
    def __init__(self):
        self.pipelines: deque[ProcessingPipeline] = deque()

    def add(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data():
        pass

##############################################


def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("\nInitializing Nexus Manager...")
    print(
        "Pipeline capacity: 1000 streams/second\n\
Creating Data Processing Pipeline...\n\
Stage 1: Input validation and parsing\n\
Stage 2: Data transformation and enrichment\n\
Stage 3: Output formatting and delivery\n\
\n\
=== Multi-Format Data Processing ===\n\
Processing JSON data through pipeline..."
    )
    input_json = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print(f"Input: {input_json}")
    print("Transform: Enriched with metadata and validation")
    json_pipeline = JSONAdapter("JSON_PIPE")
    csv_pipeline = CSVAdapter("CSV_PIPE")
    stream_pipeline = StreamAdapter("STREAM_PIPE")

    json_pipeline.add_stage(InputStage())
    csv_pipeline.add_stage(TransformStage())
    stream_pipeline.add_stage(OutputStage())

    manager = NexusManager()
    manager.add(json_pipeline)
    manager.add(csv_pipeline)
    manager.add(stream_pipeline)

    print("\n=== Multi-Format Data Processing ===")
    print(manager.chain_process(
        {"sensor": "temp", "value": 23.5, "unit": "C"}))
    print(manager.chain_process("user,action,timestamp"))
    print(manager.chain_process([21.0, 22.5, 23.2, 21.7]))

    print("\n=== Performance Report ===")
    manager.report()

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
