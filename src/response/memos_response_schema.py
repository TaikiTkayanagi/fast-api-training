
from pydantic import BaseModel
from model.memo import Memo


class MemosResponseSchema(BaseModel):
    memos: list[Memo]