from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str = None
    is_done: bool = False


items = []


@app.get("/")
def root():
    """Returns a simple greeting message."""
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: Item):
    """Adds a new item to the list."""
    items.append(item)
    return items


@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    """Returns a list of items, up to a specified limit."""
    return items[0:limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    """Returns an item by its ID."""
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(
            status_code=404, detail=f"Item {item_id} not found")
