"""Terminal UI dashboard formatter."""
from __future__ import annotations
from typing import Dict, Any

def render_dashboard(metrics: Dict[str, Any]) -> str:
    """Render comprehensive terminal dashboard view."""
    border = "=" * 60
    return f"""{border}
  GitHub Activity Lab - Unified Analytics Dashboard
{border}
  Total Commits:      {metrics.get('commits', 0)}
  Merged PRs:         {metrics.get('prs', 0)}
  Total Badges:       {metrics.get('badges', 0)}
  Gold Thresholds:    {metrics.get('gold_unlocked', 0)} Unlocked
{border}"""
