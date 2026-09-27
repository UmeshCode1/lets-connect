"""JSON Activity feed serializer."""
from __future__ import annotations
import json
from typing import List, Dict, Any

def serialize_feed(events: List[Dict[str, Any]]) -> str:
    """Format activity events into standard JSON feed."""
    feed = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": "Activity Lab Feed",
        "items": events,
    }
    return json.dumps(feed, indent=2)
