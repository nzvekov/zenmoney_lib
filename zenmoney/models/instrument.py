from dataclasses import dataclass

from .utils import check_dict_type, from_float, from_int, from_str, to_float


@dataclass
class Instrument:
    id: int
    title: str
    rate: float
    symbol: str
    changed: int
    short_title: str

    @staticmethod
    def from_dict(obj: dict) -> 'Instrument':
        check_dict_type(obj)

        return Instrument(
            id=from_int(obj.get("id")),
            rate=from_float(obj.get("rate")),
            title=from_str(obj.get("title")),
            symbol=from_str(obj.get("symbol")),
            changed=from_int(obj.get("changed")),
            short_title=from_str(obj.get("shortTitle")),
        )

    def to_dict(self) -> dict:
        return {
            "id": from_int(self.id),
            "rate": to_float(self.rate),
            "title": from_str(self.title),
            "symbol": from_str(self.symbol),
            "changed": from_int(self.changed),
            "shortTitle": from_str(self.short_title),
        }
