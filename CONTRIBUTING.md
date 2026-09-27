# Contributing to GitHub Activity Lab

Thank you for your interest in contributing to **GitHub Activity & Contribution Laboratory**! We welcome high-quality, legitimate open-source contributions.

## Code of Conduct

All contributors and participants agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Contribution Principles

1. **Authenticity Over Vanity**: We strictly oppose fabricated commits, forged timestamps, fake accounts, or artificial activity spam. Every commit, issue, and pull request must represent meaningful progress or documentation.
2. **Proper Co-Authorship**: If you collaborate with someone, pair program, or review ideas, credit them using standard Git trailers.
3. **Tested Code**: Every bug fix or feature must include unit tests that pass with `python -m unittest`.

---

## Co-Authorship Guidelines

When creating commits with another contributor, add the `Co-authored-by` trailer at the bottom of the commit message.

### Rules for Valid Co-Authorship:
- Separate the commit body and the trailer with at least **one blank line**.
- Use the exact syntax:
  ```text
  Co-authored-by: Name <username@users.noreply.github.com>
  ```
- The email address **must** match a verified email address on the co-author's GitHub account.

### Example Commit:
```text
feat: add stargazer velocity calculation

Calculate how quickly a repository acquires stars over rolling time windows.

Co-authored-by: Alex River <alex@example.com>
```

---

## Development Workflow

1. Fork or branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make clean, atomic commits with informative messages.
3. Run tests locally:
   ```bash
   python -m unittest discover -s tests -p "test_*.py" -v
   ```
4. Push your branch and open a Pull Request against `main`.
5. Address review comments constructively.
