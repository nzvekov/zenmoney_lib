from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from .base import DictMixin
from .enums import Source


class Transaction(BaseModel, DictMixin):
    id: UUID
    user: int
    date: datetime
    income: float
    outcome: float
    income_account: UUID = Field(alias="incomeAccount")
    outcome_account: UUID = Field(alias="outcomeAccount")
    income_instrument: int = Field(alias="incomeInstrument")
    outcome_instrument: int = Field(alias="outcomeInstrument")
    changed: int
    viewed: bool
    created: int
    deleted: bool
    op_income_instrument: int | None = Field(None, alias="opIncomeInstrument")
    op_outcome_instrument: int | None = Field(None, alias="opOutcomeInstrument")
    tag: list[UUID] | None = None
    hold: bool | None = None
    payee: str | None = None
    qr_code: str | None = Field(None, alias="qrCode")
    source: Source | None = None
    comment: str | None = None
    latitude: float | None = None
    merchant: UUID | None = None
    op_income: float | None = Field(None, alias="opIncome")
    longitude: float | None = None
    op_outcome: float | None = Field(None, alias="opOutcome")
    income_bank_id: str | None = Field(None, alias="incomeBankID")
    original_payee: str | None = Field(None, alias="originalPayee")
    outcome_bank_id: str | None = Field(None, alias="outcomeBankID")
    reminder_marker: UUID | None = Field(None, alias="reminderMarker")

    model_config = {"populate_by_name": True}
