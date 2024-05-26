from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from .utils import from_bool, from_datetime, from_int, from_none, from_union


@dataclass
class Budget:
    date: datetime
    user: int
    income: int
    changed: int
    outcome: int
    incomeLock: bool
    outcomeLock: bool
    isIncomeForecast: bool
    isOutcomeForecast: bool
    tag: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Budget':
        assert isinstance(obj, dict)
        date = from_datetime(obj.get("date"))
        user = from_int(obj.get("user"))
        income = from_int(obj.get("income"))
        changed = from_int(obj.get("changed"))
        outcome = from_int(obj.get("outcome"))
        incomeLock = from_bool(obj.get("incomeLock"))
        outcomeLock = from_bool(obj.get("outcomeLock"))
        isIncomeForecast = from_bool(obj.get("isIncomeForecast"))
        isOutcomeForecast = from_bool(obj.get("isOutcomeForecast"))
        tag = from_union([from_none, lambda x: UUID(x)], obj.get("tag"))
        return Budget(
            date, user, income, changed, outcome, incomeLock, outcomeLock, isIncomeForecast, isOutcomeForecast, tag
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["date"] = self.date.isoformat()
        result["user"] = from_int(self.user)
        result["income"] = from_int(self.income)
        result["changed"] = from_int(self.changed)
        result["outcome"] = from_int(self.outcome)
        result["incomeLock"] = from_bool(self.incomeLock)
        result["outcomeLock"] = from_bool(self.outcomeLock)
        result["isIncomeForecast"] = from_bool(self.isIncomeForecast)
        result["isOutcomeForecast"] = from_bool(self.isOutcomeForecast)
        result["tag"] = from_union([from_none, lambda x: str(x)], self.tag)
        return result
