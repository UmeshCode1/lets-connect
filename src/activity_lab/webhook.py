"""GitHub Webhook event validation and dispatching."""
from __future__ import annotations
from typing import Dict, Any

def route_webhook_event(event_type: str, payload: Dict[str, Any]) -> str:
    """Route webhook event to action description."""
    if event_type == "pull_request":
        action = payload.get("action", "unknown")
        pr_num = payload.get("number", "?")
        return f"PR #{pr_num} {action}"
    elif event_type == "push":
        ref = payload.get("ref", "unknown")
        commits = len(payload.get("commits", []))
        return f"Pushed {commits} commits to {ref}"
    return f"Unhandled event: {event_type}"
