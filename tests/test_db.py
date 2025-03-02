import asyncpg
from infra.db import create_connection_pool, session_generator
import config


async def test_create_connection_pool():
    pool = await create_connection_pool(config.DSN)
    assert isinstance(pool, asyncpg.pool.Pool)
    await pool.close()


async def test_session_generator():
    pool = await create_connection_pool(config.DSN)
    async with session_generator(pool) as conn:
        assert isinstance(conn, asyncpg.connection.Connection)
    await pool.close()
