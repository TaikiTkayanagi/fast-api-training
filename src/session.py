from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

engine = create_async_engine("sqlite+aiosqlite:///memo.db", echo=True)
session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with session() as s:
        yield s


async def init_db():
    async with engine.begin() as conn:
        from model.memo import Base
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
