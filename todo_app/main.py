from fastapi import FastAPI
from todo_app.tasks.router import router as router_tasks
from todo_app.states.router import router as router_states

app = FastAPI()

app.include_router(router_tasks)
app.include_router(router_states)
