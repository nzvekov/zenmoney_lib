from dataclasses import dataclass
from typing import Optional, Any

from .helpers import from_int, from_str, from_union, from_none


@dataclass
class Country:
    id: int
    title: str
    currency: int
    domain: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Country':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        id = from_int(obj.get("id"))
        title = from_str(obj.get("title"))
        currency = from_int(obj.get("currency"))
        domain = from_union([from_none, from_str], obj.get("domain"))
        return Country(id, title, currency, domain)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["title"] = from_str(self.title)
        result["currency"] = from_int(self.currency)
        result["domain"] = from_union([from_none, from_str], self.domain)
        return result
