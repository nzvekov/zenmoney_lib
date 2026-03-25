from pydantic import BaseModel, Field

from .base import DictMixin


class Company(BaseModel, DictMixin):
    id: int
    title: str
    deleted: bool
    changed: int
    www: str | None = None
    country: int | None = None
    full_title: str | None = Field(None, alias="fullTitle")
    country_code: str | None = Field(None, alias="countryCode")

    model_config = {"populate_by_name": True}
