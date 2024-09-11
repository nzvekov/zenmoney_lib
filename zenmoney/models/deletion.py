from dataclasses import dataclass
from uuid import UUID

from .utils import check_dict_type, check_object_class_name_list, from_int, from_str


@dataclass
class Deletion:
    id: UUID | int
    object: str
    stamp: int
    user: int

    def __post_init__(self):
        check_object_class_name_list(self.object)

    @staticmethod
    def from_dict(obj: dict) -> 'Deletion':
        check_dict_type(obj)

        obj_id = obj.get("id")
        if isinstance(obj_id, str):
            obj_id = UUID(obj.get("id"))

        return Deletion(
            id=obj_id,
            object=from_str(obj.get("object")),
            stamp=from_int(obj.get("stamp")),
            user=from_int(obj.get("user")),
        )

    def to_dict(self) -> dict:
        obj_id = self.id
        if isinstance(obj_id, UUID):
            obj_id = str(self.id)

        return {
            "id": obj_id,
            "object": from_str(self.object),
            "stamp": from_int(self.stamp),
            "user": from_int(self.user),
        }
