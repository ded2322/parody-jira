from todo_app.dao.base import BaseDao
from todo_app.models.todo_models import Tasks


class TasksDao(BaseDao):
    model = Tasks
