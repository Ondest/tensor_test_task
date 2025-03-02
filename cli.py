import argparse
import os
import json


class ValidateJsonFile(argparse.Action):
    """Валидация пути и корректности JSON файлa"""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str,
        option_string=None,
    ) -> None:
        if not os.path.exists(values):
            raise argparse.ArgumentTypeError(f"Файл по пути '{values}' не существует.")

        if not values.endswith(".json"):
            raise argparse.ArgumentTypeError(f"Файл '{values}' не является JSON.")

        try:
            with open(values, "r", encoding="utf-8") as file:
                json.load(file)
        except json.JSONDecodeError:
            raise argparse.ArgumentTypeError(
                f"Файл '{values}' не является корректным JSON."
            )

        setattr(namespace, self.dest, values)


def parse_args() -> argparse.Namespace:
    """
    Разбор аргументов командной строки.
    """
    parser = argparse.ArgumentParser(
        description="Программа для импорта данных и выборки сотрудников"
    )
    parser.add_argument(
        "json_file", type=str, action=ValidateJsonFile, help="Путь к JSON файлу"
    )
    parser.add_argument("employee_id", type=int, help="Идентификатор сотрудника")
    return parser.parse_args()
