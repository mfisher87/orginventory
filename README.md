# `orginventory`

`orginventory` scans your organization's Git repositories on hosting services for
their software dependencies and generates a report.

**This software is in early development stages. Do not expect anything to work. This
README should be considered a design document only.**


## Current goals

* SBOM tool that analyzes Git (or other?) source code repositories stored on hosting
  services, e.g. GitHub.
* Basic pluggable "repository linter" that's capable of flagging issues, e.g.:
    * Detecting the use of EOL language versions in development or build depencency
      specifications..
    * If your organization is concerned with dependency drift, you might write a rule
      that warns when  development or build dependency specifications (like
      `environment.yml`, `recipe/meta.yaml`) which haven't been updated in a certain
      amount of time.
* Have a sweet name.


## Usage

**This software is currently not packaged in any form; it must be run from source.**

```
PYTHONPATH=. python orginventory/cli.py \
  --org-url "github.com/nsidc" \
  --level info \
  -k <PAT HERE>
```

* `-o github.com/nsidc`: Specify your organization by its URL.
* `--type info`: Specify
* `-k <PAT HERE>`: Specify your Personal Access Token for authorization. _NOTE: Without
  a PAT, only publicly visible repos will be returned._


### Report levels

The following values can be used with `--level`:

* `info`: Report everything, even if it's not a problem.
* `warning`: Report minor problems or things that will be major problems in 1 year.
* `error`: Report major problems (e.g. language at EOL)


### What it can report

#### Hosting services

* GitHub


#### Language

* Does your project require Python, Javascript, or Ruby?
* What version?
* When is that version EOL? Yes: `error`; will EOL within one year: `warning`.


## Limitations

This software does not solve environments or install packages. It simply analyzes
environment specifications (e.g. `environment.yml`) for what you intend to install.


## Future concerns

* How to package and distribute this software?


### TODO

* Support JSON output for all commands
* Support Bitbucket
* Find a reliable source for EOL data. <https://endoflife.date/>?
* Consider standard output formats, e.g. CycloneDX, SPDX, ?
* Can we leverage existing software, like dependabot or one of its components, to replace
  components of this software?
    * Many SBOM tools don't support Conda
    * [bibliothecary](https://github.com/librariesio/bibliothecary) does support Conda,
      does it do something useful to this project?
