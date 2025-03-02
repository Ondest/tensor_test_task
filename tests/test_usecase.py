import pytest
import asyncpg
import json
from usecase import EmployeeService
from db import create_connection_pool
import config


@pytest.fixture(scope="module")
async def pool():
    pool = await create_connection_pool(config.DSN)
    yield pool
    await pool.close()


@pytest.fixture(scope="module")
async def employee_service(pool):
    service = EmployeeService(pool)
    yield service


async def test_import_data_and_get_employees(employee_service):
    sample_data = [
        {"id": 1, "ParentId": None, "Name": "Office1", "Type": 2},
        {"id": 2, "ParentId": 1, "Name": "John Doe", "Type": 3},
    ]
    with open("sample.json", "w") as f:
        json.dump(sample_data, f)

    employees = await employee_service.import_data_and_get_employees("sample.json", 1)
    assert len(employees) == 3
