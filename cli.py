import argparse
import os
import json


def validate_json_file(value: str) -> str:
    """
    Проверяет существование файла, его расширение и корректность JSON.
    Возвращает путь к файлу, если все проверки пройдены.
    """
    if not os.path.exists(value):
        raise argparse.ArgumentTypeError(f"Файл по пути '{value}' не существует.")

    if not value.endswith(".json"):
        raise argparse.ArgumentTypeError(f"Файл '{value}' не является JSON.")

    try:
        with open(value, "r", encoding="utf-8") as file:
            json.load(file)
    except json.JSONDecodeError:
        raise argparse.ArgumentTypeError(f"Файл '{value}' не является корректным JSON.")

    return value


def parse_args() -> argparse.Namespace:
    """
    Разбор аргументов командной строки.
    """
    parser = argparse.ArgumentParser(
        description="Программа для импорта данных и выборки сотрудников"
    )
    parser.add_argument("json_file", type=validate_json_file, help="Путь к JSON файлу")
    parser.add_argument("employee_id", type=int, help="Идентификатор сотрудника")
    return parser.parse_args()
