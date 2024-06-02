from dataclasses import dataclass
from typing import List, Optional

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
from .utils import (
    check_dict_type,
    check_object_class_name_list,
    from_int,
    from_list,
    to_class,
)


@dataclass
class Diff:
    server_timestamp: int
    current_client_timestamp: int
    tag: Optional[List[Tag]] = None
    user: Optional[List[User]] = None
    budget: Optional[List[Budget]] = None
    account: Optional[List[Account]] = None
    company: Optional[List[Company]] = None
    country: Optional[List[Country]] = None
    merchant: Optional[List[Merchant]] = None
    reminder: Optional[List[Reminder]] = None
    instrument: Optional[List[Instrument]] = None
    transaction: Optional[List[Transaction]] = None
    reminder_marker: Optional[List[ReminderMarker]] = None
    deletion: Optional[List[Deletion]] = None
    force_fetch: Optional[List[str]] = None

    def __post_init__(self):
        if self.force_fetch:
            if not isinstance(self.force_fetch, list):
                raise TypeError(f"Expected list, got {type(self.force_fetch).__name__}")

            for obj in self.force_fetch:
                check_object_class_name_list(obj)

    @staticmethod
    def from_dict(obj: dict) -> 'Diff':
        check_dict_type(obj)

        return Diff(
            server_timestamp=from_int(obj.get("serverTimestamp")),
            current_client_timestamp=from_int(obj.get("currentClientTimestamp")),
            tag=from_list(Tag.from_dict, obj.get("tag")),
            user=from_list(User.from_dict, obj.get("user")),
            budget=from_list(Budget.from_dict, obj.get("budget")),
            account=from_list(Account.from_dict, obj.get("account")),
            company=from_list(Company.from_dict, obj.get("company")),
            country=from_list(Country.from_dict, obj.get("country")),
            merchant=from_list(Merchant.from_dict, obj.get("merchant")),
            reminder=from_list(Reminder.from_dict, obj.get("reminder")),
            instrument=from_list(Instrument.from_dict, obj.get("instrument")),
            transaction=from_list(Transaction.from_dict, obj.get("transaction")),
            reminder_marker=from_list(ReminderMarker.from_dict, obj.get("reminderMarker")),
            deletion=from_list(Deletion.from_dict, obj.get("deletion")),
            force_fetch=obj.get("forceFetch"),
        )

    def to_dict(self) -> dict:
        return remove_empty_attributes(
            data={
                "serverTimestamp": from_int(self.server_timestamp),
                "currentClientTimestamp": from_int(self.current_client_timestamp),
                "tag": from_list(lambda x: to_class(Tag, x), self.tag),
                "user": from_list(lambda x: to_class(User, x), self.user),
                "budget": from_list(lambda x: to_class(Budget, x), self.budget),
                "account": from_list(lambda x: to_class(Account, x), self.account),
                "company": from_list(lambda x: to_class(Company, x), self.company),
                "country": from_list(lambda x: to_class(Country, x), self.country),
                "merchant": from_list(lambda x: to_class(Merchant, x), self.merchant),
                "reminder": from_list(lambda x: to_class(Reminder, x), self.reminder),
                "instrument": from_list(lambda x: to_class(Instrument, x), self.instrument),
                "transaction": from_list(lambda x: to_class(Transaction, x), self.transaction),
                "reminderMarker": from_list(lambda x: to_class(ReminderMarker, x), self.reminder_marker),
                "deletion": from_list(lambda x: to_class(Deletion, x), self.deletion),
                "forceFetch": self.force_fetch,
            }
        )


def remove_empty_attributes(data: dict) -> dict:
    return {k: v for k, v in data.items() if v not in ([], {}, None)}
