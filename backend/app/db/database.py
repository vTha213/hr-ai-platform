from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy.engine import make_url

from app.core.config import settings

url = make_url(settings.DATABASE_URL)

query = dict(url.query)

if "sslmode" in query:
    query.pop("sslmode")
    query["ssl"] = "require"

url = url.set(query=query)

engine = create_async_engine(
    url,
    echo=False,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session