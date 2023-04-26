"""Data container for representing repodata from hosting provider."""
from dataclasses import dataclass

@dataclass
class RepoData:
    name: str
    description: str
    url: str
    clone_url: str
    public: bool
