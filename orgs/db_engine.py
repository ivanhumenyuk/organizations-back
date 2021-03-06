from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from orgs.config import dev_config

DATABASE_URL = f"postgresql+asyncpg://{dev_config.get('POSTGRES_USER')}:" \
               f"{dev_config.get('POSTGRES_PW')}" \
               f"@{dev_config.get('POSTGRES_URL')}/" \
               f"{dev_config.get('POSTGRES_DB')}"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base(bind=engine)
