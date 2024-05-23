from dataclasses import dataclass
from typing import Any

from .helpers import from_int, from_float, from_str, to_float


@dataclass
class Instrument:
    id: int
    rate: float
    title: str
    symbol: str
    changed: int
    shortTitle: str

    @staticmethod
    def from_dict(obj: Any) -> 'Instrument':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        id = from_int(obj.get("id"))
        rate = from_float(obj.get("rate"))
        title = from_str(obj.get("title"))
        symbol = from_str(obj.get("symbol"))
        changed = from_int(obj.get("changed"))
        shortTitle = from_str(obj.get("shortTitle"))
        return Instrument(id, rate, title, symbol, changed, shortTitle)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["rate"] = to_float(self.rate)
        result["title"] = from_str(self.title)
        result["symbol"] = from_str(self.symbol)
        result["changed"] = from_int(self.changed)
        result["shortTitle"] = from_str(self.shortTitle)
        return result
