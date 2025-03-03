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

python3 -m venv env
source env/bin/activate  # В Windows используйте `env\Scripts\activate`
```
- Установите зависимости:
```bash
uv install
```
или
```bash
poetry install
```
или
```bash
pip install -r requirements.txt
```
- Разверните PostgreSQL с помощью Docker:
```bash
docker-compose up -d
```
- Создайте файл .env с переменными окружения:
```plaintext
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5433
DB_NAME=employees
```
🚀 Использование

- Для использования системы выполните следующую команду:
```bash
python main.py <path-to-json-file> <id>
```

Замените `<path-to-json-file>` на путь к вашему JSON файлу, а `<id>` на ID сотрудника или офиса.