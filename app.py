from fastapi import FastAPI
import uvicorn

from controller import calendar

app = FastAPI()

app.include_router(calendar.router, prefix='/api/v1', tags=['calendar_api'])

@app.get('/')
def home():
    return {'hello' : 'calinify'}


if __name__ == '__main__':
    
    uvicorn.run("app:app", host='127.0.0.1', port=5050, reload=True)