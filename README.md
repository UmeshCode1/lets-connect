# GitHub Activity & Contribution Laboratory (activity-lab)

[![CI](https://github.com/UmeshCode1/bages-/actions/workflows/ci.yml/badge.svg)](https://github.com/UmeshCode1/bages-/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

**GitHub Activity & Contribution Laboratory** is an open-source research and engineering toolkit designed to parse Git commit metadata, track contributor statistics, validate RFC-compliant Git trailers (including `Co-authored-by`), and calculate milestone progression toward legitimate GitHub achievements.

Rather than being an artificial badge generator, this repository acts as a real, structured development laboratory for best-practice open-source collaboration, pull request review workflows, and contributor analytics.

---

## Features

- 🔍 **Git Trailer & Co-Author Parser**: Automatically identifies and validates `Co-authored-by`, `Signed-off-by`, and issue references according to Git RFC trailer specifications.
- 📊 **Contributor Statistics**: Analyzes local and remote repository history, breaking down commits by primary author, co-authorship percentages, and trailer frequencies.
- 🎯 **Milestone & Achievement Tracker**: Programmatically tracks official GitHub achievement requirements (Pull Shark, Pair Extraordinaire, Galaxy Brain, Starstruck, YOLO, Quickdraw, Public Sponsor) and calculates remaining targets for each tier (Default, Bronze, Silver, Gold).
- 🌐 **Lightweight GitHub API Client**: Zero-dependency standard library client for querying repository metadata, pull requests, and stargazers.
- 🧪 **Comprehensive Test Suite**: 100% test coverage using standard library `unittest` across Python 3.9 through 3.14.

---

## Quickstart

### Installation (Local)

Clone the repository and install in editable mode:

```bash
git clone https://github.com/UmeshCode1/bages-.git
cd bages-
pip install -e .
```

### CLI Usage

1. **Inspect Contributor Analytics:**
   ```bash
   activity-lab stats --repo . --limit 50
   ```

2. **Verify Co-Authorship Trailers:**
   ```bash
   activity-lab check-trailers --repo .
   ```

3. **View Official GitHub Achievements & Tier Requirements:**
   ```bash
   activity-lab milestones
   ```

4. **Generate a RFC Co-Authored-By Trailer:**
   ```bash
   activity-lab format-coauthor --name "Jane Doe" --email "jane@example.com"
   ```

---

## GitHub Achievements Reference

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

## Documentation

- [Architecture & Design](docs/ARCHITECTURE.md)
- [Comprehensive Badges & Milestone Guide](docs/BADGES_GUIDE.md)
- [Collaborative Git Workflow](docs/WORKFLOW.md)
- [Contributing Guidelines](CONTRIBUTING.md)

---

## Running Tests

Run the unit test suite without installing external dependencies:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
