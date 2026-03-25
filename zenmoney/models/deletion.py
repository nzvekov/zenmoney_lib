from uuid import UUID

from pydantic import BaseModel, model_validator

from .utils import check_object_class_name_list


class Deletion(BaseModel):
    id: UUID | int
    object: str
    stamp: int
    user: int

    @model_validator(mode="after")
    def validate_object_name(self) -> "Deletion":
        check_object_class_name_list(self.object)
        return self

    @classmethod
    def from_dict(cls, obj: dict) -> "Deletion":
        obj_id = obj.get("id")
        if isinstance(obj_id, str):
            obj_id = UUID(obj_id)
        return cls(id=obj_id, object=obj["object"], stamp=obj["stamp"], user=obj["user"])

    def to_dict(self) -> dict:
        obj_id = str(self.id) if isinstance(self.id, UUID) else self.id
        return {"id": obj_id, "object": self.object, "stamp": self.stamp, "user": self.user}
