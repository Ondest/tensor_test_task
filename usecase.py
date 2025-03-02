import json
from infra.db import session_generator
from infra.organization_repository import OrganizationRepository
from tqdm.asyncio import tqdm_asyncio
from colorama import Fore, Style


class EmployeeService:
    def __init__(self, pool):
        self.pool = pool

    async def import_data_and_get_employees(
        self, json_path: str, office_id: int
    ) -> list[str]:
        """
        Импортирует данные в БД и получает сотрудников по ID офиса.
        """
        async with session_generator(self.pool) as conn:
            repository = OrganizationRepository(conn)
            await repository.create_table_if_not_exists()

            with open(json_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            for entry in tqdm_asyncio(
                data,
                total=len(data),
                desc=f"{Fore.CYAN}Импорт данных{Style.RESET_ALL}",
                bar_format="{l_bar}{bar}{r_bar}",
                unit=" зап.",
            ):
                await repository.insert_organization(entry)

            return await repository.get_employees_by_office_id(office_id)
