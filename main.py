import asyncio
from cli import parse_args
from db import create_connection_pool, create_database_if_not_exists
from usecase import EmployeeService
from colorama import Fore, Style
import config


async def main() -> None:
    """
    Основная функция программы.
    """
    args = parse_args()

    print(Fore.YELLOW + "Подключение к базе данных..." + Style.RESET_ALL)
    await create_database_if_not_exists(config.DSN, "employees")
    pool = await create_connection_pool(dsn=config.DSN)

    employee_service = EmployeeService(pool)

    print(Fore.CYAN + "Импортируем данные и получаем сотрудников..." + Style.RESET_ALL)
    employees = await employee_service.import_data_and_get_employees(
        args.json_file, args.employee_id
    )

    if employees:
        print(
            Fore.BLUE + f"Сотрудники в офисе с ID {args.employee_id}:" + Style.RESET_ALL
        )
        for employee in employees:
            print(Fore.MAGENTA + f"- {employee}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Нет сотрудников в этом офисе." + Style.RESET_ALL)


if __name__ == "__main__":
    asyncio.run(main())
