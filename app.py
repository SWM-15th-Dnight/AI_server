import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import uvicorn

from config import refresh_connection_pool
from controller import prompt_controller, event_controller

@asynccontextmanager
async def lifespan(app : FastAPI):
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_connection_pool, trigger='interval', seconds=900)
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

app.include_router(event_controller.router, prefix='/api/v1', tags=['event_api'])
app.include_router(prompt_controller.router, prefix='/api/v1/prompt', tags=['prompt_api'])


@app.get('/')
def home():
    return {'hello' : 'calinify'}

if __name__ == '__main__':
    
    if os.environ.get("CALINIFY_AI_SERVER_PROFILE") == "PROD":
        raise RuntimeError(
            "운영 및 배포 환경에서는 반드시 터미널로 uvicorn을 동작시켜야 합니다."
        )
    
    # DEV build
    uvicorn.run("app:app", host='127.0.0.1', port=5050, reload=True)