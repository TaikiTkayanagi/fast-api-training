from tkinter import W
from fastapi import APIRouter, HTTPException

from model.memo import Memo
from request.memo_request_schema import MemoRequestSchema
from response.memo_response_schema import MemoResponseSchema
from response.memos_response_schema import MemosResponseSchema

router = APIRouter()

memos: list[Memo] = []

@router.get("/memos")
def read_memos():
    return MemosResponseSchema(memos=memos)

@router.post("/memos")
def create_memo(memo: MemoRequestSchema):
    id = len(memos) + 1
    newMemo = Memo(id=id, title=memo.title, content=memo.content) 
    memos.append(newMemo)
    return MemoResponseSchema(memo=newMemo) 

@router.get("/memos/{memo_id}")
def read_memo(memo_id: int):
    print("read_memo")
    print(memos)
    for memo in memos:
        print(memo)
        if memo.id == memo_id:
            return MemoResponseSchema(memo=memo)
    raise HTTPException(status_code=404, detail="Memo not found")

@router.put("/memos/{memo_id}")
def update_memo(memo_id: int, updated_memo: MemoRequestSchema):
    for memo in memos:
        if memo.id == memo_id:
            memo.title = updated_memo.title
            memo.content = updated_memo.content
            return MemoResponseSchema(memo=memo)
    raise HTTPException(status_code=404, detail="Memo not found")

@router.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    for i, memo in enumerate(memos):
        if memo.id == memo_id:
            delMemo = memos[i]
            del memos[i]
            return MemoResponseSchema(memo=delMemo)
    raise HTTPException(status_code=404, detail="Memo not found")