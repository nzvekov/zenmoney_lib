from dataclasses import dataclass
from uuid import UUID

from .utils import check_dict_type, from_int, from_str


@dataclass
class Merchant:
    id: UUID
    user: int
    title: str
    changed: int

    @staticmethod
    def from_dict(obj: dict) -> 'Merchant':
        check_dict_type(obj)

        return Merchant(
            id=UUID(obj.get("id")),
            user=from_int(obj.get("user")),
            title=from_str(obj.get("title")),
            changed=from_int(obj.get("changed")),
        )

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "user": from_int(self.user),
            "title": from_str(self.title),
            "changed": from_int(self.changed),
        }
