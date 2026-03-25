import time

from pydantic import BaseModel, Field, model_validator

from .account import Account
from .budget import Budget
from .company import Company
from .country import Country
from .deletion import Deletion
from .instrument import Instrument
from .merchant import Merchant
from .reminder import Reminder
from .reminder_marker import ReminderMarker
from .tag import Tag
from .transaction import Transaction
from .user import User
from .utils import check_object_class_name_list, remove_empty_attributes


class Diff(BaseModel):
    server_timestamp: int = Field(alias="serverTimestamp")
    current_client_timestamp: int = Field(alias="currentClientTimestamp")
    tag: list[Tag] = Field(default_factory=list)
    user: list[User] = Field(default_factory=list)
    budget: list[Budget] = Field(default_factory=list)
    account: list[Account] = Field(default_factory=list)
    company: list[Company] = Field(default_factory=list)
    country: list[Country] = Field(default_factory=list)
    merchant: list[Merchant] = Field(default_factory=list)
    reminder: list[Reminder] = Field(default_factory=list)
    instrument: list[Instrument] = Field(default_factory=list)
    transaction: list[Transaction] = Field(default_factory=list)
    reminder_marker: list[ReminderMarker] = Field(default_factory=list, alias="reminderMarker")
    deletion: list[Deletion] = Field(default_factory=list)
    force_fetch: list[str] | None = Field(None, alias="forceFetch")

    model_config = {"populate_by_name": True}

    @model_validator(mode="after")
    def validate_force_fetch(self) -> "Diff":
        if self.force_fetch is not None:
            for obj in self.force_fetch:
                check_object_class_name_list(obj)
        return self

    @classmethod
    def from_dict(cls, obj: dict) -> "Diff":
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")
        force_fetch = obj.get("forceFetch")
        if force_fetch is not None and not isinstance(force_fetch, list):
            raise TypeError(f"Expected list for forceFetch, got {type(force_fetch).__name__}")
        normalized = {
            "serverTimestamp": obj["serverTimestamp"],
            "currentClientTimestamp": obj.get("currentClientTimestamp", int(time.time())),
            "tag": obj.get("tag") or [],
            "user": obj.get("user") or [],
            "budget": obj.get("budget") or [],
            "account": obj.get("account") or [],
            "company": obj.get("company") or [],
            "country": obj.get("country") or [],
            "merchant": obj.get("merchant") or [],
            "reminder": obj.get("reminder") or [],
            "instrument": obj.get("instrument") or [],
            "transaction": obj.get("transaction") or [],
            "reminderMarker": obj.get("reminderMarker") or [],
            "deletion": obj.get("deletion") or [],
            "forceFetch": obj.get("forceFetch"),
        }
        return cls.model_validate(normalized)

    def to_dict(self) -> dict:
        data = {
            "serverTimestamp": self.server_timestamp,
            "currentClientTimestamp": self.current_client_timestamp,
            "tag": [t.model_dump(by_alias=True, mode="json") for t in self.tag],
            "user": [u.model_dump(by_alias=True) for u in self.user],
            "budget": [b.model_dump(by_alias=True, mode="json") for b in self.budget],
            "account": [a.model_dump(by_alias=True, mode="json") for a in self.account],
            "company": [c.model_dump(by_alias=True) for c in self.company],
            "country": [c.model_dump(by_alias=True, mode="json") for c in self.country],
            "merchant": [m.model_dump(by_alias=True, mode="json") for m in self.merchant],
            "reminder": [r.model_dump(by_alias=True, mode="json") for r in self.reminder],
            "instrument": [i.model_dump(by_alias=True) for i in self.instrument],
            "transaction": [t.model_dump(by_alias=True, mode="json") for t in self.transaction],
            "reminderMarker": [rm.model_dump(by_alias=True, mode="json") for rm in self.reminder_marker],
            "deletion": [d.to_dict() for d in self.deletion],
            "forceFetch": self.force_fetch,
        }
        return remove_empty_attributes(data)
