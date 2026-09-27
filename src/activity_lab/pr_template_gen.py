"""PULL_REQUEST_TEMPLATE.md markdown generator."""
from __future__ import annotations

def generate_pr_template(sections: list[str]) -> str:
    """Build markdown PR template with checklist."""
    out = ["## Description", "<!-- Summary of changes -->", ""]
    for s in sections:
        out.extend([f"## {s}", "- [ ] Verified changes locally", "- [ ] Updated documentation", ""])
    out.extend(["## Co-Authors", "<!-- Add Co-authored-by trailers here -->"])
    return "\n".join(out)
