from datetime import datetime
from pydantic import BaseModel

from model.memo import Memo
class ResponseStatus(BaseModel):
    id: int
    deadline: datetime | None
    is_complete: bool

class ResponseMemo(BaseModel):
    id: int
    title: str
    content: str
    status: ResponseStatus

class ResponseMemos(BaseModel):
    memos: list[ResponseMemo]

