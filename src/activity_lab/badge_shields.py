"""Shields.io markdown badge builder."""
from __future__ import annotations
import urllib.parse

def make_shield_badge(label: str, message: str, color: str = "blue") -> str:
    """Construct Shields.io image URL in markdown."""
    clean_label = urllib.parse.quote(label.replace("-", "--"))
    clean_msg = urllib.parse.quote(message.replace("-", "--"))
    url = f"https://img.shields.io/badge/{clean_label}-{clean_msg}-{color}.svg"
    return f"![{label}]({url})"
