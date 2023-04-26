"""orginventory-analyzer

Analyzes a repository's parsed dependencies for:

* Language: Python, JS/TS
* Language EOL
* Dependency manager: Conda, pip, NPM, yarn
"""
from typing import Any

from orginventory.analyzer.analysis import Analysis
from orginventory.parser.depdata import DependencyData


def analyze_depdata(dependency_data: DependencyData) -> Analysis:
    ...
