from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from .enums import BalanceCorrectionType, Interval, TypeEnum
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
class Account:
    id: UUID
    user: int
    title: str
    type: TypeEnum
    archive: bool
    balance: float
    private: bool
    savings: bool
    enable_sms: bool
    in_balance: bool
    instrument: int
    credit_limit: float
    start_balance: float
    enable_correction: bool
    balance_correction_type: BalanceCorrectionType
    changed: int
    role: Optional[int] = None
    sync_id: Optional[List[str]] = None
    company: Optional[int] = None
    percent: Optional[float] = None
    start_date: Optional[datetime] = None
    payoff_step: Optional[int] = None
    end_date_offset: Optional[int] = None
    capitalization: Optional[bool] = None
    payoff_interval: Optional[Interval] = None
    end_date_offset_interval: Optional[Interval] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Account':
        check_dict_type(obj)

        return Account(
            id=UUID(obj.get("id")),
            type=TypeEnum(obj.get("type")),
            user=from_int(obj.get("user")),
            title=from_str(obj.get("title")),
            archive=from_bool(obj.get("archive")),
            balance=from_float(obj.get("balance")),
            changed=from_int(obj.get("changed")),
            private=from_bool(obj.get("private")),
            savings=from_bool(obj.get("savings")),
            enable_sms=from_bool(obj.get("enableSMS")),
            in_balance=from_bool(obj.get("inBalance")),
            instrument=from_int(obj.get("instrument")),
            credit_limit=from_float(obj.get("creditLimit")),
            start_balance=from_float(obj.get("startBalance")),
            enable_correction=from_bool(obj.get("enableCorrection")),
            balance_correction_type=BalanceCorrectionType(obj.get("balanceCorrectionType")),
            role=from_union([from_none, from_int], obj.get("role")),
            sync_id=from_union([from_none, lambda x: from_list(from_str, x)], obj.get("syncID")),
            company=from_union([from_none, from_int], obj.get("company")),
            percent=from_union([from_none, from_float], obj.get("percent")),
            start_date=from_union([from_none, from_datetime], obj.get("startDate")),
            payoff_step=from_union([from_none, from_int], obj.get("payoffStep")),
            end_date_offset=from_union([from_none, from_int], obj.get("endDateOffset")),
            capitalization=from_union([from_bool, from_none], obj.get("capitalization")),
            payoff_interval=from_union([from_none, Interval], obj.get("payoffInterval")),
            end_date_offset_interval=from_union([from_none, Interval], obj.get("endDateOffsetInterval")),
        )

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "type": to_enum(TypeEnum, self.type),
            "user": from_int(self.user),
            "title": from_str(self.title),
            "archive": from_bool(self.archive),
            "balance": to_float(self.balance),
            "changed": from_int(self.changed),
            "private": from_bool(self.private),
            "savings": from_bool(self.savings),
            "enableSMS": from_bool(self.enable_sms),
            "inBalance": from_bool(self.in_balance),
            "instrument": from_int(self.instrument),
            "creditLimit": to_float(self.credit_limit),
            "startBalance": to_float(self.start_balance),
            "enableCorrection": from_bool(self.enable_correction),
            "balanceCorrectionType": to_enum(BalanceCorrectionType, self.balance_correction_type),
            "role": from_union([from_none, from_int], self.role),
            "syncID": from_union([from_none, lambda x: from_list(from_str, x)], self.sync_id),
            "company": from_union([from_none, from_int], self.company),
            "percent": from_union([from_none, to_float], self.percent),
            "startDate": from_union([from_none, lambda x: x.isoformat()], self.start_date),
            "payoffStep": from_union([from_none, from_int], self.payoff_step),
            "endDateOffset": from_union([from_none, from_int], self.end_date_offset),
            "capitalization": from_union([from_bool, from_none], self.capitalization),
            "payoffInterval": from_union([from_none, lambda x: to_enum(Interval, x)], self.payoff_interval),
            "endDateOffsetInterval": from_union(
                [from_none, lambda x: to_enum(Interval, x)], self.end_date_offset_interval
            ),
        }
