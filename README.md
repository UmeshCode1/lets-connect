# GitHub Activity Lab

[![CI](https://github.com/UmeshCode1/lets-connect/actions/workflows/ci.yml/badge.svg)](https://github.com/UmeshCode1/lets-connect/actions/workflows/ci.yml)
[![Action Test](https://github.com/UmeshCode1/lets-connect/actions/workflows/action-test.yml/badge.svg)](https://github.com/UmeshCode1/lets-connect/actions/workflows/action-test.yml)
[![Marketplace](https://img.shields.io/badge/GitHub%20Marketplace-Activity%20Lab-181717?logo=github)](https://github.com/marketplace/actions/github-activity-lab-contribution-milestone-tracker)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**GitHub Activity Lab** is an open-source Python toolkit, command-line interface (CLI), and GitHub Actions composite action for inspecting Git contribution metadata and repository activity. It includes co-author trailer parsing, contributor statistics, commit-message checks, milestone references, pull-request review analytics, and optional Claude-assisted PR summaries.

> The project reports repository-local or API-derived signals. It does not verify GitHub achievement eligibility, replace human code review, or guarantee that a contribution will qualify for an achievement.

## What it does

| Area | Capabilities |
| --- | --- |
| Git metadata | Parse recent commit history and standard Git trailers such as `Co-authored-by:` |
| Contributor analytics | Summarize primary author and co-author contributions from the inspected history |
| Commit hygiene | Check commit subjects against the project's Conventional Commits validator |
| GitHub Action | Run an audit in CI and publish a Markdown summary to the GitHub Actions step summary |
| AI-assisted review | Produce a PR-oriented summary using the Anthropic API, an optional local CLI integration, or a deterministic heuristic fallback |
| Repository insights | Query pull requests and reviews, inspect stargazer timestamps, and calculate star-velocity estimates |
| Developer utilities | Generate co-author trailers, inspect achievement reference data, and export structured reports |

## Quick start

### Requirements

- Python 3.9 or newer.
- Git installed and available on `PATH` for local repository-history commands.
- An Anthropic API key only when you want to call the Anthropic Messages API.

### Install from source

```bash
git clone https://github.com/UmeshCode1/lets-connect.git
cd lets-connect
python -m pip install -e .
```

Check the available commands:

```bash
activity-lab --help
```

### Common CLI commands

Run a local contribution summary:

```bash
activity-lab stats --repo . --limit 100
```

Inspect co-author trailers:

```bash
activity-lab check-trailers --repo . --limit 100
```

Check the achievement reference registry:

```bash
activity-lab milestones
```

Generate a correctly formatted co-author trailer:

```bash
activity-lab format-coauthor --name "Jane Doe" --email "jane@example.com"
```

Analyze repository star velocity (API access may be rate-limited without a token):

```bash
activity-lab star-velocity --owner OWNER --repo REPOSITORY
```

Inspect review participation:

```bash
activity-lab review-stats --owner OWNER --repo REPOSITORY --limit 50
```

Run the GitHub Actions audit locally:

```bash
activity-lab run-action --repo . --limit 50
```

Generate a PR-oriented review summary:

```bash
activity-lab ai-review --title "feat(api): add webhook endpoint" --body "Adds signed webhook handling."
```

The AI review command can use the Anthropic API when `ANTHROPIC_API_KEY` is available. If no API response is available, the implementation falls back to deterministic heuristic analysis. The heuristic fallback is not an LLM review and should not be treated as a security audit.

## GitHub Actions

The repository is published as a composite GitHub Action. Add a workflow such as `.github/workflows/activity-lab.yml` to the repository you want to inspect:

```yaml
name: Activity Lab

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run GitHub Activity Lab
        uses: UmeshCode1/lets-connect@v1
        with:
          repo-path: .
          limit: "50"
          enforce-coauthors: "false"
          enforce-conventional: "false"
          ai-review: "false"
```

Use a version tag or commit SHA appropriate to your release policy. The example uses `@v1`; confirm that the tag exists and points to the release you intend to consume before relying on it in production workflows.

### Action inputs

| Input | Description | Default |
| --- | --- | --- |
| `repo-path` | Path to the target Git repository | `.` |
| `limit` | Maximum number of recent commits to inspect | `50` |
| `enforce-coauthors` | Fail the action when no co-authored commits are found in the inspected history | `false` |
| `enforce-conventional` | Fail the action when inspected commit subjects do not pass the project's validator | `false` |
| `ai-review` | Enable the PR-summary/review path | `false` |
| `pr-title` | Pull-request title supplied by the workflow | Empty |
| `pr-body` | Pull-request body supplied by the workflow | Empty |
| `anthropic-api-key` | Optional Anthropic API key used for Claude-backed PR review | Empty |

Example of supplying the API key safely through a GitHub Actions secret:

```yaml
      - name: Run GitHub Activity Lab
        uses: UmeshCode1/lets-connect@v1
        with:
          ai-review: "true"
          anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
          pr-title: ${{ github.event.pull_request.title }}
          pr-body: ${{ github.event.pull_request.body }}
```

Only grant workflow permissions that the consuming workflow needs. The action's current CI workflow uses read-only repository contents permission.

### Action outputs

| Output | Description |
| --- | --- |
| `total-commits` | Number of commits inspected |
| `co-authored-commits` | Number of inspected commits containing co-author metadata |
| `contributors-count` | Distinct contributors found in the inspected commit history |
| `co-authored-percentage` | Percentage of inspected commits containing co-author metadata |
| `compliance-status` | `success` or `failure` based on enabled enforcement options |

## Development and tests

The project uses Python's standard library for its core implementation and `unittest` for automated tests.

Run the test suite from the repository root:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p "test_*.py" -v
```

The CI workflow runs the unit-test suite on Python 3.10, 3.11, 3.12, and 3.13. Test presence does not imply 100% statement or branch coverage; no measured coverage percentage is claimed here.

## Project layout

```text
.
├── .github/
│   └── workflows/       # CI, action tests, and release workflow
├── docs/                # Architecture, workflow, and achievement references
├── src/activity_lab/    # Python package and CLI implementation
├── tests/               # unittest suite
├── action.yml           # GitHub composite action metadata
├── pyproject.toml        # Packaging and CLI entry point
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── LICENSE
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Achievement reference guide](docs/BADGES_GUIDE.md)
- [Collaborative Git workflow](docs/WORKFLOW.md)
- [Contributing guide](CONTRIBUTING.md)
- [Project roadmap](docs/ROADMAP.md)
- [Security policy](.github/SECURITY.md)

## Open-source recognition

The project is listed on the [XERJ Corpus Hub contributor page](https://hub.xerj.org/contributors/UmeshCode1). This is an external project index and recognition listing, not a measure of downloads, active users, or dependent projects.

## Contributing

Contributions, bug reports, and feature requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md), follow the [Code of Conduct](CODE_OF_CONDUCT.md), and include tests for code changes where practical.

## License

Distributed under the [MIT License](LICENSE).
