from dataclasses import dataclass
from uuid import UUID

from .utils import check_dict_type, check_object_class_name_list, from_int, from_str


@dataclass
class Deletion:
    id: UUID
    object: str
    stamp: int
    user: int

    def __post_init__(self):
        check_object_class_name_list(self.object)

    @staticmethod
    def from_dict(obj: dict) -> 'Deletion':
        check_dict_type(obj)

        return Deletion(
            id=UUID(obj.get("id")),
            object=from_str(obj.get("object")),
            stamp=from_int(obj.get("stamp")),
            user=from_int(obj.get("user")),
        )

    def to_dict(self) -> dict:
        return {
            "id": from_str(self.id),
            "object": from_str(self.object),
            "stamp": from_int(self.stamp),
            "user": from_int(self.user),
        }
