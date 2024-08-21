from fastapi import FastAPI
import uvicorn

from controller import prompt_controller, event_controller

app = FastAPI()

app.include_router(event_controller.router, prefix='/api/v1', tags=['event_api'])
app.include_router(prompt_controller.router, prefix='/api/v1/prompt', tags=['prompt_api'])


@app.get('/')
def home():
    return {'hello' : 'calinify'}


if __name__ == '__main__':
    
    # Test build
    uvicorn.run("app:app", host='127.0.0.1', port=5050, reload=True)