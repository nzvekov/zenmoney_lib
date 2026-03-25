from uuid import UUID

from pydantic import BaseModel

from .base import DictMixin


class Merchant(BaseModel, DictMixin):
    model_config = {"populate_by_name": True}

    id: UUID
    user: int
    title: str
    changed: int
