from fastapi import APIRouter

from todo_app.dao.tasks_dao import TasksDao
from todo_app.dao.states_dao import StatesDao
from todo_app.schemas.tasks_schemas import STasks,STasksUpdate

router= APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/all")
async def get_all_tasks():
    return await TasksDao.show_table()


@router.post("/add")
async def add_tasks(data_task:STasks):
    data_tasks = await StatesDao.found_one_or_none(title="string")
    if not data_tasks:
        return "ext"
    await TasksDao.add_data(title = data_task.title,
                            description=data_task.description,
                            state= data_tasks[0]["id"])

@router.patch("/change")
async def update_tasks(data_change: STasksUpdate):
    data_task = await TasksDao.found_one_or_none(title=data_change.name_task)
    if not data_task:
        return "ext"

    if data_change.title:
        await TasksDao.update_date(data_task[0]["id"], "title",data_change.title)
    if data_change.description:
        await TasksDao.update_date(data_task[0]["id"], "description", data_change.description)
    if data_change.state:
        await TasksDao.update_date(data_task[0]["id"], "state", data_change.state)


@router.delete("/delete")
async def delete_tasks(title_task:str):
    data_task = await TasksDao.found_one_or_none(title=title_task)
    if not data_task:
        return "ext"
    await TasksDao.delete(id = data_task[0]["id"])