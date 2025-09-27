from datetime import datetime
from pydantic import BaseModel

class RequestStatus(BaseModel):
    deadline: datetime | None = None
    is_complete: bool

class RequestMemo(BaseModel):
    title: str
    content: str
    status: RequestStatus

