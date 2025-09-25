from pydantic import BaseModel

from model.memo import Memo


class MemoResponseSchema(BaseModel):
    memo: Memo