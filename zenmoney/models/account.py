from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from .enums import BalanceCorrectionType, Interval, TypeEnum
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
class Account:
    id: UUID
    type: TypeEnum
    user: int
    title: str
    archive: bool
    balance: float
    changed: int
    private: bool
    savings: bool
    enableSMS: bool
    inBalance: bool
    instrument: int
    creditLimit: float
    startBalance: float
    enableCorrection: bool
    balanceCorrectionType: BalanceCorrectionType
    role: Optional[int] = None
    syncID: Optional[List[str]] = None
    company: Optional[int] = None
    percent: Optional[float] = None
    startDate: Optional[datetime] = None
    payoffStep: Optional[int] = None
    endDateOffset: Optional[int] = None
    capitalization: Optional[bool] = None
    payoffInterval: Optional[Interval] = None
    endDateOffsetInterval: Optional[Interval] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Account':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

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
            enableSMS=from_bool(obj.get("enableSMS")),
            inBalance=from_bool(obj.get("inBalance")),
            instrument=from_int(obj.get("instrument")),
            creditLimit=from_float(obj.get("creditLimit")),
            startBalance=from_float(obj.get("startBalance")),
            enableCorrection=from_bool(obj.get("enableCorrection")),
            balanceCorrectionType=BalanceCorrectionType(obj.get("balanceCorrectionType")),
            role=from_union([from_none, from_int], obj.get("role")),
            syncID=from_union([from_none, lambda x: from_list(from_str, x)], obj.get("syncID")),
            company=from_union([from_none, from_int], obj.get("company")),
            percent=from_union([from_none, from_float], obj.get("percent")),
            startDate=from_union([from_none, from_datetime], obj.get("startDate")),
            payoffStep=from_union([from_none, from_int], obj.get("payoffStep")),
            endDateOffset=from_union([from_none, from_int], obj.get("endDateOffset")),
            capitalization=from_union([from_bool, from_none], obj.get("capitalization")),
            payoffInterval=from_union([from_none, Interval], obj.get("payoffInterval")),
            endDateOffsetInterval=from_union([from_none, Interval], obj.get("endDateOffsetInterval")),
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = str(self.id)
        result["type"] = to_enum(TypeEnum, self.type)
        result["user"] = from_int(self.user)
        result["title"] = from_str(self.title)
        result["archive"] = from_bool(self.archive)
        result["balance"] = to_float(self.balance)
        result["changed"] = from_int(self.changed)
        result["private"] = from_bool(self.private)
        result["savings"] = from_bool(self.savings)
        result["enableSMS"] = from_bool(self.enableSMS)
        result["inBalance"] = from_bool(self.inBalance)
        result["instrument"] = from_int(self.instrument)
        result["creditLimit"] = to_float(self.creditLimit)
        result["startBalance"] = to_float(self.startBalance)
        result["enableCorrection"] = from_bool(self.enableCorrection)
        result["balanceCorrectionType"] = to_enum(BalanceCorrectionType, self.balanceCorrectionType)
        result["role"] = from_union([from_none, from_int], self.role)
        result["syncID"] = from_union([from_none, lambda x: from_list(from_str, x)], self.syncID)
        result["company"] = from_union([from_none, from_int], self.company)
        result["percent"] = from_union([from_none, to_float], self.percent)
        result["startDate"] = from_union([from_none, lambda x: x.isoformat()], self.startDate)
        result["payoffStep"] = from_union([from_none, from_int], self.payoffStep)
        result["endDateOffset"] = from_union([from_none, from_int], self.endDateOffset)
        result["capitalization"] = from_union([from_bool, from_none], self.capitalization)
        result["payoffInterval"] = from_union([from_none, lambda x: to_enum(Interval, x)], self.payoffInterval)
        result["endDateOffsetInterval"] = from_union(
            [from_none, lambda x: to_enum(Interval, x)], self.endDateOffsetInterval
        )
        return result
