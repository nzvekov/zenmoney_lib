from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from .enums import Interval
from .mixins import BaseOperationMixin
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
class Reminder(BaseOperationMixin):
    step: int
    notify: bool
    points: List[int]
    start_date: datetime
    tag: Optional[List[UUID]] = None
    payee: Optional[str] = None
    comment: Optional[str] = None
    end_date: Optional[datetime] = None
    interval: Optional[Interval] = None
    merchant: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Reminder':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        return Reminder(
            id=UUID(obj.get("id")),
            step=from_int(obj.get("step")),
            user=from_int(obj.get("user")),
            income=from_float(obj.get("income")),
            notify=from_bool(obj.get("notify")),
            points=from_list(from_int, obj.get("points")),
            changed=from_int(obj.get("changed")),
            outcome=from_float(obj.get("outcome")),
            start_date=from_datetime(obj.get("startDate")),
            income_account=UUID(obj.get("incomeAccount")),
            outcome_account=UUID(obj.get("outcomeAccount")),
            income_instrument=from_int(obj.get("incomeInstrument")),
            outcome_instrument=from_int(obj.get("outcomeInstrument")),
            tag=from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("tag")),
            payee=from_union([from_none, from_str], obj.get("payee")),
            comment=from_union([from_none, from_str], obj.get("comment")),
            end_date=from_union([from_none, from_datetime], obj.get("endDate")),
            interval=from_union([from_none, Interval], obj.get("interval")),
            merchant=from_union([from_none, lambda x: UUID(x)], obj.get("merchant")),
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
        result["startDate"] = self.start_date.isoformat()
        result["incomeAccount"] = str(self.income_account)
        result["outcomeAccount"] = str(self.outcome_account)
        result["incomeInstrument"] = from_int(self.income_instrument)
        result["outcomeInstrument"] = from_int(self.outcome_instrument)
        result["tag"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.tag)
        result["payee"] = from_union([from_none, from_str], self.payee)
        result["comment"] = from_union([from_none, from_str], self.comment)
        result["endDate"] = from_union([from_none, lambda x: x.isoformat()], self.end_date)
        result["interval"] = from_union([from_none, lambda x: to_enum(Interval, x)], self.interval)
        result["merchant"] = from_union([from_none, lambda x: str(x)], self.merchant)
        return result
