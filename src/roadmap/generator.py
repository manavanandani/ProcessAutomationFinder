import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class RoadmapGenerator:
    """
    Synthesizes evaluated processes into a prioritized automation roadmap
    based on the time-saved-per-build-hour (ROI) heuristic.
    """
    
    def generate_prioritized_roadmap(self, evaluated_processes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Sorts and filters opportunities to surface the highest-impact targets first.
        """
        valid_targets = []
        
        for process in evaluated_processes:
            # Skip unfeasible processes
            if process["evaluation"]["feasibility_score"] < 0.5:
                continue
                
            manual_hours_monthly = process["manual_hours_weekly"] * 4.33
            build_hours = process["evaluation"]["estimated_build_hours"]
            
            # ROI heuristic: How many hours do we save monthly per hour spent building?
            roi_ratio = manual_hours_monthly / build_hours
            
            process["roi_ratio"] = round(roi_ratio, 2)
            valid_targets.append(process)
            
        # Sort descending by ROI
        valid_targets.sort(key=lambda x: x["roi_ratio"], reverse=True)
        return valid_targets
