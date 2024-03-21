from pydantic import BaseModel


class SStates(BaseModel):
    title: str


class SStatesUpdate(BaseModel):
    old_title: str
    new_title: str
