from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def home():
    return {'hello' : 'calinify'}


if __name__ == '__main__':
    
    uvicorn.run("app:app", host='127.0.0.1', port=5050, reload=True)