from dataclasses import dataclass
from typing import Any, Optional

from .utils import from_bool, from_int, from_none, from_str, from_union


@dataclass
class Company:
    id: int
    title: str
    changed: int
    deleted: bool
    www: Optional[str] = None
    country: Optional[int] = None
    fullTitle: Optional[str] = None
    countryCode: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Company':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        id = from_int(obj.get("id"))
        title = from_str(obj.get("title"))
        changed = from_int(obj.get("changed"))
        deleted = from_bool(obj.get("deleted"))
        www = from_union([from_none, from_str], obj.get("www"))
        country = from_union([from_none, from_int], obj.get("country"))
        fullTitle = from_union([from_none, from_str], obj.get("fullTitle"))
        countryCode = from_union([from_none, from_str], obj.get("countryCode"))
        return Company(id, title, changed, deleted, www, country, fullTitle, countryCode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["title"] = from_str(self.title)
        result["changed"] = from_int(self.changed)
        result["deleted"] = from_bool(self.deleted)
        result["www"] = from_union([from_none, from_str], self.www)
        result["country"] = from_union([from_none, from_int], self.country)
        result["fullTitle"] = from_union([from_none, from_str], self.fullTitle)
        result["countryCode"] = from_union([from_none, from_str], self.countryCode)
        return result
