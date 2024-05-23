from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Any
from uuid import UUID

from zenmoney.enum import Source
from zenmoney.helpers import (
    from_datetime,
    from_int,
    from_float,
    from_bool,
    from_none,
    from_union,
    from_list,
    from_str,
    to_float,
    to_enum,
)


@dataclass
class Transaction:
    id: UUID
    date: datetime
    user: int
    income: float
    viewed: bool
    changed: int
    created: int
    deleted: bool
    outcome: float
    incomeAccount: UUID
    outcomeAccount: UUID
    incomeInstrument: int
    outcomeInstrument: int
    opIncomeInstrument: None
    opOutcomeInstrument: None
    tag: Optional[List[UUID]] = None
    hold: Optional[bool] = None
    payee: Optional[str] = None
    qrCode: Optional[str] = None
    source: Optional[Source] = None
    comment: Optional[str] = None
    latitude: Optional[float] = None
    merchant: Optional[UUID] = None
    opIncome: Optional[int] = None
    longitude: Optional[float] = None
    opOutcome: Optional[int] = None
    incomeBankID: Optional[str] = None
    originalPayee: Optional[str] = None
    outcomeBankID: Optional[str] = None
    reminderMarker: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Transaction':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        id = UUID(obj.get("id"))
        date = from_datetime(obj.get("date"))
        user = from_int(obj.get("user"))
        income = from_float(obj.get("income"))
        viewed = from_bool(obj.get("viewed"))
        changed = from_int(obj.get("changed"))
        created = from_int(obj.get("created"))
        deleted = from_bool(obj.get("deleted"))
        outcome = from_float(obj.get("outcome"))
        incomeAccount = UUID(obj.get("incomeAccount"))
        outcomeAccount = UUID(obj.get("outcomeAccount"))
        incomeInstrument = from_int(obj.get("incomeInstrument"))
        outcomeInstrument = from_int(obj.get("outcomeInstrument"))
        opIncomeInstrument = from_none(obj.get("opIncomeInstrument"))
        opOutcomeInstrument = from_none(obj.get("opOutcomeInstrument"))
        tag = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("tag"))
        hold = from_union([from_bool, from_none], obj.get("hold"))
        payee = from_union([from_none, from_str], obj.get("payee"))
        qrCode = from_union([from_none, from_str], obj.get("qrCode"))
        source = from_union([from_none, Source], obj.get("source"))
        comment = from_union([from_none, from_str], obj.get("comment"))
        latitude = from_union([from_none, from_float], obj.get("latitude"))
        merchant = from_union([from_none, lambda x: UUID(x)], obj.get("merchant"))
        opIncome = from_union([from_none, from_int], obj.get("opIncome"))
        longitude = from_union([from_none, from_float], obj.get("longitude"))
        opOutcome = from_union([from_none, from_int], obj.get("opOutcome"))
        incomeBankID = from_union([from_none, from_str], obj.get("incomeBankID"))
        originalPayee = from_union([from_none, from_str], obj.get("originalPayee"))
        outcomeBankID = from_union([from_none, from_str], obj.get("outcomeBankID"))
        reminderMarker = from_union([from_none, lambda x: UUID(x)], obj.get("reminderMarker"))
        return Transaction(
            id,
            date,
            user,
            income,
            viewed,
            changed,
            created,
            deleted,
            outcome,
            incomeAccount,
            outcomeAccount,
            incomeInstrument,
            outcomeInstrument,
            opIncomeInstrument,
            opOutcomeInstrument,
            tag,
            hold,
            payee,
            qrCode,
            source,
            comment,
            latitude,
            merchant,
            opIncome,
            longitude,
            opOutcome,
            incomeBankID,
            originalPayee,
            outcomeBankID,
            reminderMarker,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = str(self.id)
        result["date"] = self.date.isoformat()
        result["user"] = from_int(self.user)
        result["income"] = to_float(self.income)
        result["viewed"] = from_bool(self.viewed)
        result["changed"] = from_int(self.changed)
        result["created"] = from_int(self.created)
        result["deleted"] = from_bool(self.deleted)
        result["outcome"] = to_float(self.outcome)
        result["incomeAccount"] = str(self.incomeAccount)
        result["outcomeAccount"] = str(self.outcomeAccount)
        result["incomeInstrument"] = from_int(self.incomeInstrument)
        result["outcomeInstrument"] = from_int(self.outcomeInstrument)
        result["opIncomeInstrument"] = from_none(self.opIncomeInstrument)
        result["opOutcomeInstrument"] = from_none(self.opOutcomeInstrument)
        result["tag"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.tag)
        result["hold"] = from_union([from_bool, from_none], self.hold)
        result["payee"] = from_union([from_none, from_str], self.payee)
        result["qrCode"] = from_union([from_none, from_str], self.qrCode)
        result["source"] = from_union([from_none, lambda x: to_enum(Source, x)], self.source)
        result["comment"] = from_union([from_none, from_str], self.comment)
        result["latitude"] = from_union([from_none, to_float], self.latitude)
        result["merchant"] = from_union([from_none, lambda x: str(x)], self.merchant)
        result["opIncome"] = from_union([from_none, from_int], self.opIncome)
        result["longitude"] = from_union([from_none, to_float], self.longitude)
        result["opOutcome"] = from_union([from_none, from_int], self.opOutcome)
        result["incomeBankID"] = from_union([from_none, from_str], self.incomeBankID)
        result["originalPayee"] = from_union([from_none, from_str], self.originalPayee)
        result["outcomeBankID"] = from_union([from_none, from_str], self.outcomeBankID)
        result["reminderMarker"] = from_union([from_none, lambda x: str(x)], self.reminderMarker)
        return result
