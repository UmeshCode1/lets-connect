"""Structured JSONL activity audit logger."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from typing import Dict, Any

def create_audit_entry(action: str, actor: str, metadata: Dict[str, Any]) -> str:
    """Format single audit log line."""
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "actor": actor,
        "metadata": metadata
    }
    return json.dumps(record)
