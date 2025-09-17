from datetime import date, timedelta
from typing import Optional
from .entity import Entity
from .reader import Reader
from .book import Book

class Loan(Entity):
    def __init__(self, id: int, reader: Reader, book: Book, loan_days: int = 14):
        super().__init__(id)
        if not (reader, Reader) or not (book, Book):
            raise TypeError("Invalid type for reader or book.")
        
        self.reader = reader
        self.book = book
        self.loan_date = date.today()
        self.due_date = self.loan_date + timedelta(days=loan_days)
        self.return_date: Optional[date] = None
        self.status = "active"

    def return_loan(self):
        self.status = "returned"
        self.return_date = date.today()
        self.book.return_copy()
        self.reader.remove_loan(self)

    def __str__(self) -> str:
        return f"{super().__str__()}, Status: {self.status.capitalize()}, Due: {self.due_date}, Book: '{self.book.title}', Reader: {self.reader.name}"