from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from .utils import (
    check_dict_type,
    from_bool,
    from_datetime,
    from_float,
    from_int,
    from_none,
    from_union,
)


@dataclass
class Budget:
    date: datetime
    user: int
    income: float
    changed: int
    outcome: float
    income_lock: bool
    outcome_lock: bool
    is_income_forecast: bool
    is_outcome_forecast: bool
    tag: UUID | None = None

    @staticmethod
    def from_dict(obj: dict) -> 'Budget':
        check_dict_type(obj)

        return Budget(
            date=from_datetime(obj.get("date")),
            user=from_int(obj.get("user")),
            income=from_float(obj.get("income")),
            changed=from_int(obj.get("changed")),
            outcome=from_float(obj.get("outcome")),
            income_lock=from_bool(obj.get("incomeLock")),
            outcome_lock=from_bool(obj.get("outcomeLock")),
            is_income_forecast=from_bool(obj.get("isIncomeForecast")),
            is_outcome_forecast=from_bool(obj.get("isOutcomeForecast")),
            tag=from_union([from_none, lambda x: UUID(x)], obj.get("tag")),
        )

    def to_dict(self) -> dict:
        return {
            "date": self.date.isoformat(),
            "user": from_int(self.user),
            "income": from_float(self.income),
            "changed": from_int(self.changed),
            "outcome": from_float(self.outcome),
            "incomeLock": from_bool(self.income_lock),
            "outcomeLock": from_bool(self.outcome_lock),
            "isIncomeForecast": from_bool(self.is_income_forecast),
            "isOutcomeForecast": from_bool(self.is_outcome_forecast),
            "tag": from_union([from_none, lambda x: str(x)], self.tag),
        }
