"""Data containers for representing dependencies found in a repository."""
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Dependency:
    name: str
    version_spec: str


@dataclass
class DependencyData:
    package_manager: str
    dependency_file_path: Path
    # TODO: Separate libraries and languages?
    dependencies: list[Dependency]
