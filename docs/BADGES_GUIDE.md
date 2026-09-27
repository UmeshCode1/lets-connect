# Comprehensive GitHub Achievements Guide

This document specifies the verified operational rules, criteria, and tier thresholds for GitHub Achievements based on current documentation and platform behavior.

---

## 1. Pull Shark

- **Status:** Active, Tiered
- **Tiers:**
  - Default: 2 merged pull requests
  - Bronze: 16 merged pull requests
  - Silver: 128 merged pull requests
  - Gold: 1,024 merged pull requests
- **Eligibility Rules:**
  - Must author the pull request.
  - The pull request must be **merged** into the repository's default branch.
  - The repository must be **public**. Activity in private repositories is not recognized by GitHub's achievement pipeline.
  - Self-merging into an unprotected branch is permitted.

---

## 2. Pair Extraordinaire

- **Status:** Active, Tiered
- **Tiers:**
  - Default: 1 co-authored merged pull request
  - Bronze: 10 co-authored merged pull requests
  - Silver: 24 co-authored merged pull requests
  - Gold: 48 co-authored merged pull requests
- **Eligibility Rules:**
  - A commit within the merged pull request must feature a valid `Co-authored-by` trailer.
  - The email specified in the trailer must be associated with a verified GitHub account.
  - When the PR is merged into a public repository, both the primary commit author and the credited co-author qualify for credit.

---

## 3. Starstruck

- **Status:** Active, Tiered
- **Tiers:**
  - Default: 16 stars on a single repository
  - Bronze: 128 stars
  - Silver: 512 stars
  - Gold: 4,096 stars
- **Eligibility Rules:**
  - Evaluated on a **single** repository owned by the user (stars across different repositories are not cumulative).
  - Must be a **public** repository.
  - Stargazers must be genuine user accounts; automated or bot accounts are detected and removed by GitHub's abuse prevention systems.

---

## 4. Galaxy Brain

- **Status:** Active, Tiered
- **Tiers:**
  - Default: 2 accepted answers
  - Bronze: 8 accepted answers
  - Silver: 16 accepted answers
  - Gold: 32 accepted answers
- **Eligibility Rules:**
  - Requires active GitHub Discussions with the "Q&A" format enabled in a public repository.
  - The discussion creator or repository maintainer must click "Mark as answer".
  - **Self-acceptance is disqualified**: Accepting your own reply to your own question does not count toward the achievement.
  - Discussions in the official `github/community` meta-forum have badge awards disabled. Contributions must occur in standard public project repositories.

---

## 5. Quickdraw

- **Status:** Active, Non-tiered (One-time)
- **Eligibility Rules:**
  - Close an issue or pull request within 5 minutes (300 seconds) of its creation.
  - Must occur in a public repository.

---

## 6. YOLO

- **Status:** Active, Non-tiered (One-time)
- **Eligibility Rules:**
  - Merge a pull request into a branch without submitting or requesting code reviews.
  - Branch protection rules requiring review approvals must be disabled.
  - Must occur in a public repository.

---

## 7. Public Sponsor

- **Status:** Active, Non-tiered (One-time)
- **Eligibility Rules:**
  - Sponsor an open-source maintainer, organization, or developer via GitHub Sponsors.
  - The sponsorship privacy setting must be set to "Public".

---

## 8. Retired / Experimental Badges

### Heart on Your Sleeve
- **Status:** Retired / Unreleased.
- Associated with reacting with ❤️ emojis during an experimental GitHub trial in 2022. It was never released to general users and is not currently earnable.

### Open Sourcerer
- **Status:** Retired / Unreleased.
- Associated with merging PRs across multiple distinct public repositories during an internal GitHub test in 2022. It is not currently active or earnable.
