import asyncpg


class OrganizationRepository:
    def __init__(self, conn: asyncpg.connection.Connection):
        self.conn = conn

    async def create_table_if_not_exists(self) -> None:
        """Создаёт таблицу 'organization', если она не существует."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS organization (
            Id INT PRIMARY KEY,
            ParentId INT,
            Name TEXT,
            Type INT
        );
        """
        await self.conn.execute(create_table_query)

    async def insert_organization(self, entry: dict) -> None:
        """Вставляет запись организации в базу данных."""
        await self.conn.execute(
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

    async def get_employees_by_office_id(self, office_id: int) -> list[str]:
        """Получает список сотрудников по идентификатору офиса."""
        result = await self.conn.fetch(
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
