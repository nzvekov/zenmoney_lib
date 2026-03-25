from pydantic import BaseModel, Field

from .base import DictMixin


class Instrument(BaseModel, DictMixin):
    id: int
    title: str
    rate: float
    symbol: str
    changed: int
    short_title: str = Field(alias="shortTitle")

    model_config = {"populate_by_name": True}
