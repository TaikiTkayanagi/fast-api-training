from typing import Optional


class Book:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year


books = [
    Book(id=1, title="1984", author="George Orwell", year=1949),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", year=1960),
    Book(id=3, title="The Great Gatsby",
         author="F. Scott Fitzgerald", year=1925),
    Book(id=4, title="One Hundred Years of Solitude",
         author="Gabriel Garcia Marquez", year=1967)
]


def get_books(book_id: Optional[int]) -> list[Book]:
    if book_id is None:
        return books
    r = [b for b in books if b.id == book_id]
    return r
