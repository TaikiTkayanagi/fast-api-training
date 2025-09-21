from pydantic import BaseModel


class Event(BaseModel):
    event_type: str
    data: dict

e = Event(event_type="1", data={"user_id": 123, "timestamp": "2024-10-01T12:00:00Z"})

print(e.event_type)
print(e.data)