"""Command-line interface for GitHub Activity & Contribution Laboratory."""

from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional

from activity_lab.milestones import ACHIEVEMENT_REGISTRY, Tier
from activity_lab.parser import CoAuthor, read_git_history
from activity_lab.stats import calculate_stats


def cmd_stats(args: argparse.Namespace) -> int:
    """Analyze local git repository commits and output contributor statistics."""
    commits = read_git_history(repo_path=args.repo, max_count=args.limit)
    if not commits:
        print(f"No commits found in repository at '{args.repo}'.")
        return 0

    stats = calculate_stats(commits)
    print("=" * 60)
    print(" GitHub Activity Lab - Contributor & Commit Analytics")
    print("=" * 60)
    print(f"Total commits analyzed:        {stats.total_commits}")
    print(f"Commits with co-authors:       {stats.commits_with_co_authors} ({stats.co_authored_percentage:.1f}%)")
    print(f"Unique contributors detected:  {len(stats.contributors)}")
    print("-" * 60)
    print("Contributors breakdown:")
    for email, contributor in sorted(stats.contributors.items(), key=lambda x: x[1].total_contributions, reverse=True):
        print(f" • {contributor.name} <{contributor.email}>: "
              f"{contributor.primary_commits} author commits, "
              f"{contributor.co_authored_commits} co-authored")
    print("-" * 60)
    if stats.trailers_distribution:
        print("Git trailers found:")
        for trailer, count in sorted(stats.trailers_distribution.items()):
            print(f" • {trailer}: {count}")
    print("=" * 60)
    return 0


def cmd_check_trailers(args: argparse.Namespace) -> int:
    """Check commits in git log for valid RFC Git trailers and co-authors."""
    commits = read_git_history(repo_path=args.repo, max_count=args.limit)
    if not commits:
        print(f"No commits found in '{args.repo}'.")
        return 0

    co_authored_found = 0
    print(f"Inspecting last {len(commits)} commits for valid trailers...\n")
    for commit in commits:
        if commit.has_co_authors:
            co_authored_found += 1
            print(f"✓ Commit {commit.sha[:8]} - '{commit.subject}'")
            for ca in commit.co_authors:
                print(f"   Co-Author: {ca.name} <{ca.email}>")
    print(f"\nSummary: {co_authored_found} of {len(commits)} commits contain valid co-authorship metadata.")
    return 0


def cmd_milestones(args: argparse.Namespace) -> int:
    """Display registry of official GitHub Achievements, tiers, and criteria."""
    print("=" * 70)
    print(" GitHub Official Achievements & Milestone Tiers")
    print("=" * 70)
    for slug, badge in ACHIEVEMENT_REGISTRY.items():
        status = "ACTIVE" if badge.is_active else "RETIRED/UNRELEASED"
        public_req = "Public Repo Only" if badge.requires_public_repo else "Any / Profile Level"
        peer_req = "Requires Peer" if badge.requires_peer else "Solo Feasible"

        print(f"\n[{status}] {badge.display_name} ({slug})")
        print(f"  Description: {badge.description}")
        print(f"  Conditions:  {public_req} | {peer_req}")

        if badge.thresholds:
            tiers_str = " | ".join(f"{t.value}: {count}" for t, count in badge.thresholds.items())
            print(f"  Tiers:       {tiers_str}")
        else:
            print("  Tiers:       N/A (Not currently earnable)")
    print("\n" + "=" * 70)
    return 0


def cmd_format_coauthor(args: argparse.Namespace) -> int:
    """Generate properly formatted Co-authored-by trailer."""
    co = CoAuthor(name=args.name, email=args.email)
    print("\nGenerated Git Trailer (paste at end of commit message after a blank line):")
    print("-" * 50)
    print(co.format_trailer())
    print("-" * 50)
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="activity-lab",
        description="GitHub Activity & Contribution Laboratory CLI",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # stats
    p_stats = subparsers.add_parser("stats", help="Compute repository contributor statistics")
    p_stats.add_argument("--repo", default=".", help="Path to Git repository (default: current dir)")
    p_stats.add_argument("--limit", type=int, default=100, help="Maximum number of commits to scan")
    p_stats.set_defaults(func=cmd_stats)

    # check-trailers
    p_trailers = subparsers.add_parser("check-trailers", help="Verify Co-authored-by trailers in commits")
    p_trailers.add_argument("--repo", default=".", help="Path to Git repository (default: current dir)")
    p_trailers.add_argument("--limit", type=int, default=100, help="Number of commits to check")
    p_trailers.set_defaults(func=cmd_check_trailers)

    # milestones
    p_milestones = subparsers.add_parser("milestones", help="Show achievement milestone rules and tier requirements")
    p_milestones.set_defaults(func=cmd_milestones)

    # format-coauthor
    p_coauthor = subparsers.add_parser("format-coauthor", help="Format standard Co-authored-by trailer")
    p_coauthor.add_argument("--name", required=True, help="Collaborator's full name or GitHub display name")
    p_coauthor.add_argument("--email", required=True, help="Collaborator's verified GitHub email")
    p_coauthor.set_defaults(func=cmd_format_coauthor)

    parsed = parser.parse_args(argv)
    return parsed.func(parsed)


if __name__ == "__main__":
    sys.exit(main())
