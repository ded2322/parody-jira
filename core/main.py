from fastapi import FastAPI
from core.tasks.router import router as router_tasks
from core.states.router import router as router_states

app = FastAPI()

app.include_router(router_tasks)
app.include_router(router_states)
