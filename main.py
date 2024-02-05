from typing import union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: union[str, None] = None ):
    return {"item_id": item_id, "q":q}