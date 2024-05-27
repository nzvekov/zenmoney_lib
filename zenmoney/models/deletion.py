from dataclasses import dataclass
from typing import Any

from .mixins import BaseUserObjectMixin
from .utils import check_object_class_name_list, from_int, from_str


@dataclass
class Deletion(BaseUserObjectMixin):
    object: str
    stamp: int

    def __post_init__(self):
        check_object_class_name_list(self.object)

    @staticmethod
    def from_dict(obj: Any) -> 'Deletion':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        return Deletion(
            id=from_str(obj.get("id")),
            object=from_str(obj.get("object")),
            stamp=from_int(obj.get("stamp")),
            user=from_int(obj.get("user")),
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["object"] = from_str(self.object)
        result["stamp"] = from_int(self.stamp)
        result["user"] = from_int(self.user)

        return result
