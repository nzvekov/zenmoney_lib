from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from .base import DictMixin
from .enums import State


class ReminderMarker(BaseModel, DictMixin):
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
    state: State
    notify: bool
    reminder: UUID
    is_forecast: bool = Field(alias="isForecast")
    tag: list[UUID] | None = None
    payee: str | None = None
    comment: str | None = None
    merchant: UUID | None = None

    model_config = {"populate_by_name": True}
