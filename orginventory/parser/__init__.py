"""orginventory-parser

Parse a repository; look for config files for various dependency managers (conda, pip,
rubygems, npm, yarn, etc.) and generate a representation.
"""
from pathlib import Path
from typing import Any

from orginventory.parser.depdata import DependencyData

package_managers = {
    'conda': {
        'matcher': r'environment.y[a]ml',
        'handler': NotImplemented,
    },
    'pip': {
        'matcher': r'requirements.txt',
        'handler': NotImplemented,
    },
    'npm': {
        'matcher': r'package.json',
        'handler': NotImplemented,
    },
    'puppet': {
        'matcher': r'Puppetfile',
        'handler': NotImplemented,
    },
}


def parse_repo(repo_path: Path) -> list[DependencyData]:
    """Find dependencies as defined by package manager config files."""
    dep_data = []
    for package_manager, pm_attrs in package_managers.items():
        for pm_configs in match_files_in_dir(pm_attrs["matcher"]):
            dep_data.append(pm_attrs["handler"](pm_config))

    return dep_data
