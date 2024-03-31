from pydantic import BaseModel
from typing import Optional
from datetime import date


class TasksSchema(BaseModel):
    name: str
    description: str
    priority: int
    data_completion: date


class TasksSchemaID(BaseModel):
    id_tasks: int


class TasksSchemaUpdate(BaseModel):
    id_tasks: int
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    data_completion: Optional[date] = None
