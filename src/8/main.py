import asyncio
from sqlalchemy import Column, Integer, Select, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# モデル定義の基底クラスを作成
Base = declarative_base()
engine = create_async_engine("sqlite+aiosqlite:///example.db", echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

# テーブルに対応するクラスを定義


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_user(user: User):
    async with async_session() as session:
        session.add(user)
        await session.commit()


async def get_user(user: User):
    async with async_session() as session:
        result = await session.get(User, user.id)
        return result


async def main():
    await init_db()
    t = User(name="Alice")
    await add_user(t)
    user = await get_user(t)
    if user:
        print(f"Retrieved User: {user.name}")
    await add_user(User(name="Bob"))


if __name__ == "__main__":
    asyncio.run(main())
