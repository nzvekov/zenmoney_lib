from pydantic import BaseModel

from .base import DictMixin


class Country(BaseModel, DictMixin):
    model_config = {"populate_by_name": True}

    id: int
    title: str
    currency: int
    domain: str | None = None
