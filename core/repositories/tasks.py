from core.model.tasks_models import Tasks
from core.utils.sqlalchemy_repository import SqlalchemyRepository


class TasksRepository(SqlalchemyRepository):
    models = Tasks
