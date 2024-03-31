from fastapi import APIRouter
from core.endpoint.dependencies import tasks_service
from core.schemas.tasks import TasksSchema, TasksSchemaUpdate, TasksSchemaID

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/all", status_code=200, summary="Show all tasks")
async def show_all_tasks():
    """
    Отображает все таски
    :return: Словарь с списком из задач
    """
    return await tasks_service().show_tasks()


@router.post("/found", status_code=200, summary="Find task by id")
async def found_task(data_id: TasksSchemaID):
    """
    Производит поиск задачи по id
    :param data_id: обязательные параметры все
    :return: Словарь в словаре с данными
    """
    return await tasks_service().found_task(data_id)


@router.post("/add", status_code=201, summary="Add new tasks")
async def add_tasks(data_task: TasksSchema):
    """
    Добавляет новые задачи
    :param data_task: Все параметры обязательны
    :return: Словарь с сообщением об успешном добавлении задачи или ошибка
    """
    return await tasks_service().add_tasks(data_task)


@router.patch("/update", status_code=200, summary="Update tasks")
async def update_task(data_task: TasksSchemaUpdate):
    """
    Обновляет задачи
    :param data_task: id_tasks обязательный, остальное опционально
    :return: Словарь с сообщением об успешном обновлении или ошибка
    """
    return await tasks_service().update_tasks(data_task)


@router.delete("/delete", status_code=201, summary="Delete tasks")
async def delete_tasks(data_task: TasksSchemaID):
    """
    Удаляет задачу по id
    :param data_task: все параметры обязательны
    :return: Словарь с сообщением об успешном удалении или ошибка
    """
    return await tasks_service().delete_tasks(data_task)
