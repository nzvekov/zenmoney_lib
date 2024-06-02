from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from .utils import (
    check_dict_type,
    from_bool,
    from_int,
    from_none,
    from_str,
    from_union,
    is_type,
)


@dataclass
class Tag:
    id: UUID
    user: int
    title: str
    color: str
    picture: str
    show_income: bool
    show_outcome: bool
    budget_income: bool
    budget_outcome: bool
    changed: int
    static_id: Optional[int] = None
    icon: Optional[str] = None
    parent: Optional[UUID] = None
    required: Optional[bool] = None

    @staticmethod
    def from_dict(obj: dict) -> 'Tag':
        check_dict_type(obj)

        return Tag(
            id=UUID(obj.get("id")),
            user=from_int(obj.get("user")),
            color=from_none(obj.get("color")),
            title=from_str(obj.get("title")),
            changed=from_int(obj.get("changed")),
            picture=from_none(obj.get("picture")),
            static_id=from_union([from_none, lambda x: int(from_str(x))], obj.get("staticId")),
            show_income=from_bool(obj.get("showIncome")),
            show_outcome=from_bool(obj.get("showOutcome")),
            budget_income=from_bool(obj.get("budgetIncome")),
            budget_outcome=from_bool(obj.get("budgetOutcome")),
            icon=from_union([from_none, from_str], obj.get("icon")),
            parent=from_union([from_none, lambda x: UUID(x)], obj.get("parent")),
            required=from_union([from_bool, from_none], obj.get("required")),
        )

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "user": from_int(self.user),
            "color": from_none(self.color),
            "title": from_str(self.title),
            "changed": from_int(self.changed),
            "picture": from_none(self.picture),
            "staticId": from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x)),
                ],
                self.static_id,
            ),
            "showIncome": from_bool(self.show_income),
            "showOutcome": from_bool(self.show_outcome),
            "budgetIncome": from_bool(self.budget_income),
            "budgetOutcome": from_bool(self.budget_outcome),
            "icon": from_union([from_none, from_str], self.icon),
            "parent": from_union([from_none, lambda x: str(x)], self.parent),
            "required": from_union([from_bool, from_none], self.required),
        }
