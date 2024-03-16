from fastapi import APIRouter, HTTPException,status
from todo_app.dao.states_dao import StatesDao
from todo_app.schemas.states_schemas import SStates, SStatesUpdate

router = APIRouter(
    prefix="/state",
    tags=["States"]
)


@router.get("/all", status_code=200,summary="Get all states")
async def get_all_states():
    return await StatesDao.show_table()


@router.post("/add",status_code=200,summary="Add states")
async def add_states(data_task: SStates):
    await StatesDao.add_data(title=data_task.title)


@router.patch("/change",status_code=200,summary="Change states")
async def update_states(data_change: SStatesUpdate):
    data_task = await StatesDao.found_one_or_none(title=data_change.old_title)
    if not data_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Состояние на найдено")

    await StatesDao.update_date(data_task["id"], "title", data_change.new_title)


@router.delete("/delete")
async def delete_tasks(title_task: str):
    data_task = await StatesDao.found_one_or_none(title=title_task)
    if not data_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Состояние на найдено")
    await StatesDao.delete(id=data_task["id"])
