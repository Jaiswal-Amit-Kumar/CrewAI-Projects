#!/usr/bin/env python
import sys
import warnings

from research_report.crew import ResearchReport

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Advancements in AI',
    }

    try:
        ResearchReport().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
