import click

@click.group()
def cli():
    pass


org_url_option = click.option(
    "--org-url", "-o",
    help="Organization URL (e.g. 'github.com/nsidc')",
    required=True,
    type=str,
)


@cli.command(help="List organization's repositories")
@org_url_option
def list(org_url: str):
    from orginventory.scraper import get_org_repos

    for repodata in get_org_repos(org_url=org_url):
        print()
        print(repodata.name)
        print(f"  {repodata.url}")
        print(f"  {repodata.description}")


@cli.command(help="Report on language dependencies for all repos in org")
@org_url_option
def report(org_url: str):
    from orginventory.scraper import get_org_repos
    from orginventory.getter import git_repository
    from orginventory.parser import parse_repo
    from orginventory.analyzer import analyze_depdata

    analyses = []
    for repodata in get_org_repos(org_url=org_url):
        with git_repository(repodata.clone_url) as git_repo_path:
            depdata = parse_repo(git_repo_path)
            analysis = analyze_depdata(depdata)
            analyses.append(analysis)

    print(analyses)


if __name__ == '__main__':
    cli()
