from typing import Dict, List, Optional
from ..model.entity import Entity

class Repository:
    def __init__(self):
        self._data: Dict[int, Entity] = {}

    def insert(self, entity: Entity):
        self._data[entity.id] = entity

    def get_by_id(self, entity_id: int) -> Optional[Entity]:
        return self._data.get(entity_id)

    def list_all(self) -> List[Entity]:
        return list(self._data.values())

    def delete(self, entity_id: int):
        if entity_id in self._data:
            del self._data[entity_id]
            
    def __str__(self) -> str:
        if not self._data:
            return "No entities registered."
        sorted_items = sorted(self._data.values(), key=lambda e: e.id)
        return "\n".join(str(entity) for entity in sorted_items)