"""SPDX license key identifier."""
from __future__ import annotations

KNOWN_LICENSES = {
    "mit": "MIT License",
    "apache-2.0": "Apache License 2.0",
    "gpl-3.0": "GNU General Public License v3.0",
    "bsd-3-clause": "BSD 3-Clause License",
}

def identify_license(spdx_key: str) -> str:
    """Return full human-readable license name for an SPDX key."""
    return KNOWN_LICENSES.get(spdx_key.strip().lower(), "Custom / Proprietary")
