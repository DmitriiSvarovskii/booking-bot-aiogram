import datetime
from typing import Annotated, AsyncGenerator, Any
from sqlalchemy import MetaData, text
from sqlalchemy.sql import func
from sqlalchemy.types import JSON
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from sqlalchemy.pool import NullPool
from src.configs.app import settings


metadata = MetaData()


engine = create_async_engine(settings.DB_URL, poolclass=NullPool)
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    type_annotation_map = {
        dict[str, Any]: JSON,
    }


intpk = Annotated[int, mapped_column(primary_key=True, index=True)]

is_active = Annotated[bool, mapped_column(server_default=text("true"))]

created_at = Annotated[datetime.datetime, mapped_column(
    default=func.now())]

updated_at = Annotated[datetime.datetime,
                       mapped_column(server_onupdate=func.now())]
