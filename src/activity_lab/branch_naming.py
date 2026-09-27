"""Git branch naming policy evaluator."""
from __future__ import annotations
import re

BRANCH_PATTERN = re.compile(r"^(feature|bugfix|hotfix|release|chore)/[a-z0-9\-]+$")

def is_valid_branch_name(branch: str) -> bool:
    """Check if branch matches git-flow naming standards."""
    return bool(BRANCH_PATTERN.match(branch.strip()))
