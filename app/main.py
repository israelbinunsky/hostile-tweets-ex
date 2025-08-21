from fastapi import FastAPI
import uvicorn
from manager import manager

app = FastAPI()
manager = manager()

@app.get('/')
def get_data():
    data = manager.get_result()
    return data

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)


