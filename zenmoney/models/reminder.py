from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from .enums import Interval
from .utils import (
    check_dict_type,
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
class Reminder:
    id: UUID
    user: int
    income: float
    outcome: float
    income_account: UUID
    outcome_account: UUID
    income_instrument: int
    outcome_instrument: int
    changed: int
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
    def from_dict(obj: dict) -> 'Reminder':
        check_dict_type(obj)

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
        return {
            "id": str(self.id),
            "step": from_int(self.step),
            "user": from_int(self.user),
            "income": to_float(self.income),
            "notify": from_bool(self.notify),
            "points": from_list(from_int, self.points),
            "changed": from_int(self.changed),
            "outcome": to_float(self.outcome),
            "startDate": self.start_date.isoformat(),
            "incomeAccount": str(self.income_account),
            "outcomeAccount": str(self.outcome_account),
            "incomeInstrument": from_int(self.income_instrument),
            "outcomeInstrument": from_int(self.outcome_instrument),
            "tag": from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.tag),
            "payee": from_union([from_none, from_str], self.payee),
            "comment": from_union([from_none, from_str], self.comment),
            "endDate": from_union([from_none, lambda x: x.isoformat()], self.end_date),
            "interval": from_union([from_none, lambda x: to_enum(Interval, x)], self.interval),
            "merchant": from_union([from_none, lambda x: str(x)], self.merchant),
        }
