import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("id, name, description, priority, data_completion, status_code", [
    ("10", "Task2", "description task", 1, "2024-03-26", 201),
    ("11", "Task1", "description task", 1, "03", 422)
])
async def test_add_tasks(id, name, description, priority, data_completion, status_code, async_client: AsyncClient):
    response = await async_client.post("/tasks/add", json={
        "id": id,
        "name": name,
        "description": description,
        "priority": priority,
        "data_completion": data_completion
    })
    assert response.status_code == status_code


async def test_get_all_tasks(async_client: AsyncClient):
    response = await async_client.get("/tasks/all")
    assert response.status_code == 200
