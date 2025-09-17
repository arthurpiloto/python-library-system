from datetime import date
from typing import List, TYPE_CHECKING
from .person import Person

if TYPE_CHECKING:
    from .book import Book

class Author(Person):
    def __init__(self, id: int, name: str, birthdate: date, contact_info: str):
        super().__init__(id, name, birthdate, contact_info)
        self.written_books: List[Book] = []

    def add_book(self, book: Book):
        if book not in self.written_books:
            self.written_books.append(book)

    def __str__(self) -> str:
        return f"{super().__str__()}, Writter Books: {self.written_books}"