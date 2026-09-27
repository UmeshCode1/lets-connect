"""Contributor statistics and repository analytics."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import List

from activity_lab.parser import CommitMetadata


@dataclass
class ContributorSummary:
    """Metrics for an individual contributor."""
    name: str
    email: str
    primary_commits: int = 0
    co_authored_commits: int = 0

    @property
    def total_contributions(self) -> int:
        return self.primary_commits + self.co_authored_commits


@dataclass
class RepositoryStats:
    """Aggregated statistics across repository commits."""
    total_commits: int
    commits_with_co_authors: int
    contributors: dict[str, ContributorSummary] = field(default_factory=dict)
    trailers_distribution: dict[str, int] = field(default_factory=dict)

    @property
    def co_authored_percentage(self) -> float:
        if self.total_commits == 0:
            return 0.0
        return (self.commits_with_co_authors / self.total_commits) * 100.0


def calculate_stats(commits: list[CommitMetadata]) -> RepositoryStats:
    """Compute aggregate statistics from a list of parsed commits."""
    total_commits = len(commits)
    co_author_commit_count = 0
    contributors_map: dict[str, ContributorSummary] = {}
    trailer_counts: Counter[str] = Counter()

    for commit in commits:
        author_key = commit.author_email.lower().strip() or commit.author_name.lower().strip()
        if author_key not in contributors_map:
            contributors_map[author_key] = ContributorSummary(
                name=commit.author_name,
                email=commit.author_email,
            )
        contributors_map[author_key].primary_commits += 1

        if commit.has_co_authors:
            co_author_commit_count += 1
            for ca in commit.co_authors:
                ca_key = ca.email.lower().strip() or ca.name.lower().strip()
                if ca_key not in contributors_map:
                    contributors_map[ca_key] = ContributorSummary(name=ca.name, email=ca.email)
                contributors_map[ca_key].co_authored_commits += 1

        for trailer_key, values in commit.trailers.items():
            trailer_counts[trailer_key] += len(values)

    return RepositoryStats(
        total_commits=total_commits,
        commits_with_co_authors=co_author_commit_count,
        contributors=contributors_map,
        trailers_distribution=dict(trailer_counts),
    )
