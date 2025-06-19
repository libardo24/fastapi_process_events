from typing import List, Optional
from datetime import datetime, timezone
from app.models.event import Event

def filter_future_events(events: List[Event]) -> List[Event]:
    now = int(datetime.now(timezone.utc).timestamp())
    return [e for e in events if e.timestamp >= now]

def get_latest_event(events: List[Event]) -> Optional[Event]:
    if not events:
        return None
    return max(events, key=lambda e: e.timestamp)
