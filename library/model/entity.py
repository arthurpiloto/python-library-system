from abc import ABC

class Entity(ABC):
    def __init__(self, id: int = 0):
        self._id = id

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    def __str__(self) -> str:
        return f"ID: {self._id}"