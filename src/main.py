
from typing import Optional
from fastapi import FastAPI, HTTPException


import book
import data


app = FastAPI()

@app.get("/users/{user_id}/")
def read_user(user_id: int):
    user = data.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/books/")
def read_books(id: Optional[int] = None):
    books = book.get_books(id)
    if not books:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"books": books}
