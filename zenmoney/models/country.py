from dataclasses import dataclass
from typing import Optional

from .utils import check_dict_type, from_int, from_none, from_str, from_union


@dataclass
class Country:
    id: int
    title: str
    currency: int
    domain: Optional[str] = None

    @staticmethod
    def from_dict(obj: dict) -> 'Country':
        check_dict_type(obj)

        return Country(
            id=from_int(obj.get("id")),
            title=from_str(obj.get("title")),
            currency=from_int(obj.get("currency")),
            domain=from_union([from_none, from_str], obj.get("domain")),
        )

    def to_dict(self) -> dict:
        return {
            "id": from_int(self.id),
            "title": from_str(self.title),
            "currency": from_int(self.currency),
            "domain": from_union([from_none, from_str], self.domain),
        }
