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
    income_lock: bool
    outcome_lock: bool
    is_income_forecast: bool
    is_outcome_forecast: bool
    tag: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Budget':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        return Budget(
            date=from_datetime(obj.get("date")),
            user=from_int(obj.get("user")),
            income=from_int(obj.get("income")),
            changed=from_int(obj.get("changed")),
            outcome=from_int(obj.get("outcome")),
            income_lock=from_bool(obj.get("incomeLock")),
            outcome_lock=from_bool(obj.get("outcomeLock")),
            is_income_forecast=from_bool(obj.get("isIncomeForecast")),
            is_outcome_forecast=from_bool(obj.get("isOutcomeForecast")),
            tag=from_union([from_none, lambda x: UUID(x)], obj.get("tag")),
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["date"] = self.date.isoformat()
        result["user"] = from_int(self.user)
        result["income"] = from_int(self.income)
        result["changed"] = from_int(self.changed)
        result["outcome"] = from_int(self.outcome)
        result["incomeLock"] = from_bool(self.income_lock)
        result["outcomeLock"] = from_bool(self.outcome_lock)
        result["isIncomeForecast"] = from_bool(self.is_income_forecast)
        result["isOutcomeForecast"] = from_bool(self.is_outcome_forecast)
        result["tag"] = from_union([from_none, lambda x: str(x)], self.tag)
        return result
