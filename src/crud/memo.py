from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from model.memo import Memo

async def findAll(session: AsyncSession) -> list[Memo]:
    result = await session.execute(
        select(Memo).options(selectinload(Memo.status))
    )
    return list(result.scalars().all())

async def findById(session: AsyncSession, memo_id: int) -> Memo | None:
    result = await session.execute(select(Memo).where(Memo.id == memo_id).options(selectinload(Memo.status)))
    return result.scalars().first()

async def create(session: AsyncSession, new_memo: Memo) -> Memo:
    session.add(new_memo)
    await session.commit()
    await session.refresh(new_memo)
    return new_memo

async def update(session: AsyncSession, memo_id: int, title: str, content: str) -> Memo | None:
    memo = await findById(session, memo_id)
    if memo is None:
        return None
    memo.title = title
    memo.content = content
    await session.commit()
    await session.refresh(memo)
    return memo

async def delete(session: AsyncSession, memo_id: int) -> Memo | None:
    memo = await findById(session, memo_id)
    if memo is None:
        return None
    await session.delete(memo)
    await session.commit()
    return memo