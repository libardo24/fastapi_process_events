from pydantic import BaseModel

class Event(BaseModel):
    event_id: str
    timestamp: int
    data: str
    category: str
