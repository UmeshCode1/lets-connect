"""SECURITY.md vulnerability disclosure policy generator."""
from __future__ import annotations

def generate_security_policy(project_name: str, contact_email: str) -> str:
    """Create standardized SECURITY.md policy."""
    return f"""# Security Policy

## Supported Versions
| Version | Supported |
| ------- | --------- |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability
Please report vulnerabilities privately by emailing `{contact_email}` before public disclosure.
"""
