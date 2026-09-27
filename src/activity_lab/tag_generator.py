"""Release tag generator with standard v-prefix."""
from __future__ import annotations

def format_release_tag(major: int, minor: int, patch: int, prerelease: str = "") -> str:
    """Construct semantic tag string."""
    tag = f"v{major}.{minor}.{patch}"
    if prerelease:
        tag += f"-{prerelease}"
    return tag
