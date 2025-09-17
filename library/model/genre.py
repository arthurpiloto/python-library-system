from .entity import Entity

class Genre(Entity):
    def __init__(self, id: int, name: str):
        super().__init__(id)
        self.name = name

    def __str__(self) -> str:
        return f"{super().__str__()}, Genre: {self.name}"