import json
import asyncio
import pytest
from datetime import datetime
from sqlalchemy import insert
from fastapi.testclient import TestClient
from httpx import AsyncClient

from core.database import Base, engine, async_session_maker
from core.config import settings
from core.model.tasks_models import Tasks
from core.main import app as fastapi_app


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock(model: str):
        with open(f"core/tests/mock_{model}.json", "r", encoding="utf-8") as file:
            return json.load(file)

    tasks = open_mock("tasks")

    for task in tasks:
        task["data_completion"] = datetime.strptime(task["data_completion"], "%Y-%m-%d")

    async with async_session_maker() as session:
        query = insert(Tasks).values(tasks)
        await session.execute(query)
        await session.commit()


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def async_client():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as async_client:
        yield async_client
