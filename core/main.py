import uvicorn
import time
from fastapi import FastAPI, Request
from core.logger import logger
from core.endpoint.router import router as tasks_router


app = FastAPI()
app.include_router(tasks_router)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(
        f"Request handling time", extra={"process_time": round(process_time, 4)}
    )
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
