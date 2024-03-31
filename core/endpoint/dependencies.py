from core.repositories.tasks import TasksRepository
from core.services.tasks import TasksService


def tasks_service():
    return TasksService(TasksRepository)
