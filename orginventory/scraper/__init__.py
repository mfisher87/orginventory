"""orginventory-scraper

Gets a list of an organization's repo URLs from a hosting provider.

Supported: GitHub, Bitbucket.
"""
from urllib.parse import urlparse, ParseResult

from loguru import logger

from orginventory.scraper.repodata import RepoData
from orginventory.scraper.github import get_github_org_repos 


def get_org_repos(
    org_url: str,
    *,
    personal_access_token: str | None = None,
) -> list[RepoData]:
    """Take an organization URL and get a list of repos in that org.
    
    Organization URLs look like:

    * github.com/nsidc
    * TODO: bitbucket.org/nsidc
    """
    if not personal_access_token:
        logger.warning('No personal access token provided; only reporting public repos.')

    try:
        # urllib.parse will not recognize a `netloc` without `//` before it:
        #    https://docs.python.org/3/library/urllib.parse.html
        if not org_url.startswith('http://') or not org_url.startswith('https://'):
            org_url = f"//{org_url}"

        purl = urlparse(org_url)
    except:
        raise RuntimeError(f"Could not parse {org_url=}")

    if purl.netloc == "github.com":
        return get_github_org_repos(purl)

    else:
        breakpoint()
        raise RuntimeError(f"Unsupported hosting platform in {org_url=}")
