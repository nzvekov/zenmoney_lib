from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Any
from uuid import UUID

from .enum import State
from .helpers import (
    from_datetime,
    from_int,
    from_float,
    from_bool,
    from_list,
    from_union,
    from_none,
    from_str,
    to_enum,
    to_float,
)


@dataclass
class ReminderMarker:
    id: UUID
    date: datetime
    user: int
    state: State
    income: float
    notify: bool
    changed: int
    outcome: float
    reminder: UUID
    isForecast: bool
    incomeAccount: UUID
    outcomeAccount: UUID
    incomeInstrument: int
    outcomeInstrument: int
    tag: Optional[List[UUID]] = None
    payee: Optional[str] = None
    comment: Optional[str] = None
    merchant: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReminderMarker':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        id = UUID(obj.get("id"))
        date = from_datetime(obj.get("date"))
        user = from_int(obj.get("user"))
        state = State(obj.get("state"))
        income = from_float(obj.get("income"))
        notify = from_bool(obj.get("notify"))
        changed = from_int(obj.get("changed"))
        outcome = from_float(obj.get("outcome"))
        reminder = UUID(obj.get("reminder"))
        isForecast = from_bool(obj.get("isForecast"))
        incomeAccount = UUID(obj.get("incomeAccount"))
        outcomeAccount = UUID(obj.get("outcomeAccount"))
        incomeInstrument = from_int(obj.get("incomeInstrument"))
        outcomeInstrument = from_int(obj.get("outcomeInstrument"))
        tag = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("tag"))
        payee = from_union([from_none, from_str], obj.get("payee"))
        comment = from_union([from_none, from_str], obj.get("comment"))
        merchant = from_union([from_none, lambda x: UUID(x)], obj.get("merchant"))
        return ReminderMarker(
            id,
            date,
            user,
            state,
            income,
            notify,
            changed,
            outcome,
            reminder,
            isForecast,
            incomeAccount,
            outcomeAccount,
            incomeInstrument,
            outcomeInstrument,
            tag,
            payee,
            comment,
            merchant,
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
        result["isForecast"] = from_bool(self.isForecast)
        result["incomeAccount"] = str(self.incomeAccount)
        result["outcomeAccount"] = str(self.outcomeAccount)
        result["incomeInstrument"] = from_int(self.incomeInstrument)
        result["outcomeInstrument"] = from_int(self.outcomeInstrument)
        result["tag"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.tag)
        result["payee"] = from_union([from_none, from_str], self.payee)
        result["comment"] = from_union([from_none, from_str], self.comment)
        result["merchant"] = from_union([from_none, lambda x: str(x)], self.merchant)
        return result
