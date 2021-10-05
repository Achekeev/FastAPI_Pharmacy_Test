from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'This Is Index Page'}

