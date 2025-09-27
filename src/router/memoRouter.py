from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud import memo as memo_crud 
from model.memo import Memo
from model.status import Status
from schema.request import RequestMemo
from schema.response import ResponseMemo, ResponseMemos
from session import get_session

router = APIRouter()

Session = Annotated[AsyncSession, Depends(get_session)]

@router.get("/memos", response_model=ResponseMemos)
async def read_memos(session: Session):
    memos = await memo_crud.findAll(session)
    return {"memos": memos}

@router.post("/memos", response_model=ResponseMemo)
async def create_memo(request: RequestMemo, session: Session):
    status = Status(is_complete=request.status.is_complete, deadline=request.status.deadline)
    insert = Memo(title=request.title, content=request.content, status=status)
    new_memo = await memo_crud.create(session, insert) 
    return {**new_memo.__dict__, "status": {**new_memo.status.__dict__}}

@router.get("/memos/{memo_id}", response_model=ResponseMemo)
async def read_memo(memo_id: int, session: Session):
    memo = await memo_crud.findById(session, memo_id)
    if memo is None:
        raise HTTPException(status_code=404, detail="Memo not found")
    return memo

@router.put("/memos/{memo_id}", response_model=ResponseMemo)
async def update_memo(memo_id: int, updated_memo: RequestMemo, session: Session):
    memo = await memo_crud.update(session, memo_id, updated_memo.title, updated_memo.content)
    if memo is None:
        raise HTTPException(status_code=404, detail="Memo not found")
    return memo

@router.delete("/memos/{memo_id}", response_model=ResponseMemo)
async def delete_memo(memo_id: int, session: Session):
    memo = await memo_crud.delete(session, memo_id)
    if memo is None:
        raise HTTPException(status_code=404, detail="Memo not found")
    return memo