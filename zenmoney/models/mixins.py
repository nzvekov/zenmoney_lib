from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class IntIdMixin:
    id: int


@dataclass
class UuidIdMixin:
    id: UUID


@dataclass
class ChangedMixin:
    changed: int


@dataclass
class BaseServiceObjectMixin(IntIdMixin):
    id: int
    title: str


@dataclass
class BaseUserObjectMixin(UuidIdMixin):
    user: int


@dataclass
class BaseUserDictionaryObjectMixin(BaseUserObjectMixin, ChangedMixin):
    title: str


@dataclass
class BaseOperationMixin(BaseUserObjectMixin):
    income: float
    outcome: float
    income_account: UUID
    outcome_account: UUID
    income_instrument: int
    outcome_instrument: int
    changed: int


@dataclass
class BaseRealOperationMixin(BaseOperationMixin):
    date: datetime
