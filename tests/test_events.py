from app.models.event import Event
from app.services.event_service import filter_future_events, get_latest_event
from datetime import datetime, timezone

def test_filter_future_events():
    now = int(datetime.now(timezone.utc).timestamp())
    events = [
        Event(event_id="1", timestamp=now - 10, data="expired"),
        Event(event_id="2", timestamp=now + 60, data="valid")
    ]
    future = filter_future_events(events)
    assert len(future) == 1
    assert future[0].event_id == "2"

def test_get_latest_event():
    now = int(datetime.now(timezone.utc).timestamp())
    events = [
        Event(event_id="1", timestamp=now + 10, data="a"),
        Event(event_id="2", timestamp=now + 50, data="b"),
    ]
    latest = get_latest_event(events)
    assert latest.event_id == "2"
