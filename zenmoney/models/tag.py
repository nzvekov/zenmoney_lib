from dataclasses import dataclass
from typing import Any, Optional
from uuid import UUID

from .utils import from_bool, from_int, from_none, from_str, from_union, is_type


@dataclass
class Tag:
    id: UUID
    user: int
    color: None
    title: str
    changed: int
    picture: None
    showIncome: bool
    showOutcome: bool
    budgetIncome: bool
    budgetOutcome: bool
    staticId: Optional[int] = None
    icon: Optional[str] = None
    parent: Optional[UUID] = None
    required: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tag':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        id = UUID(obj.get("id"))
        user = from_int(obj.get("user"))
        color = from_none(obj.get("color"))
        title = from_str(obj.get("title"))
        changed = from_int(obj.get("changed"))
        picture = from_none(obj.get("picture"))
        staticId = from_union([from_none, lambda x: int(from_str(x))], obj.get("staticId"))
        showIncome = from_bool(obj.get("showIncome"))
        showOutcome = from_bool(obj.get("showOutcome"))
        budgetIncome = from_bool(obj.get("budgetIncome"))
        budgetOutcome = from_bool(obj.get("budgetOutcome"))
        icon = from_union([from_none, from_str], obj.get("icon"))
        parent = from_union([from_none, lambda x: UUID(x)], obj.get("parent"))
        required = from_union([from_bool, from_none], obj.get("required"))
        return Tag(
            id,
            user,
            color,
            title,
            changed,
            picture,
            staticId,
            showIncome,
            showOutcome,
            budgetIncome,
            budgetOutcome,
            icon,
            parent,
            required,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = str(self.id)
        result["user"] = from_int(self.user)
        result["color"] = from_none(self.color)
        result["title"] = from_str(self.title)
        result["changed"] = from_int(self.changed)
        result["picture"] = from_none(self.picture)
        result["staticId"] = from_union(
            [
                lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x)),
            ],
            self.staticId,
        )
        result["showIncome"] = from_bool(self.showIncome)
        result["showOutcome"] = from_bool(self.showOutcome)
        result["budgetIncome"] = from_bool(self.budgetIncome)
        result["budgetOutcome"] = from_bool(self.budgetOutcome)
        result["icon"] = from_union([from_none, from_str], self.icon)
        result["parent"] = from_union([from_none, lambda x: str(x)], self.parent)
        result["required"] = from_union([from_bool, from_none], self.required)
        return result
