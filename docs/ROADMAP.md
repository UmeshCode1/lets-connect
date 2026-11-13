# Project Roadmap

This roadmap describes candidate priorities for GitHub Activity Lab. It is a planning document, not a promise that every item will ship on a particular date. Priorities may change based on user feedback, maintainer capacity, and technical findings.

## Project direction

Make GitHub Activity Lab a dependable, lightweight toolkit for understanding repository activity and contribution metadata, with a usable CLI and a maintainable GitHub Actions integration.

The project should favour:
- Correct, explainable metrics over vanity scores.
- Small, composable features over a large service architecture.
- Secure handling of tokens and untrusted pull-request input.
- Deterministic tests and clear error messages.
- Compatibility and documentation that make the tool approachable to first-time contributors.

## Near term: reliability and contributor experience

- Expand unit tests around the GitHub API client's success, authentication, HTTP error, network error, and malformed-response paths.
- Decide and document pagination behaviour for collection endpoints such as pull requests and stargazers; avoid silently presenting a first page as a complete repository history.
- Improve CLI validation and error messages for invalid repository paths, missing Git, and invalid owner/repository input.
- Add examples for common workflows and clarify which commands require GitHub credentials or external API access.
- Keep the GitHub Action input/output documentation in sync with `action.yml`.

## Next: analytics correctness and usability

- Document the definitions and limitations of each contribution metric.
- Add fixture-based tests for edge cases in commit parsing, co-author attribution, and timezone/window boundaries.
- Make API rate-limit responses visible and actionable without exposing credentials.
- Review caching behaviour and make cache invalidation and expiry explicit.
- Improve machine-readable report schemas and document their stability expectations.

## Later: integrations and extensibility

- Consider optional exporters or integrations only when there is a concrete user need.
- Evaluate telemetry or webhooks only if a supported service architecture is introduced; the current project is primarily a Python CLI and GitHub Action.
- Explore richer reports after the underlying metrics and API pagination semantics are reliable.

## How to influence the roadmap

Open an issue using the feature-request template. Explain the user problem, current workaround, expected behaviour, and a minimal example. Discussion and evidence from real usage help maintainers prioritise work.

## Current contribution entry points

- **Good first issue:** [Add deterministic unit tests for GitHubApiClient (#94)](https://github.com/UmeshCode1/lets-connect/issues/94). This is a focused, no-network testing task.
- **Enhancement:** [Add explicit pagination for GitHub collection endpoints (#95)](https://github.com/UmeshCode1/lets-connect/issues/95). This is a broader API-client improvement.
- Browse [all open issues](https://github.com/UmeshCode1/lets-connect/issues) and read [CONTRIBUTING.md](../CONTRIBUTING.md) before starting.

If you are new to the project, issue #94 is the recommended first contribution. Comment on the issue before starting so maintainers can coordinate work and answer questions.
