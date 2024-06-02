from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from .enums import State
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
class ReminderMarker:
    id: UUID
    user: int
    date: datetime
    income: float
    outcome: float
    income_account: UUID
    outcome_account: UUID
    income_instrument: int
    outcome_instrument: int
    changed: int
    state: State
    notify: bool
    reminder: UUID
    is_forecast: bool
    tag: Optional[List[UUID]] = None
    payee: Optional[str] = None
    comment: Optional[str] = None
    merchant: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: dict) -> 'ReminderMarker':
        check_dict_type(obj)

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
        return {
            "id": str(self.id),
            "date": self.date.isoformat(),
            "user": from_int(self.user),
            "state": to_enum(State, self.state),
            "income": to_float(self.income),
            "notify": from_bool(self.notify),
            "changed": from_int(self.changed),
            "outcome": to_float(self.outcome),
            "reminder": str(self.reminder),
            "isForecast": from_bool(self.is_forecast),
            "incomeAccount": str(self.income_account),
            "outcomeAccount": str(self.outcome_account),
            "incomeInstrument": from_int(self.income_instrument),
            "outcomeInstrument": from_int(self.outcome_instrument),
            "tag": from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.tag),
            "payee": from_union([from_none, from_str], self.payee),
            "comment": from_union([from_none, from_str], self.comment),
            "merchant": from_union([from_none, lambda x: str(x)], self.merchant),
        }
