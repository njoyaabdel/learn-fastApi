
from fastapi import FastAPI
import random
from enum import Enum
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
async def root():
    return { 'example':'this is a example', 'data': 0}

@app.post('/')
async def post():
    return{"message":"hello from the post route"}

@app.put('/')
async def put():
    return{"message":"hello from the put route"}
@app.get('/user')
async def list_user():
    return{"message":"list users route"}

@app.get('/users/me')
async def get_current_user():
    return{"message": "this a current user"}

@app.get('/users/{user_id}')
async def get_user(user_id: str):
    return {'item_id':user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetabe = "vegetable"
    dairy = "dairy"
@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetabe:
        return {"food_name":food_name ,"messages":"you are hearly"}
    
    if food_name.value == "fruits":
        return{
            "food_name": food_name,
            "mesages":"you are still heartly, but like a sweat thinks"}
    return {"food_name": food_name,
            "messages":"i likes a chocolate milk"}

fake_items_db =[{"item_name": "foo"},{"item_name": "barateon"},{"item_name": "baz"}]

@app.get("/items")
async def list_items(skip : int = 0, limit : int = 10):
    return fake_items_db[skip: skip + limit ]

@app.get("/items/{item_id}")
async def get_item(item_id: str, q:str | None = None, short: bool =False ):
    item = {"item_id":item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"decription":"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."})
    return item
@ app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(item_id:str,sample_query_param:str, q:str |None = None, short : bool = False):
    item = {"item_id":item_id, "sample_query_param":sample_query_param}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"decription":"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."})
    return item

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
@app.put("/items/{item_id}")
async def create_item_with_put(item_id:int,item:Item, q: str | None = None):
    result ={"item_id":item_id, **item.dict()}
    if q: 
        result.update({"q":q})
    return result