# Collaborative Git & GitHub Workflow

This guide details the exact Git branch and pull request workflow for contributing to the `github-activity-lab` repository.

## Branch Strategy

The repository follows a trunk-based feature branch model:

```text
main (stable release)
 ├── feature/readme             -> Project presentation & badges
 ├── feature/github-api         -> REST API client implementation
 ├── feature/activity-parser    -> Commit trailer parsing engine
 ├── feature/contributor-stats  -> Analytics & aggregation module
 ├── feature/milestones         -> Achievement milestone registry
 ├── docs/guides                -> Architecture, workflows, and badge guides
 └── feature/ci                 -> GitHub Actions CI automation
```

## Step-by-Step Feature Lifecycle

### 1. Create a Branch
Always branch from an updated `main`:
```bash
git checkout main
git checkout -b feature/activity-parser
```

### 2. Implement Code & Tests
Write modular code in `src/activity_lab/` and companion unit tests in `tests/`.

### 3. Commit with Co-Authors (When Collaborating)
Ensure your commit adheres to RFC trailer formatting:
```bash
git commit -m "feat: add support for multiple co-authors

Support multiple co-authors in a single commit message.

Co-authored-by: Collaborator Name <collaborator@example.com>"
```

### 4. Run Local Test Suite
Ensure all tests pass before proposing changes:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 5. Open Pull Request
Push your branch to GitHub and open a Pull Request using the PR template.
Specify:
- Summary of changes
- Motivation and context
- Verification steps completed

### 6. Code Review & Merge
Request a review from a collaborator or team member. Once checks pass and the review is approved, merge the pull request.
