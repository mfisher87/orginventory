from urllib.parse import ParseResult

import requests
from loguru import logger

from orginventory.scraper.repodata import RepoData


def get_github_org_repos(
    purl: ParseResult,
    *,
    personal_access_token: str | None = None,
) -> list[RepoData]:
    """Get list of GitHub repos in given organization URL.
    
    Expects URLs to look like `github.com/nsidc` or `https://github.com/nsidc`.
    """
    if personal_access_token:
        raise NotImplementedError("Auth not implemented")

    # TODO: Use regex on a URL string instead of operating on a ParseResult?
    org_name = purl.path.removeprefix("/")
    if "/" in org_name:
        raise RuntimeError(f"Invalid {org_name=}")

    logger.info(f"Getting repo list for GitHub org: {org_name}")

    apicall_url = f"https://api.github.com/users/{org_name}/repos"
    repos_raw = requests.get(apicall_url).json()
    repos = [
        RepoData(
            name=r["name"],
            description=r["description"],
            url=r["html_url"],
            clone_url=r["clone_url"],
            public=not r["private"],
        ) for r in repos_raw
    ]

    logger.info(f"Found {len(repos)} repos!")
    return repos
