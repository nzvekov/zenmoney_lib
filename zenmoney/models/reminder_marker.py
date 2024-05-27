from dataclasses import dataclass
from typing import Any, List, Optional
from uuid import UUID

from .enums import State
from .mixins import BaseRealOperationMixin
from .utils import (
    from_bool,
    from_datetime,
    from_float,
    from_int,
    from_list,
    from_none,
    from_str,
    from_union,
    to_enum,
    to_float,
)


@dataclass
class ReminderMarker(BaseRealOperationMixin):
    state: State
    notify: bool
    reminder: UUID
    is_forecast: bool
    tag: Optional[List[UUID]] = None
    payee: Optional[str] = None
    comment: Optional[str] = None
    merchant: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReminderMarker':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        return ReminderMarker(
            id=UUID(obj.get("id")),
            date=from_datetime(obj.get("date")),
            user=from_int(obj.get("user")),
            state=State(obj.get("state")),
            income=from_float(obj.get("income")),
            notify=from_bool(obj.get("notify")),
            changed=from_int(obj.get("changed")),
            outcome=from_float(obj.get("outcome")),
            reminder=UUID(obj.get("reminder")),
            is_forecast=from_bool(obj.get("isForecast")),
            income_account=UUID(obj.get("incomeAccount")),
            outcome_account=UUID(obj.get("outcomeAccount")),
            income_instrument=from_int(obj.get("incomeInstrument")),
            outcome_instrument=from_int(obj.get("outcomeInstrument")),
            tag=from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("tag")),
            payee=from_union([from_none, from_str], obj.get("payee")),
            comment=from_union([from_none, from_str], obj.get("comment")),
            merchant=from_union([from_none, lambda x: UUID(x)], obj.get("merchant")),
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = str(self.id)
        result["date"] = self.date.isoformat()
        result["user"] = from_int(self.user)
        result["state"] = to_enum(State, self.state)
        result["income"] = to_float(self.income)
        result["notify"] = from_bool(self.notify)
        result["changed"] = from_int(self.changed)
        result["outcome"] = to_float(self.outcome)
        result["reminder"] = str(self.reminder)
        result["isForecast"] = from_bool(self.is_forecast)
        result["incomeAccount"] = str(self.income_account)
        result["outcomeAccount"] = str(self.outcome_account)
        result["incomeInstrument"] = from_int(self.income_instrument)
        result["outcomeInstrument"] = from_int(self.outcome_instrument)
        result["tag"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.tag)
        result["payee"] = from_union([from_none, from_str], self.payee)
        result["comment"] = from_union([from_none, from_str], self.comment)
        result["merchant"] = from_union([from_none, lambda x: str(x)], self.merchant)
        return result
