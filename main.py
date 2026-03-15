import json
import logging
from src.ingestion.log_parser import TimeLogParser
from src.analyzer.llm_evaluator import ProcessEvaluator
from src.roadmap.generator import RoadmapGenerator

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_finder_demo():
    print("Initializing Process Automation Finder...\n")
    
    parser = TimeLogParser()
    evaluator = ProcessEvaluator()
    roadmap_gen = RoadmapGenerator()
    
    # 1. Ingest Data
    raw_logs = parser.parse_mock_logs()
    
    # 2. Evaluate each process
    evaluated_processes = []
    for log in raw_logs:
        eval_result = evaluator.evaluate_process(log["process_description"])
        log["evaluation"] = eval_result
        evaluated_processes.append(log)
        
    # 3. Generate Roadmap
    roadmap = roadmap_gen.generate_prioritized_roadmap(evaluated_processes)
    
    # 4. Output Results
    print("\n--- Prioritized Automation Roadmap ---")
    for i, target in enumerate(roadmap, 1):
        print(f"\nPriority {i}: {target['process_name']}")
        print(f"  - Recommended Tech: {target['evaluation']['automation_type']}")
        print(f"  - ROI Ratio: {target['roi_ratio']} (Hours saved monthly per build hour)")
        print(f"  - Est. Build Hours: {target['evaluation']['estimated_build_hours']}h")
        
    print("\nProcess complete. Tool successfully surfaced the highest-impact targets.")

if __name__ == "__main__":
    run_finder_demo()
