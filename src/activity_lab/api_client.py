"""Lightweight GitHub API client using standard library urllib."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional


class GitHubApiClient:
    """Client for querying GitHub REST API endpoints with optional authentication."""

    BASE_URL = "https://api.github.com"

    def __init__(self, token: Optional[str] = None):
        self.token = token or os.environ.get("GITHUB_TOKEN")

    def _get_headers(self) -> dict[str, str]:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "github-activity-lab",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def get_repo(self, owner: str, repo: str) -> dict[str, Any]:
        """Fetch repository details."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        return self._request(url)

    def get_pull_requests(self, owner: str, repo: str, state: str = "all") -> list[dict[str, Any]]:
        """Fetch pull requests for a repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/pulls?state={state}&per_page=100"
        res = self._request(url)
        return res if isinstance(res, list) else []

    def get_stargazers(self, owner: str, repo: str) -> list[dict[str, Any]]:
        """Fetch stargazers for a repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/stargazers?per_page=100"
        res = self._request(url)
        return res if isinstance(res, list) else []

    def _request(self, url: str) -> Any:
        req = urllib.request.Request(url, headers=self._get_headers())
        try:
            with urllib.request.urlopen(req) as resp:
                content = resp.read().decode("utf-8")
                return json.loads(content)
        except urllib.error.HTTPError as e:
            return {"error": str(e), "code": e.code}
        except urllib.error.URLError as e:
            return {"error": str(e)}
