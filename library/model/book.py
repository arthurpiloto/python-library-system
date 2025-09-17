from typing import List, Optional, TYPE_CHECKING
from .entity import Entity
from .genre import Genre
from .author import Author

if TYPE_CHECKING:
    from .reader import Reader

class Book(Entity):
    def __init__(self, id: int, title: str, author: Author, genre: Genre, total_copies: int):
        super().__init__(id)
        if not (author, Author) or not (genre, Genre):
            raise TypeError("Invalid type for author or genre.")
        
        self.title = title
        self.author = author
        self.genre = genre
        self.total_copies = total_copies
        self._available_copies = total_copies
        self._reservation_queue: List[Reader] = []

    @property
    def available_copies(self) -> int:
        return self._available_copies

    def is_available(self) -> bool:
        return self._available_copies > 0

    def loan_copy(self):
        if self.is_available():
            self._available_copies -= 1
        else:
            raise ValueError("No copies available to loan.")

    def return_copy(self):
        if self._available_copies < self.total_copies:
            self._available_copies += 1

    def add_reservation(self, reader: Reader):
        if reader not in self._reservation_queue:
            self._reservation_queue.append(reader)

    def get_next_reader_in_queue(self) -> Optional[Reader]:
        if self._reservation_queue:
            return self._reservation_queue.pop(0)
        return None

    def __str__(self) -> str:
        return f"{super().__str__()}, Title: {self.title}, Author: {self.author.name}, Available: {self._available_copies}/{self.total_copies}"