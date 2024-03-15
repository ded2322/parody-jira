from pydantic import BaseModel
from typing import Optional


class STasks(BaseModel):
    title: str
    description: str
    state: str


class STasksUpdate(BaseModel):
    name_task:str
    title: Optional[str]
    description: Optional[str]
    state: Optional[str]
