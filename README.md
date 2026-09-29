# GitHub Activity & Contribution Laboratory (activity-lab)

[![CI](https://github.com/UmeshCode1/lets-connect/actions/workflows/ci.yml/badge.svg)](https://github.com/UmeshCode1/lets-connect/actions/workflows/ci.yml)
[![Action Test](https://github.com/UmeshCode1/lets-connect/actions/workflows/action-test.yml/badge.svg)](https://github.com/UmeshCode1/lets-connect/actions/workflows/action-test.yml)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Activity--Lab-blue?logo=github-actions&logoColor=white)](https://github.com/marketplace/actions/github-activity-lab-contribution-milestone-tracker)
[![GitHub Developer Program](https://img.shields.io/badge/GitHub-Developer%20Program%20Member-00ff88?logo=github&logoColor=black)](https://github.com/UmeshCode1)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

**GitHub Activity & Contribution Laboratory** is an open-source research and engineering toolkit, reusable **GitHub Marketplace Action**, and **Claude AI PR reviewer** designed to parse Git commit metadata, track contributor statistics, validate RFC-compliant Git trailers (including `Co-authored-by`), and calculate milestone progression toward legitimate GitHub achievements.

Rather than being an artificial badge generator, this repository acts as a real, structured development laboratory for best-practice open-source collaboration, pull request review workflows, and contributor analytics.

---

## ⚡ GitHub Actions Integration (Marketplace Action)

You can run `activity-lab` directly in any GitHub repository to automate contributor audits, validate Conventional Commits, enforce `Co-authored-by` trailer standards, and post rich Markdown summaries to `$GITHUB_STEP_SUMMARY`.

Add this workflow to `.github/workflows/activity-lab.yml`:

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
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run Activity Lab Audit
        uses: UmeshCode1/lets-connect@v1
        with:
          repo-path: '.'
          limit: '50'
          enforce-coauthors: 'false'
          enforce-conventional: 'false'
          ai-review: 'true'
          pr-title: ${{ github.event.pull_request.title }}
          pr-body: ${{ github.event.pull_request.body }}
          anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Action Inputs & Outputs

| Input | Description | Default |
|:------|:------------|:-------:|
| `repo-path` | Path to git repository root | `.` |
| `limit` | Maximum number of recent commits to analyze | `50` |
| `enforce-coauthors` | Fail CI if no co-authored commits exist | `false` |
| `enforce-conventional` | Fail CI if commit titles violate Conventional Commits | `false` |
| `ai-review` | Enable Claude AI PR review analysis | `false` |
| `pr-title` | Pull request title for automated review | `''` |
| `pr-body` | Pull request description | `''` |
| `anthropic-api-key` | Optional Anthropic API Key for Claude 3.7 / 3.5 Sonnet | `''` |

---

## 🚀 Features

- 🔍 **Git Trailer & Co-Author Parser**: Automatically identifies and validates `Co-authored-by`, `Signed-off-by`, and issue references according to Git RFC trailer specifications.
- 🤖 **Claude AI PR Reviewer**: Analyzes pull request titles, descriptions, and diffs using Anthropic Claude models (or zero-dependency heuristics) to assess risk, suggest co-authors, and verify Conventional Commits.
- 📊 **Contributor Statistics**: Analyzes local and remote repository history, breaking down commits by primary author, co-authorship percentages, and trailer frequencies.
- 🎯 **Milestone & Achievement Tracker**: Programmatically tracks official GitHub achievement requirements (Pull Shark, Pair Extraordinaire, Galaxy Brain, Starstruck, YOLO, Quickdraw, Public Sponsor) and calculates remaining targets for each tier (Default, Bronze, Silver, Gold).
- 📦 **Turnkey CI/CD Action**: Native GitHub Action composite runner that writes rich step summaries directly into workflow runs.
- 🌐 **Lightweight GitHub API Client**: Zero-dependency standard library client for querying repository metadata, pull requests, and stargazers.
- 🧪 **Comprehensive Test Suite**: 100% test coverage using standard library `unittest` across Python 3.9 through 3.14.

---

## 💻 CLI Quickstart

### Installation (Local)

Clone the repository and install in editable mode:

```bash
git clone https://github.com/UmeshCode1/lets-connect.git
cd lets-connect
pip install -e .
```

### CLI Commands

1. **Inspect Contributor Analytics:**
   ```bash
   activity-lab stats --repo . --limit 50
   ```

2. **Run Local CI/CD Contribution Audit:**
   ```bash
   activity-lab run-action --repo . --limit 25
   ```

3. **Verify Co-Authorship Trailers:**
   ```bash
   activity-lab check-trailers --repo .
   ```

4. **Claude AI Pull Request Review:**
   ```bash
   activity-lab ai-review --title "feat(ci): add composite action runner" --body "Automates contributor audits"
   ```

5. **View Official GitHub Achievements & Tier Requirements:**
   ```bash
   activity-lab milestones
   ```

6. **Generate an RFC Co-Authored-By Trailer:**
   ```bash
   activity-lab format-coauthor --name "Jane Doe" --email "jane@example.com"
   ```

7. **Analyze Stargazer Velocity & Projections:**
   ```bash
   activity-lab star-velocity --owner UmeshCode1 --repo lets-connect
   ```

---

## 🏆 GitHub Achievements Reference

| Achievement | Tiered | Default Requirement | Bronze | Silver | Gold | Legitimacy Notes |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Pull Shark** | Yes | 2 merged PRs | 16 PRs | 128 PRs | 1,024 PRs | Author own PRs merged into public repository |
| **Pair Extraordinaire** | Yes | 1 co-authored PR | 10 PRs | 24 PRs | 48 PRs | Valid `Co-authored-by:` trailer in commit |
| **Starstruck** | Yes | 16 stars | 128 stars | 512 stars | 4,096 stars | On a single public repository from real users |
| **Galaxy Brain** | Yes | 2 accepted answers | 8 answers | 16 answers | 32 answers | In public repo Discussions Q&A (non-self) |
| **Quickdraw** | No | 1 event | — | — | — | Close Issue/PR within 5 minutes of creation |
| **YOLO** | No | 1 event | — | — | — | Merge PR without reviews on unprotected branch |
| **Public Sponsor** | No | 1 sponsorship | — | — | — | Publicly sponsor via GitHub Sponsors |

*Note: Achievements like **Heart on Your Sleeve** and **Open Sourcerer** were internal/experimental trial badges that are retired and not earnable.*

---

## 📚 Documentation

- [Architecture & Design](docs/ARCHITECTURE.md)
- [Comprehensive Badges & Milestone Guide](docs/BADGES_GUIDE.md)
- [Collaborative Git Workflow](docs/WORKFLOW.md)
- [Contributing Guidelines](CONTRIBUTING.md)

---

## 🧪 Running Tests

Run the full unit test suite without installing external dependencies:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
