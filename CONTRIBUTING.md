# Contributing to GitHub Activity Lab

Thank you for considering a contribution. GitHub Activity Lab is maintained in the open, and useful contributions include bug fixes, tests, documentation improvements, accessibility improvements, and carefully scoped features.

Please read this guide before opening a pull request.

## Start here

1. Read the [README](../README.md) to understand the CLI and GitHub Action.
2. Check [open issues](https://github.com/UmeshCode1/lets-connect/issues) before starting work.
3. For a substantial change, open an issue first so maintainers and contributors can agree on the problem and scope.
4. If you are new to the project, look for issues tagged **good first issue** or **help wanted**. If none are available, ask in an issue which small task would be useful.

Please do not open pull requests solely to create activity. Every contribution should solve a real problem or improve the project for its users.

## Development setup

Requirements:
- Python 3.10 or newer for the currently configured CI matrix. The package metadata declares Python 3.9+; Python 3.9 is not currently included in CI.
- Git for repository-history features.

Clone and install the project in editable mode:

```bash
git clone https://github.com/UmeshCode1/lets-connect.git
cd lets-connect
python -m pip install --upgrade pip
python -m pip install -e .
```

Check the CLI:

```bash
activity-lab --help
```

## Run the tests

Run the complete unit test suite:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The CI workflow currently tests Python 3.10, 3.11, 3.12, and 3.13. Please include focused tests for bug fixes and new behaviour. Prefer deterministic tests that do not require network access, real GitHub credentials, or an Anthropic API key.

For GitHub API code, mock the HTTP boundary rather than making live API calls. For time-dependent calculations, pass an explicit reference time.

## Make a change

Create a focused branch from the latest main branch:

```bash
git switch main
git pull origin main
git switch -c fix/short-description
```

Use a descriptive branch name, for example:
- `fix/parser-trailer-edge-case`
- `feat/api-pagination`
- `docs/clarify-action-setup`

Keep pull requests small and cohesive. Avoid unrelated formatting changes or broad refactors in a bug-fix PR.

## Code expectations

- Preserve the standard-library-first approach unless a dependency is justified and discussed in the issue.
- Keep public CLI behaviour and GitHub Action inputs backward-compatible unless a breaking change is explicitly approved.
- Handle missing credentials, API errors, and unavailable optional integrations gracefully.
- Never log tokens, API keys, private repository data, or other secrets.
- Do not claim that heuristic analysis is equivalent to an LLM review or a security audit.
- Add or update docstrings and user documentation when behaviour changes.
- Use clear names, type hints where they improve clarity, and small functions with focused responsibilities.

## Pull request checklist

Before requesting review:

- [ ] The PR is linked to an issue when one exists.
- [ ] The change solves the issue described and stays within its scope.
- [ ] Tests were added or updated where appropriate.
- [ ] The full unit test suite passes locally.
- [ ] Documentation and examples reflect the actual behaviour.
- [ ] No secrets, credentials, generated files, or unrelated changes are included.
- [ ] The PR description explains the problem, solution, and verification steps.

A maintainer may ask for changes, request a smaller scope, or close a PR that does not align with the project direction. Please keep review discussions respectful and focused on the code.

## Commit messages and co-authorship

Use concise, descriptive commit subjects. Conventional Commit prefixes are welcome, for example:

```text
fix(parser): handle trailer-only commit messages
test(api): cover rate-limit response handling
docs: clarify local development setup
```

Only add a `Co-authored-by:` trailer when another person materially collaborated on that commit. Never add co-author trailers for people who did not contribute.

## Reporting bugs and security issues

Use the repository's bug report template for reproducible defects. Include the command, expected result, actual result, operating system, Python version, and a minimal reproduction when possible.

Do not disclose vulnerabilities in public issues. Follow the private reporting instructions in [SECURITY.md](../.github/SECURITY.md).

## Community and recognition

Contributors are recognised through their meaningful, merged work and with their permission. We do not manufacture commits, co-authorship, stars, downloads, or contributor counts. The project's goal is a healthy, useful tool and a welcoming community—not activity metrics.
