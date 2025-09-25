from pydantic import BaseModel


class MemoRequestSchema(BaseModel):
    title: str
    content: str