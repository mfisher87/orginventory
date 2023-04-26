"""orginventory-getter

Downloads a repository by URL to a temporary location. Provides a context manager with
automated cleanup.
"""
import subprocess
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Generator

from loguru import logger


@contextmanager
def git_repository(clone_url: str) -> Generator[Path, None, None]:
    """Clone a Git repository from a url, and clean up when done."""
    with TemporaryDirectory() as tmp_dir:
        tmp_dir_path = Path(tmp_dir)
        clone_repository(clone_url, path=tmp_dir_path)
        yield tmp_dir_path


def clone_repository(clone_url: str, *, path: Path) -> None:
    subprocess.run(
        [
            'git',
            'clone',
            '--depth=1',
            clone_url,
            str(path),
        ],
        check=True,
    )
    logger.info(f"Cloned {clone_url}")
