from typing import Dict, List, Optional, Type
from ..model.entity import Entity
from ..model.author import Author
from ..model.reader import Reader
from ..model.genre import Genre
from ..model.book import Book
from ..model.loan import Loan
from .repository import Repository

class Database:
<<<<<<< HEAD
=======
    """
    Ponto de acesso central para a persistência.
    Gerencia os repositórios para cada tipo de entidade e a geração de IDs.
    """
>>>>>>> 75bb60ffe3e1caaf770e666cbdc24203ae440a4d
    def __init__(self):
        self._repositories: Dict[Type[Entity], Repository] = {
            Author: Repository(),
            Reader: Repository(),
            Genre: Repository(),
            Book: Repository(),
            Loan: Repository()
        }
        self._id_counters: Dict[Type[Entity], int] = {
            Author: 1,
            Reader: 1,
            Genre: 1,
            Book: 1,
            Loan: 1
        }

    def _get_repository(self, entity_type: Type[Entity]) -> Repository:
        repo = self._repositories.get(entity_type)
        if repo is None:
            raise TypeError(f"No repository registered for type {entity_type.__name__}")
        return repo
        
    def insert(self, entity: Entity) -> Entity:
<<<<<<< HEAD
=======
        """Insere uma entidade, atribuindo um ID único e sequencial."""
>>>>>>> 75bb60ffe3e1caaf770e666cbdc24203ae440a4d
        entity_type = type(entity)
        next_id = self._id_counters[entity_type]
        entity.id = next_id
        self._id_counters[entity_type] = next_id + 1
        
        repo = self._get_repository(entity_type)
        repo.insert(entity)
        return entity

    def get_by_id(self, entity_type: Type[Entity], entity_id: int) -> Optional[Entity]:
        repo = self._get_repository(entity_type)
        return repo.get_by_id(entity_id)

    def list_all(self, entity_type: Type[Entity]) -> List[Entity]:
        repo = self._get_repository(entity_type)
        return repo.list_all()
        
    def delete(self, entity_type: Type[Entity], entity_id: int):
        repo = self._get_repository(entity_type)
        repo.delete(entity_id)
        
    def get_repository_as_string(self, entity_type: Type[Entity]) -> str:
        repo = self._get_repository(entity_type)
        return str(repo)
