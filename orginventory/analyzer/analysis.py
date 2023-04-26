"""Data containers for representing dependencies found in a repository."""
from dataclasses import dataclass


@dataclass
class Analysis:
    name: str
