import config
from db import session_generator
import json
import asyncpg


class EmployeeService:
    def __init__(self, pool):
        self.pool = pool

    async def create_database_if_not_exists(
        self, conn: asyncpg.connection.Connection, db_name: str
    ) -> None:
        """Проверяет существование базы данных и создаёт её, если она не существует."""
        databases = await conn.fetch("SELECT datname FROM pg_database")
        if not any(db["datname"] == db_name for db in databases):
            await conn.execute(f"CREATE DATABASE {db_name}")

    async def create_table_if_not_exists(
        self, conn: asyncpg.connection.Connection
    ) -> None:
        """Создаёт таблицу 'organization', если она не существует."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS organization (
            Id INT PRIMARY KEY,
            ParentId INT,
            Name TEXT,
            Type INT
        );
        """
        await conn.execute(create_table_query)

    async def import_data_and_get_employees(
        self, json_path: str, office_id: int
    ) -> list[str]:
        """
        Импортирует данные в БД и получает сотрудников по ID офиса.
        """
        async with session_generator(self.pool) as conn:
            await self.create_database_if_not_exists(conn, config.DB_NAME)
            await self.create_table_if_not_exists(conn)

        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        async with session_generator(self.pool) as conn:
            await self._insert_data(conn, data)
            return await self._get_employees_by_office_id(conn, office_id)

    async def _insert_data(self, conn, data: list[dict[str, str | None | int]]) -> None:
        """
        Вставляет данные в базу данных.
        """
        for entry in data:
            await conn.execute(
                """
            INSERT INTO organization (Id, ParentId, Name, Type)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (Id) DO NOTHING
            """,
                entry["id"],
                entry["ParentId"],
                entry["Name"],
                entry["Type"],
            )

    async def _get_employees_by_office_id(self, conn, office_id: int) -> list[str]:
        """
        Получает список сотрудников для заданного офиса.
        """
        result = await conn.fetch(
            """
            WITH RECURSIVE hierarchy AS (
                SELECT id, parentid, name, type
                FROM organization
                WHERE id = $1

                UNION ALL

                SELECT o.id, o.parentid, o.name, o.type
                FROM organization o
                JOIN hierarchy h ON o.id = h.parentid
            ),
            city_root AS (
                SELECT id
                FROM hierarchy
                WHERE parentid IS NULL
            ),
            employees_in_city AS (
                SELECT o.id, o.name
                FROM organization o
                WHERE o.parentid IN (
                    WITH RECURSIVE dept_hierarchy AS (
                        SELECT id, parentid
                        FROM organization
                        WHERE parentid IN (SELECT id FROM city_root)
                        
                        UNION ALL
                        
                        SELECT o.id, o.parentid
                        FROM organization o
                        JOIN dept_hierarchy dh ON o.parentid = dh.id
                    )
                    SELECT id FROM dept_hierarchy
                ) AND o.type = 3
            )
            SELECT name
            FROM employees_in_city;
            """,
            office_id,
        )

        return [employee["name"] for employee in result]
