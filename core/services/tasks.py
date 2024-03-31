from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from core.logger import logger
from core.utils.repository import AbstractRepository
from core.schemas.tasks import TasksSchema, TasksSchemaUpdate, TasksSchemaID


class TasksService:
    def __init__(self, tasks_repo: AbstractRepository):
        self.tasks_repo: AbstractRepository = tasks_repo()

    async def show_tasks(self) -> dict:
        """
        Делает запрос на вытаскивания всех задач из бд
        """
        try:
            result = await self.tasks_repo.show_all_table()
            return result

        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database exc show database: {str(e)}"
            else:
                msg = f"Unknown exc: {str(e)}"

            logger.error(msg, exc_info=True)

    async def found_task(self, data_tasks: TasksSchemaID) -> HTTPException or dict:
        """
        Ищет задачу по id
        """
        try:
            result = await self.tasks_repo.found_one_or_none(id=data_tasks.id_tasks)
            if not result:
                return HTTPException(status_code=404, detail="Task not found")
            return result
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database exc found_task: {str(e)}"
            else:
                msg = f"Unknown exc: {str(e)}"

            logger.error(msg, exc_info=True)

    async def add_tasks(self, date_tasks: TasksSchema) -> HTTPException or dict:
        """
        Добавляет задачу
        """
        try:
            if date_tasks.priority > 5 or date_tasks.priority < 1:
                return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Incorrect priority")

            await self.tasks_repo.insert_data(name=date_tasks.name, description=date_tasks.description,
                                              priority=date_tasks.priority, data_completion=date_tasks.data_completion)

            return {"message": "Task successful add"}

        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database exc add task: {str(e)}"
            else:
                msg = f"Unknown exc: {str(e)}"

            logger.error(msg, exc_info=True)

    async def update_tasks(self, date_tasks: TasksSchemaUpdate) -> HTTPException or dict:
        """
        Обновляет задачу
        """
        try:
            # проверяет наличие задачи в бд
            if not await self.tasks_repo.found_one_or_none(id=date_tasks.id_tasks):
                return HTTPException(status_code=404, detail="Task not found")
            # проход циклом по переданным данным для обновления
            for data_task in date_tasks:
                # если данные не обновлены (None) или это id_tasks
                if data_task[1] is None or data_task[0] == "id_tasks":
                    pass # эти данные просто пропускаются
                else:
                    # если данные изменены, то эти данные заносятся в словарь,
                    # и после обновляются в таблице
                    data_by_tasks = {data_task[0] : data_task[1]}
                    await self.tasks_repo.update_data(date_tasks.id_tasks,data_by_tasks)

            return {"Tasks": "Task successful update"}

        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database exc update tasks: {str(e)}"
            else:
                msg = f"Unknown exc: {str(e)}"

            logger.error(msg, exc_info=True)

    async def delete_tasks(self, data_tasks: TasksSchemaID) -> HTTPException or dict:
        """
        Удаляет задачу
        """
        try:
            if not await self.tasks_repo.found_one_or_none(id=data_tasks.id_tasks):
                return HTTPException(status_code=404, detail="Task not found")

            await self.tasks_repo.delete_data(id=data_tasks.id_tasks)
            return {"message": "Task successful delete"}

        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database exc delete tasks: {str(e)}"
            else:
                msg = f"Unknown exc: {str(e)}"

            logger.error(msg, exc_info=True)

