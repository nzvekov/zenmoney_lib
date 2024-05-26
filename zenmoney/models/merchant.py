from dataclasses import dataclass
from typing import Any
from uuid import UUID

from .utils import from_int, from_str


@dataclass
class Merchant:
    id: UUID
    user: int
    title: str
    changed: int

    @staticmethod
    def from_dict(obj: Any) -> 'Merchant':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        id = UUID(obj.get("id"))
        user = from_int(obj.get("user"))
        title = from_str(obj.get("title"))
        changed = from_int(obj.get("changed"))
        return Merchant(id, user, title, changed)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = str(self.id)
        result["user"] = from_int(self.user)
        result["title"] = from_str(self.title)
        result["changed"] = from_int(self.changed)
        return result
