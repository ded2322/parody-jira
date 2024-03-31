import pytest
from unittest.mock import AsyncMock
from core.repositories.tasks import TasksRepository


async def test_show_all_table():
    """
    Тест проверяющий show_all_table
    Проверяет есть ли задача с id=1
    """
    tasks = await TasksRepository().show_all_table()
    assert tasks[0]["id"] == 1


@pytest.mark.parametrize("id_tasks,is_present", [
    (1, True),
    (2, True),
    (100, False)
])
async def test_find_user_by_id(id_tasks,is_present):
    """
    Тест проверяющий found_one_or_none
    Передаются 2 id для проверки, есть ли задачи в бд
    """
    task = await TasksRepository().found_one_or_none(id = id_tasks)
    if is_present:
        assert task
        assert task["id"] == id_tasks
    else:
        assert not task

@pytest.mark.parametrize("id, column, new_data, check", [
    (1, "name", "New name", True),
    (100, "True","New name", None),
])
async def test_update_data(id, column, new_data,check):
    """
    Тест проверяющий update_data
    Передаются истинные и ложные данные, для проверки
    """
    result = await TasksRepository.update_data(id, column)
    assert result == check

@pytest.mark.parametrize("id,check, column_deleted", [
    (1, True, 1),
    (1000, True, 0)
])
async def test_delete(id ,check,column_deleted):
    """
    Тест проверяющий delete_data
    Передаются истинные и ложные данные, для проверки
    """
    result = await TasksRepository.delete_data(id = id)
    assert result[1] == column_deleted
