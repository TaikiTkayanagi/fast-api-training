
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    authror: str = Field(default="", min_length=1, max_length=100)

class BookResponse(Book):
    id: int

books: list[BookResponse] = [
    BookResponse(id=0, title="Book One", authror="Author One"),
    BookResponse(id=1, title="Book Two", authror="Author Two"),
    BookResponse(id=2, title="Book Three", authror="Author Three"),
]


@app.get("/books/", response_model=list[BookResponse])
def read_books():
    if(not books):
        raise HTTPException(status_code=404, detail="No books found")
    return books

@app.get("/books/{book_id}", response_model=BookResponse)
def read_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="Book not found")
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books/", response_model=BookResponse)
def create_book(book: Book):
    id = max([b.id for b in books], default=-1) + 1
    newBook = BookResponse(id=id, **book.model_dump())
    books.append(newBook)
    return newBook

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated_book: Book):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="Book not found")
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = BookResponse(id=book_id, **updated_book.model_dump())
            return books[index]
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", response_model=BookResponse)
def delete_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="Book not found")
    for index, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(index)
            return deleted_book
    raise HTTPException(status_code=404, detail="Book not found")