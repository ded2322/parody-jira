from todo_app.models.state_models import States
from todo_app.dao.base import BaseDao


class StatesDao(BaseDao):
    model = States
