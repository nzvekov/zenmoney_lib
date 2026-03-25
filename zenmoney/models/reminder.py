from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

from .base import DictMixin
from .enums import Interval


class Reminder(BaseModel, DictMixin):
    id: UUID
    user: int
    income: float
    outcome: float
    income_account: UUID = Field(alias="incomeAccount")
    outcome_account: UUID = Field(alias="outcomeAccount")
    income_instrument: int = Field(alias="incomeInstrument")
    outcome_instrument: int = Field(alias="outcomeInstrument")
    changed: int
    step: int | None = None
    notify: bool
    points: list[int] = Field(default_factory=list)
    start_date: datetime = Field(alias="startDate")
    tag: list[UUID] | None = None
    payee: str | None = None
    comment: str | None = None
    end_date: datetime | None = Field(None, alias="endDate")
    interval: Interval | None = None
    merchant: UUID | None = None

    model_config = {"populate_by_name": True}

    @field_validator("points", mode="before")
    @classmethod
    def points_none_to_empty(cls, v: object) -> list:
        return [] if v is None else v
