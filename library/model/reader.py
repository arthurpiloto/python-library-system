from .person import Person
from datetime import date

class Reader(Person):
    def __init__(self, id: int, name: str, birthdate: date, contact_info: str):
        super().__init__(id, name, birthdate, contact_info)