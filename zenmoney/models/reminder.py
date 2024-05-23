from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Any
from uuid import UUID

from zenmoney.enum import Interval
from zenmoney.helpers import (
    from_int,
    from_float,
    from_bool,
    from_list,
    from_datetime,
    from_union,
    from_none,
    from_str,
    to_float,
    to_enum,
)


@dataclass
class Reminder:
    id: UUID
    step: int
    user: int
    income: float
    notify: bool
    points: List[int]
    changed: int
    outcome: float
    startDate: datetime
    incomeAccount: UUID
    outcomeAccount: UUID
    incomeInstrument: int
    outcomeInstrument: int
    tag: Optional[List[UUID]] = None
    payee: Optional[str] = None
    comment: Optional[str] = None
    endDate: Optional[datetime] = None
    interval: Optional[Interval] = None
    merchant: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Reminder':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        id = UUID(obj.get("id"))
        step = from_int(obj.get("step"))
        user = from_int(obj.get("user"))
        income = from_float(obj.get("income"))
        notify = from_bool(obj.get("notify"))
        points = from_list(from_int, obj.get("points"))
        changed = from_int(obj.get("changed"))
        outcome = from_float(obj.get("outcome"))
        startDate = from_datetime(obj.get("startDate"))
        incomeAccount = UUID(obj.get("incomeAccount"))
        outcomeAccount = UUID(obj.get("outcomeAccount"))
        incomeInstrument = from_int(obj.get("incomeInstrument"))
        outcomeInstrument = from_int(obj.get("outcomeInstrument"))
        tag = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("tag"))
        payee = from_union([from_none, from_str], obj.get("payee"))
        comment = from_union([from_none, from_str], obj.get("comment"))
        endDate = from_union([from_none, from_datetime], obj.get("endDate"))
        interval = from_union([from_none, Interval], obj.get("interval"))
        merchant = from_union([from_none, lambda x: UUID(x)], obj.get("merchant"))
        return Reminder(
            id,
            step,
            user,
            income,
            notify,
            points,
            changed,
            outcome,
            startDate,
            incomeAccount,
            outcomeAccount,
            incomeInstrument,
            outcomeInstrument,
            tag,
            payee,
            comment,
            endDate,
            interval,
            merchant,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = str(self.id)
        result["step"] = from_int(self.step)
        result["user"] = from_int(self.user)
        result["income"] = to_float(self.income)
        result["notify"] = from_bool(self.notify)
        result["points"] = from_list(from_int, self.points)
        result["changed"] = from_int(self.changed)
        result["outcome"] = to_float(self.outcome)
        result["startDate"] = self.startDate.isoformat()
        result["incomeAccount"] = str(self.incomeAccount)
        result["outcomeAccount"] = str(self.outcomeAccount)
        result["incomeInstrument"] = from_int(self.incomeInstrument)
        result["outcomeInstrument"] = from_int(self.outcomeInstrument)
        result["tag"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.tag)
        result["payee"] = from_union([from_none, from_str], self.payee)
        result["comment"] = from_union([from_none, from_str], self.comment)
        result["endDate"] = from_union([from_none, lambda x: x.isoformat()], self.endDate)
        result["interval"] = from_union([from_none, lambda x: to_enum(Interval, x)], self.interval)
        result["merchant"] = from_union([from_none, lambda x: str(x)], self.merchant)
        return result
