import pandas as pd
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class TimeLogParser:
    """
    Ingests and normalizes operations time logs to calculate manual burden.
    """
    def __init__(self):
        # Setting up basic configuration
        pass

    def parse_mock_logs(self) -> List[Dict[str, Any]]:
        """
        Simulates parsing a CSV of operations time-tracking data.
        In production, this would use pd.read_csv() and perform grouping.
        """
        logger.info("Parsing operational time logs...")
        
        # Simulated aggregated data (e.g., grouped by Task Category)
        mock_data = [
            {
                "process_name": "Vendor Invoice Reconciliation",
                "manual_hours_weekly": 14.5,
                "process_description": "Manually downloading PDFs from 3 portals, extracting line items, and comparing them against the master Excel sheet."
            },
            {
                "process_name": "L1 Escalation Triage",
                "manual_hours_weekly": 22.0,
                "process_description": "Reading incoming Zendesk tickets, determining which product team owns the issue based on keywords, and re-assigning."
            },
            {
                "process_name": "Quarterly Vendor Negotiations",
                "manual_hours_weekly": 5.0,
                "process_description": "Meetings with vendors to negotiate contract terms and pricing for the upcoming quarter."
            }
        ]
        
        return mock_data
