from fastapi import APIRouter, HTTPException, status

from todo_app.dao.tasks_dao import TasksDao
from todo_app.dao.states_dao import StatesDao
from todo_app.schemas.tasks_schemas import STasks, STasksUpdate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/all", status_code=200,summary="Get all tasks")
async def get_all_tasks():
    return await TasksDao.show_table()


@router.post("/add",status_code=200,summary="Add tasks")
async def add_tasks(data_task: STasks):
    data_tasks = await StatesDao.found_one_or_none(title=data_task.state)
    if not data_tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Состояние не найдено")
    await TasksDao.add_data(title=data_task.title,
                            description=data_task.description,
                            state=data_tasks[0]["id"])


@router.patch("/change",status_code=200,summary="Change task")
async def update_tasks(data_change: STasksUpdate):
    data_task = await TasksDao.found_one_or_none(title=data_change.name_task)
    if not data_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такой задачи нет")

    if data_change.title:
        await TasksDao.update_date(data_task[0]["id"], "title", data_change.title)
    if data_change.description:
        await TasksDao.update_date(data_task[0]["id"], "description", data_change.description)
    if data_change.state:
        await TasksDao.update_date(data_task[0]["id"], "state", data_change.state)


@router.delete("/delete",status_code=200, summary="Delete task")
async def delete_tasks(title_task: str):
    data_task = await TasksDao.found_one_or_none(title=title_task)
    if not data_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такой задачи нет")
    await TasksDao.delete(id=data_task[0]["id"])
