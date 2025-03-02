from contextlib import asynccontextmanager
import config
import asyncpg
from typing import AsyncGenerator


async def create_connection_pool(dsn: str) -> asyncpg.pool.Pool:
    """Создаёт пул соединений с базой данных."""
    return await asyncpg.pool.create_pool(dsn)


@asynccontextmanager
async def session_generator(
    pool: asyncpg.pool.Pool,
) -> AsyncGenerator[asyncpg.connection.Connection, None]:
    """Создаёт соединение с базой данных"""
    async with pool.acquire() as conn:
        yield conn


async def create_database_if_not_exists(db_name: str) -> None:
    """Проверяет существование базы данных и создаёт её, если она не существует."""
    conn = await asyncpg.connection.connect(
        host=config.DB_HOST,
        password=config.DB_PASSWORD,
        user=config.DB_USER,
        port=config.DB_PORT,
    )
    try:
        databases = await conn.fetch("SELECT datname FROM pg_database")
        if not any(db["datname"] == db_name for db in databases):
            await conn.execute(f"CREATE DATABASE {db_name}")
    finally:
        await conn.close()
