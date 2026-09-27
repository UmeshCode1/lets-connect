"""Git commit and trailer parser module."""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


# Regex for Co-authored-by trailer matching GitHub's specification:
# Co-authored-by: Name <email@example.com>
CO_AUTHORED_BY_PATTERN = re.compile(
    r"^Co-authored-by:\s*(?P<name>[^<]+?)\s*<(?P<email>[^>]+)>\s*$",
    re.IGNORECASE,
)

GENERIC_TRAILER_PATTERN = re.compile(
    r"^(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.+)$"
)


@dataclass
class CoAuthor:
    """Represents a co-author on a commit."""
    name: str
    email: str

    def format_trailer(self) -> str:
        """Format as a standard Git trailer line."""
        return f"Co-authored-by: {self.name} <{self.email}>"


@dataclass
class CommitMetadata:
    """Structured information parsed from a Git commit."""
    sha: str
    author_name: str
    author_email: str
    subject: str
    body: str
    trailers: dict[str, list[str]] = field(default_factory=dict)
    co_authors: list[CoAuthor] = field(default_factory=list)

    @property
    def has_co_authors(self) -> bool:
        """Return True if commit contains at least one co-author."""
        return len(self.co_authors) > 0


def parse_commit_message(raw_message: str, sha: str = "", author_name: str = "", author_email: str = "") -> CommitMetadata:
    """Parse a commit message string and extract subject, body, trailers, and co-authors."""
    raw_message = raw_message.strip()
    if not raw_message:
        return CommitMetadata(sha=sha, author_name=author_name, author_email=author_email, subject="", body="")

    lines = raw_message.splitlines()
    subject = lines[0].strip()
    body_lines = lines[1:] if len(lines) > 1 else []
    body = "\n".join(body_lines).strip()

    trailers: dict[str, list[str]] = {}
    co_authors: list[CoAuthor] = []

    # Git trailers reside in the final paragraph/block of the commit message
    # Separate message into paragraphs by double newlines
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", raw_message) if p.strip()]

    # If there are multiple paragraphs, the last paragraph is inspected for trailers
    candidate_lines = paragraphs[-1].splitlines() if len(paragraphs) > 1 else []

    # Check if lines in the candidate block are trailers
    for line in candidate_lines:
        line_clean = line.strip()
        co_match = CO_AUTHORED_BY_PATTERN.match(line_clean)
        if co_match:
            co_author = CoAuthor(
                name=co_match.group("name").strip(),
                email=co_match.group("email").strip(),
            )
            co_authors.append(co_author)
            trailers.setdefault("Co-authored-by", []).append(f"{co_author.name} <{co_author.email}>")
            continue

        trailer_match = GENERIC_TRAILER_PATTERN.match(line_clean)
        if trailer_match:
            key = trailer_match.group("key").strip()
            val = trailer_match.group("value").strip()
            trailers.setdefault(key, []).append(val)

    return CommitMetadata(
        sha=sha,
        author_name=author_name,
        author_email=author_email,
        subject=subject,
        body=body,
        trailers=trailers,
        co_authors=co_authors,
    )


def read_git_history(repo_path: str = ".", max_count: int = 100) -> list[CommitMetadata]:
    """Read commit history from a local git repository using git log with custom formatting."""
    sep = "---GIT_COMMIT_SEPARATOR---"
    cmd = [
        "git",
        "-C",
        repo_path,
        "log",
        f"-n{max_count}",
        f"--format=%H%x1f%an%x1f%ae%x1f%B%x1e{sep}",
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        raw_output = proc.stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []

    commits: list[CommitMetadata] = []
    chunks = raw_output.split(sep)
    for chunk in chunks:
        chunk = chunk.strip("\n\r\x1e ")
        if not chunk:
            continue
        parts = chunk.split("\x1f")
        if len(parts) >= 4:
            sha, author, email, msg = parts[0], parts[1], parts[2], parts[3]
            commits.append(parse_commit_message(msg, sha=sha, author_name=author, author_email=email))
    return commits
