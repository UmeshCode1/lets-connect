# GitHub Activity Lab & Contribution Tracker

[![CI](https://github.com/UmeshCode1/lets-connect/actions/workflows/ci.yml/badge.svg)](https://github.com/UmeshCode1/lets-connect/actions/workflows/ci.yml)
[![Action Test](https://github.com/UmeshCode1/lets-connect/actions/workflows/action-test.yml/badge.svg)](https://github.com/UmeshCode1/lets-connect/actions/workflows/action-test.yml)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Activity--Lab-blue?logo=github-actions&logoColor=white)](https://github.com/marketplace/actions/github-activity-lab-contribution-milestone-tracker)
[![GitHub Developer Program](https://img.shields.io/badge/GitHub-Developer%20Program%20Member-00ff88?logo=github&logoColor=black)](https://github.com/UmeshCode1)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

**GitHub Activity Lab** is a production-grade GitHub Marketplace Action and CLI suite designed to audit repository contributors, validate RFC-compliant Git trailers (`Co-authored-by`), lint Conventional Commits, track achievement milestones, and generate intelligent Claude AI pull request reviews.

---

## ⚡ GitHub Actions Setup

Integrate Activity Lab into your CI/CD pipeline with a single step. It automatically computes repository metrics and publishes an interactive Markdown dashboard directly to `$GITHUB_STEP_SUMMARY`.

Create `.github/workflows/activity-lab.yml`:

```yaml
name: Contributor & Milestone Audit

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run Activity Lab Audit
        uses: UmeshCode1/lets-connect@v1
        with:
          repo-path: '.'
          limit: '50'
          ai-review: 'true'
          pr-title: ${{ github.event.pull_request.title }}
          pr-body: ${{ github.event.pull_request.body }}
          anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Action Configuration

#### Inputs

| Input | Description | Default | Required |
|:------|:------------|:-------:|:--------:|
| `repo-path` | Path to target git repository | `.` | No |
| `limit` | Maximum number of commits to scan | `50` | No |
| `enforce-coauthors` | Fail CI if no co-authored commits are found | `false` | No |
| `enforce-conventional` | Fail CI if commit subjects violate Conventional Commits | `false` | No |
| `ai-review` | Enable AI-assisted PR review & summary generation | `false` | No |
| `pr-title` | Pull request title for automated review | `''` | No |
| `pr-body` | Pull request description | `''` | No |
| `anthropic-api-key` | Anthropic API Key for Claude models (optional) | `''` | No |

#### Outputs

| Output | Description |
|:-------|:------------|
| `total-commits` | Total commits analyzed in current run |
| `co-authored-commits` | Number of commits containing verified co-authors |
| `contributors-count` | Number of unique contributors detected |
| `co-authored-percentage`| Ratio of co-authored commits to total commits |
| `compliance-status` | Execution status (`success` or `failure`) |

---

## 🚀 Key Capabilities

- **🔍 RFC Git Trailer Validation**: Accurately extracts and verifies `Co-authored-by: Name <email>` trailers following Git RFC specifications.
- **🤖 Claude AI PR Reviewer**: Evaluates pull requests for semantic clarity, security risk levels (`LOW`, `MEDIUM`, `HIGH`), suggested co-authors, and commit hygiene using Claude 3.7 / 3.5 Sonnet (with resilient heuristic fallback).
- **📊 Contributor & Pairing Analytics**: Quantifies individual author commits, co-authorship frequencies, and team collaboration ratios.
- **🏆 Milestone Progression Tracking**: Tracks milestones toward official GitHub achievements (*Pair Extraordinaire*, *Pull Shark*, *Galaxy Brain*, *Starstruck*).
- **📝 Automated Step Summaries**: Generates clean, formatted GitHub-flavored markdown tables in GitHub Actions.
- **⚡ Zero External Dependencies**: Runs entirely on the Python standard library with 100% test coverage.

---

## 💻 CLI Quickstart

Install locally in editable mode:

```bash
git clone https://github.com/UmeshCode1/lets-connect.git
cd lets-connect
pip install -e .
```

### Common Commands

* **Run CI/CD audit locally:**
  ```bash
  activity-lab run-action --repo . --limit 25
  ```

* **Review PR with Claude AI:**
  ```bash
  activity-lab ai-review --title "feat(api): add webhook endpoint" --body "Implements HMAC verification"
  ```

* **Inspect contributor statistics:**
  ```bash
  activity-lab stats --repo . --limit 50
  ```

* **Verify commit trailers:**
  ```bash
  activity-lab check-trailers --repo .
  ```

* **Format a valid Co-authored-by trailer:**
  ```bash
  activity-lab format-coauthor --name "Jane Doe" --email "jane@example.com"
  ```

* **View GitHub Achievements & Tier Requirements:**
  ```bash
  activity-lab milestones
  ```

---

## 🧪 Testing

Run the test suite:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 📚 Documentation

- [Architecture & Design](docs/ARCHITECTURE.md)
- [GitHub Achievements Reference & Tiers](docs/BADGES_GUIDE.md)
- [Collaborative Git Workflow](docs/WORKFLOW.md)
- [Contributing Guidelines](CONTRIBUTING.md)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
