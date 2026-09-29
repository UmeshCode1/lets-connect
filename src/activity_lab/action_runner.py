"""GitHub Action execution runner for Activity Lab.

Orchestrates git trailer verification, contributor analytics, achievement tracking,
and generates step summaries for GitHub Actions CI/CD workflows.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Dict, List, Optional, Tuple

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


from activity_lab.ai_reviewer import review_pull_request
from activity_lab.commit_linter import validate_commit_message
from activity_lab.milestones import ACHIEVEMENT_REGISTRY, Tier
from activity_lab.parser import CommitMetadata, read_git_history
from activity_lab.stats import calculate_stats, RepositoryStats


def evaluate_action(
    repo_path: str = ".",
    limit: int = 50,
    enforce_coauthors: bool = False,
    enforce_conventional: bool = False,
    ai_review: bool = False,
    pr_title: str = "",
    pr_body: str = "",
    api_key: Optional[str] = None,
) -> Tuple[int, str, Dict[str, str]]:
    """Execute action analysis, return (exit_code, markdown_summary, outputs)."""
    commits = read_git_history(repo_path=repo_path, max_count=limit)
    stats: RepositoryStats = calculate_stats(commits) if commits else RepositoryStats()

    # Track conventional commit compliance
    conventional_violations: List[Tuple[str, str]] = []
    coauthor_commits: List[CommitMetadata] = []

    for c in commits:
        if c.has_co_authors:
            coauthor_commits.append(c)
        if not validate_commit_message(c.subject):
            conventional_violations.append((c.sha[:7], c.subject))

    # Determine compliance status
    status = "success"
    exit_code = 0
    failure_reasons: List[str] = []

    if enforce_coauthors and not coauthor_commits:
        status = "failure"
        failure_reasons.append("No valid Co-authored-by trailers found in analyzed commits.")
        exit_code = 1

    if enforce_conventional and conventional_violations:
        status = "failure"
        failure_reasons.append(
            f"{len(conventional_violations)} commit(s) violate Conventional Commits format."
        )
        exit_code = 1

    # Format Markdown Summary
    lines: List[str] = [
        "## 🧪 GitHub Activity Lab - CI/CD Milestone & Compliance Summary",
        "",
        "> Automated contribution audit powered by **[GitHub Activity Lab](https://github.com/UmeshCode1/lets-connect)**.",
        "",
        "### 📊 Contribution Analytics",
        "",
        "| Metric | Value | Status |",
        "|:-------|:-----:|:------:|",
        f"| **Total Commits Analyzed** | `{stats.total_commits}` | ℹ️ |",
        f"| **Commits with Co-Authors** | `{stats.commits_with_co_authors}` | {'✅' if stats.commits_with_co_authors > 0 else '⚪'} |",
        f"| **Co-Authorship Ratio** | `{stats.co_authored_percentage:.1f}%` | {'🎉 Active Pairing' if stats.co_authored_percentage > 0 else 'Single-author'} |",
        f"| **Unique Contributors** | `{len(stats.contributors)}` | 👥 |",
        "",
    ]

    # Contributors Breakdown
    if stats.contributors:
        lines.append("### 👥 Contributors Detected")
        lines.append("")
        lines.append("| Contributor | Primary Author Commits | Co-Authored Commits | Total |")
        lines.append("|:------------|:----------------------:|:-------------------:|:-----:|")
        for email, contrib in sorted(stats.contributors.items(), key=lambda x: x[1].total_contributions, reverse=True):
            lines.append(f"| **{contrib.name}** (`{email}`) | {contrib.primary_commits} | {contrib.co_authored_commits} | **{contrib.total_contributions}** |")
        lines.append("")

    # Achievement Milestone Progress
    lines.append("### 🏆 GitHub Achievement Milestones Tracking")
    lines.append("")
    lines.append("| Achievement | Criteria | Local Progress | Status |")
    lines.append("|:------------|:---------|:--------------:|:------:|")

    # Pair Extraordinaire Progress
    pair_badge = ACHIEVEMENT_REGISTRY.get("pair-extraordinaire")
    bronze_pair = pair_badge.thresholds[Tier.BRONZE] if pair_badge and Tier.BRONZE in pair_badge.thresholds else 10
    pair_status = "🥇 Gold" if stats.commits_with_co_authors >= 48 else "🥈 Silver" if stats.commits_with_co_authors >= 24 else "🥉 Bronze" if stats.commits_with_co_authors >= bronze_pair else "⚡ Default" if stats.commits_with_co_authors >= 1 else "⏳ In Progress"
    lines.append(f"| **Pair Extraordinaire** | Co-authored commits (`Co-authored-by:`) | `{stats.commits_with_co_authors}` / {bronze_pair} | {pair_status} |")

    # Pull Shark Tracking
    lines.append(f"| **Pull Shark** | Merged Pull Requests | PR Workflow | Monitored |")
    lines.append(f"| **Galaxy Brain** | Discussion Accepted Answers | Community Q&A | Monitored |")
    lines.append("")

    # Conventional Commits Check
    if conventional_violations:
        lines.append("### ⚠️ Conventional Commit Linting")
        lines.append("")
        lines.append(f"Found **{len(conventional_violations)}** commit(s) not following `type(scope): subject` syntax:")
        lines.append("")
        for sha, msg in conventional_violations[:5]:
            lines.append(f"- `{sha}`: {msg}")
        if len(conventional_violations) > 5:
            lines.append(f"- *...and {len(conventional_violations) - 5} more*")
        lines.append("")
    else:
        lines.append("### ✅ Conventional Commit Linting")
        lines.append("All analyzed commit titles adhere to Conventional Commits specifications.\n")

    # AI Review Section (if enabled or pr_title provided)
    if ai_review or pr_title:
        commit_msgs = [c.subject for c in commits[:10]]
        ai_res = review_pull_request(
            title=pr_title or (commits[0].subject if commits else "Repository Audit"),
            body=pr_body,
            commit_messages=commit_msgs,
            api_key=api_key,
        )
        lines.append(ai_res.to_markdown())
        lines.append("")

    # Failure Callout if applicable
    if failure_reasons:
        lines.append("> [!CAUTION]")
        for reason in failure_reasons:
            lines.append(f"> - {reason}")
        lines.append("")

    summary_md = "\n".join(lines)

    outputs = {
        "total-commits": str(stats.total_commits),
        "co-authored-commits": str(stats.commits_with_co_authors),
        "contributors-count": str(len(stats.contributors)),
        "co-authored-percentage": f"{stats.co_authored_percentage:.1f}",
        "compliance-status": status,
    }

    return exit_code, summary_md, outputs


def main(argv: Optional[List[str]] = None) -> int:
    """Action runner entry point."""
    parser = argparse.ArgumentParser(description="GitHub Action runner for Activity Lab.")
    parser.add_argument("--repo", default=".", help="Repository path")
    parser.add_argument("--limit", type=int, default=50, help="Max commits to analyze")
    parser.add_argument("--enforce-coauthors", action="store_true", help="Fail if no co-authors")
    parser.add_argument("--enforce-conventional", action="store_true", help="Fail if conventional commits violated")
    parser.add_argument("--ai-review", action="store_true", help="Run Claude AI review")
    parser.add_argument("--pr-title", default="", help="Pull request title")
    parser.add_argument("--pr-body", default="", help="Pull request description")
    parser.add_argument("--api-key", default=None, help="Anthropic API Key")

    args = parser.parse_args(argv)

    exit_code, summary_md, outputs = evaluate_action(
        repo_path=args.repo,
        limit=args.limit,
        enforce_coauthors=args.enforce_coauthors,
        enforce_conventional=args.enforce_conventional,
        ai_review=args.ai_review,
        pr_title=args.pr_title,
        pr_body=args.pr_body,
        api_key=args.api_key,
    )

    # Write to GITHUB_STEP_SUMMARY if available
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        try:
            with open(summary_path, "a", encoding="utf-8") as f:
                f.write(summary_md + "\n")
        except Exception as e:
            print(f"Warning: Could not write GITHUB_STEP_SUMMARY: {e}", file=sys.stderr)

    # Write to GITHUB_OUTPUT if available
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        try:
            with open(output_path, "a", encoding="utf-8") as f:
                for k, v in outputs.items():
                    f.write(f"{k}={v}\n")
        except Exception as e:
            print(f"Warning: Could not write GITHUB_OUTPUT: {e}", file=sys.stderr)

    # Print summary to stdout
    print(summary_md)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
