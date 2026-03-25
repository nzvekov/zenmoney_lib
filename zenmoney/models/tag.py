from uuid import UUID

from pydantic import BaseModel, Field

from .base import DictMixin


class Tag(BaseModel, DictMixin):
    id: UUID
    user: int
    title: str
    picture: str | None = None
    show_income: bool = Field(alias="showIncome")
    show_outcome: bool = Field(alias="showOutcome")
    budget_income: bool = Field(alias="budgetIncome")
    budget_outcome: bool = Field(alias="budgetOutcome")
    changed: int
    color: int | None = None
    static_id: int | None = Field(None, alias="staticId")
    icon: str | None = None
    parent: UUID | None = None
    required: bool | None = None

    model_config = {"populate_by_name": True}

    def to_dict(self) -> dict:
        data = super().to_dict()
        if self.static_id is not None:
            data["staticId"] = str(self.static_id)
        return data
