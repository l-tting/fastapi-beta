from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id : int):
#     return {"item_id": item_id}

my_dict ={"name":"Brian","age":25,"address":"Nairobi"}

@app.get("/query")
async def get_query(skip: int=0,limit:int=10):
    data = {key: my_dict[key] for key in list(my_dict.keys())[skip:skip + limit]}
    return data

class Item(BaseModel):
    name: str
    price: float
    tax: float | None = None

class ItemSaved(Item):
    id : int

@app.post("/items/")
async def create_item(item: Item):
    item_saved = ItemSaved(id=1,name=item.name,price=item.price,tax=item.tax)
    return item_saved



  
    
# @app.post("/items/", response_model=ItemSaved)
# async def create_item(item: Item):
#     item_saved = ItemSaved(id=1, **item.dict())
#     return item_saved