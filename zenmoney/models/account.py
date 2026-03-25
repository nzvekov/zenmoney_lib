from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from .base import DictMixin
from .enums import BalanceCorrectionType, Interval, TypeEnum


class Account(BaseModel, DictMixin):
    id: UUID
    user: int
    title: str
    type: TypeEnum
    archive: bool
    balance: float
    private: bool
    enable_sms: bool = Field(alias="enableSMS")
    in_balance: bool = Field(alias="inBalance")
    instrument: int
    credit_limit: float = Field(alias="creditLimit")
    start_balance: float = Field(alias="startBalance")
    enable_correction: bool = Field(alias="enableCorrection")
    balance_correction_type: BalanceCorrectionType = Field(alias="balanceCorrectionType")
    changed: int
    savings: bool | None = None
    role: int | None = None
    sync_id: list[str] | None = Field(None, alias="syncID")
    company: int | None = None
    percent: float | None = None
    start_date: datetime | None = Field(None, alias="startDate")
    payoff_step: int | None = Field(None, alias="payoffStep")
    end_date_offset: int | None = Field(None, alias="endDateOffset")
    capitalization: bool | None = None
    payoff_interval: Interval | None = Field(None, alias="payoffInterval")
    end_date_offset_interval: Interval | None = Field(None, alias="endDateOffsetInterval")

    model_config = {"populate_by_name": True}
