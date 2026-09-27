"""Export utilities — format and write repository stats to CSV, JSON, or table."""

from __future__ import annotations

import csv
import io
import json
from dataclasses import asdict
from typing import Literal

from activity_lab.stats import RepositoryStats


ExportFormat = Literal["table", "csv", "json"]


def _stats_to_records(stats: RepositoryStats) -> list[dict]:
    """Convert RepositoryStats contributors map to a list of flat dicts."""
    records = []
    for key, contributor in stats.contributors.items():
        records.append({
            "email": contributor.email,
            "name": contributor.name,
            "primary_commits": contributor.primary_commits,
            "co_authored_commits": contributor.co_authored_commits,
            "total_contributions": contributor.total_contributions,
        })
    # Sort by total contributions descending
    records.sort(key=lambda r: r["total_contributions"], reverse=True)
    return records


def export_stats(stats: RepositoryStats, fmt: ExportFormat = "table") -> str:
    """Serialize RepositoryStats to the requested format string.

    Args:
        stats: Computed repository statistics.
        fmt:   Output format — 'table', 'csv', or 'json'.

    Returns:
        Formatted string ready for stdout or file write.
    """
    records = _stats_to_records(stats)

    if fmt == "json":
        payload = {
            "summary": {
                "total_commits": stats.total_commits,
                "commits_with_co_authors": stats.commits_with_co_authors,
                "co_authored_percentage": round(stats.co_authored_percentage, 2),
                "unique_contributors": len(stats.contributors),
                "trailers": stats.trailers_distribution,
            },
            "contributors": records,
        }
        return json.dumps(payload, indent=2)

    if fmt == "csv":
        buf = io.StringIO()
        if not records:
            return ""
        writer = csv.DictWriter(buf, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)
        return buf.getvalue()

    # Default: table
    lines = [
        f"{'Name':<30} {'Email':<35} {'Primary':>7} {'Co-Auth':>7} {'Total':>7}",
        "-" * 90,
    ]
    for r in records:
        lines.append(
            f"{r['name']:<30} {r['email']:<35} {r['primary_commits']:>7} "
            f"{r['co_authored_commits']:>7} {r['total_contributions']:>7}"
        )
    lines.append("-" * 90)
    lines.append(
        f"Repository totals: {stats.total_commits} commits, "
        f"{stats.commits_with_co_authors} co-authored "
        f"({stats.co_authored_percentage:.1f}%)"
    )
    return "\n".join(lines)
