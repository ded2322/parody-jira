from core.dao.base import BaseDao
from core.models.todo_models import Tasks


class TasksDao(BaseDao):
    model = Tasks
