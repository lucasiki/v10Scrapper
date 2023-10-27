from fastapi import FastAPI
from fastapi.requests import Request
from pydantic import BaseModel
from driver import rundriver


app = FastAPI()


class Item(BaseModel):
    url: str
    script: list 

@app.post('/script')
async def script(item: Item):
    res = rundriver(item)
    return {'data': res}