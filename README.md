# Тестовое задание для компании Tensor

Задание заключалось в импорте данных из json в sql и извлечения данных из sql с помощью сырого запроса
Для выполнения задания были использованы следующие библиотеки:

- [argparse](https://docs.python.org/3/library/argparse.html)
- [asyncpg](https://magicstack.github.io/asyncpg/current/)
- [tqdm](https://tqdm.github.io/)
- [colorama](https://pypi.org/project/colorama/)

> **Версия python** __3.12__

Демонстрация работы ниже
![image](docs/doc.gif)

⚙️ Установка

Чтобы запустить проект, выполните следующие шаги:
- Скопируйте репозиторий
```bash
git clone git@github.com:Ondest/tensor_test_task.git
cd tensor_test_task
```

- Создайте и активируйте виртуальное окружение:

```bash
uv venv
source .venv/bin/activate
```
- Установите зависимости:
```bash
uv sync
```
Для обратной совместимости с pip есть также requirements.txt

- Разверните PostgreSQL с помощью Docker:
```bash
docker-compose up -d
```
- Создайте файл .env с переменными окружения как .env-example:

🚀 Использование

- Для использования системы выполните следующую команду:
```bash
python main.py <path-to-json-file> <id>
```

Замените `<path-to-json-file>` на путь к вашему JSON файлу, а `<id>` на ID сотрудника или офиса.