from dataclasses import dataclass
from typing import Any, List, Optional
from uuid import UUID

from .enums import Source
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
class Transaction(BaseRealOperationMixin):
    viewed: bool
    created: int
    deleted: bool
    op_income_instrument: Optional[int] = None
    op_outcome_instrument: Optional[int] = None
    tag: Optional[List[UUID]] = None
    hold: Optional[bool] = None
    payee: Optional[str] = None
    qr_code: Optional[str] = None
    source: Optional[Source] = None
    comment: Optional[str] = None
    latitude: Optional[float] = None
    merchant: Optional[UUID] = None
    op_income: Optional[int] = None
    longitude: Optional[float] = None
    op_outcome: Optional[int] = None
    income_bank_id: Optional[str] = None
    original_payee: Optional[str] = None
    outcome_bank_id: Optional[str] = None
    reminder_marker: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Transaction':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        return Transaction(
            id=UUID(obj.get("id")),
            date=from_datetime(obj.get("date")),
            user=from_int(obj.get("user")),
            income=from_float(obj.get("income")),
            viewed=from_bool(obj.get("viewed")),
            changed=from_int(obj.get("changed")),
            created=from_int(obj.get("created")),
            deleted=from_bool(obj.get("deleted")),
            outcome=from_float(obj.get("outcome")),
            income_account=UUID(obj.get("incomeAccount")),
            outcome_account=UUID(obj.get("outcomeAccount")),
            income_instrument=from_int(obj.get("incomeInstrument")),
            outcome_instrument=from_int(obj.get("outcomeInstrument")),
            op_income_instrument=from_none(obj.get("opIncomeInstrument")),
            op_outcome_instrument=from_none(obj.get("opOutcomeInstrument")),
            tag=from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("tag")),
            hold=from_union([from_bool, from_none], obj.get("hold")),
            payee=from_union([from_none, from_str], obj.get("payee")),
            qr_code=from_union([from_none, from_str], obj.get("qrCode")),
            source=from_union([from_none, Source], obj.get("source")),
            comment=from_union([from_none, from_str], obj.get("comment")),
            latitude=from_union([from_none, from_float], obj.get("latitude")),
            merchant=from_union([from_none, lambda x: UUID(x)], obj.get("merchant")),
            op_income=from_union([from_none, from_int], obj.get("opIncome")),
            longitude=from_union([from_none, from_float], obj.get("longitude")),
            op_outcome=from_union([from_none, from_int], obj.get("opOutcome")),
            income_bank_id=from_union([from_none, from_str], obj.get("incomeBankID")),
            original_payee=from_union([from_none, from_str], obj.get("originalPayee")),
            outcome_bank_id=from_union([from_none, from_str], obj.get("outcomeBankID")),
            reminder_marker=from_union([from_none, lambda x: UUID(x)], obj.get("reminderMarker")),
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
        result["incomeAccount"] = str(self.income_account)
        result["outcomeAccount"] = str(self.outcome_account)
        result["incomeInstrument"] = from_int(self.income_instrument)
        result["outcomeInstrument"] = from_int(self.outcome_instrument)
        result["opIncomeInstrument"] = from_none(self.op_income_instrument)
        result["opOutcomeInstrument"] = from_none(self.op_outcome_instrument)
        result["tag"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.tag)
        result["hold"] = from_union([from_bool, from_none], self.hold)
        result["payee"] = from_union([from_none, from_str], self.payee)
        result["qrCode"] = from_union([from_none, from_str], self.qr_code)
        result["source"] = from_union([from_none, lambda x: to_enum(Source, x)], self.source)
        result["comment"] = from_union([from_none, from_str], self.comment)
        result["latitude"] = from_union([from_none, to_float], self.latitude)
        result["merchant"] = from_union([from_none, lambda x: str(x)], self.merchant)
        result["opIncome"] = from_union([from_none, from_int], self.op_income)
        result["longitude"] = from_union([from_none, to_float], self.longitude)
        result["opOutcome"] = from_union([from_none, from_int], self.op_outcome)
        result["incomeBankID"] = from_union([from_none, from_str], self.income_bank_id)
        result["originalPayee"] = from_union([from_none, from_str], self.original_payee)
        result["outcomeBankID"] = from_union([from_none, from_str], self.outcome_bank_id)
        result["reminderMarker"] = from_union([from_none, lambda x: str(x)], self.reminder_marker)
        return result
