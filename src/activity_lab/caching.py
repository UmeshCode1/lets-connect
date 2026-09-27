"""TTL-based response cache for GitHub API queries."""
from __future__ import annotations
import time
from typing import Any, Dict, Optional, Tuple

class CacheStore:
    def __init__(self, default_ttl: int = 300):
        self._store: Dict[str, Tuple[Any, float]] = {}
        self.default_ttl = default_ttl

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        expiry = time.time() + (ttl or self.default_ttl)
        self._store[key] = (value, expiry)

    def get(self, key: str) -> Optional[Any]:
        if key not in self._store:
            return None
        val, expiry = self._store[key]
        if time.time() > expiry:
            del self._store[key]
            return None
        return val
