from datetime import date
from .entity import Entity

class Person(Entity):
    def __init__(self, id: int, name: str, birth_date: date, contact: str):
        super().__init__(id)
        self.name = name
        self.birth_date = birth_date
        self.contact = contact
    
    def __str__(self) -> str:
        return f"{super().__str__()}, Name: {self.name}, Birth Date: {self.birth_date}, Contact: {self.contact}"