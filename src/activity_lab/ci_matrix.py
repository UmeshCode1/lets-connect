"""GitHub Actions testing matrix generator."""
from __future__ import annotations
from typing import List, Dict, Any

def build_test_matrix(python_versions: List[str], os_list: List[str]) -> Dict[str, Any]:
    """Build matrix dictionary for workflow generation."""
    return {
        "strategy": {
            "matrix": {
                "python-version": python_versions,
                "os": os_list,
            }
        }
    }
