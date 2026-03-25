from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from .base import DictMixin


class Budget(BaseModel, DictMixin):
    date: datetime
    user: int
    income: float
    changed: int
    outcome: float
    income_lock: bool = Field(alias="incomeLock")
    outcome_lock: bool = Field(alias="outcomeLock")
    is_income_forecast: bool = Field(alias="isIncomeForecast")
    is_outcome_forecast: bool = Field(alias="isOutcomeForecast")
    tag: UUID | None = None

    model_config = {"populate_by_name": True}

    def to_dict(self) -> dict:
        data = super().to_dict()
        if self.tag is not None:
            data["tag"] = str(self.tag)
        return data
