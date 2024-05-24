from dataclasses import dataclass
from typing import List, Any, Optional

from utils import check_object_class_name_list
from .deletion import Deletion
from .helpers import from_list, to_class, from_int
from .account import Account
from .budget import Budget
from .company import Company
from .country import Country
from .instrument import Instrument
from .merchant import Merchant
from .reminder import Reminder
from .reminder_marker import ReminderMarker
from .tag import Tag
from .transaction import Transaction
from .user import User


def remove_empty_attributes(data: dict) -> dict:
    return {k: v for k, v in data.items() if v not in [[], {}]}


@dataclass
class Diff:
    serverTimestamp: int
    currentClientTimestamp: int
    tag: Optional[List[Tag]]
    user: Optional[List[User]]
    budget: Optional[List[Budget]]
    account: Optional[List[Account]]
    company: Optional[List[Company]]
    country: Optional[List[Country]]
    merchant: Optional[List[Merchant]]
    reminder: Optional[List[Reminder]]
    instrument: Optional[List[Instrument]]
    transaction: Optional[List[Transaction]]
    reminderMarker: Optional[List[ReminderMarker]]
    deletion: Optional[List[Deletion]]
    forceFetch: Optional[List[str]]

    def __post_init__(self):
        if self.forceFetch and not isinstance(self.forceFetch, list):
            raise TypeError(f"Expected list, got {type(self.forceFetch).__name__}")

        for obj in self.forceFetch:
            check_object_class_name_list(obj)

    @staticmethod
    def from_dict(obj: Any) -> 'Diff':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        tag = from_list(Tag.from_dict, obj.get("tag"))
        user = from_list(User.from_dict, obj.get("user"))
        budget = from_list(Budget.from_dict, obj.get("budget"))
        account = from_list(Account.from_dict, obj.get("account"))
        company = from_list(Company.from_dict, obj.get("company"))
        country = from_list(Country.from_dict, obj.get("country"))
        merchant = from_list(Merchant.from_dict, obj.get("merchant"))
        reminder = from_list(Reminder.from_dict, obj.get("reminder"))
        instrument = from_list(Instrument.from_dict, obj.get("instrument"))
        transaction = from_list(Transaction.from_dict, obj.get("transaction"))
        reminderMarker = from_list(ReminderMarker.from_dict, obj.get("reminderMarker"))
        serverTimestamp = from_int(obj.get("serverTimestamp"))
        currentClientTimestamp = from_int(obj.get("currentClientTimestamp"))
        deletion = from_list(Deletion.from_dict, obj.get("deletion"))
        forceFetch = obj.get("forceFetch")
        return Diff(
            serverTimestamp,
            currentClientTimestamp,
            tag,
            user,
            budget,
            account,
            company,
            country,
            merchant,
            reminder,
            instrument,
            transaction,
            reminderMarker,
            deletion,
            forceFetch,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["serverTimestamp"] = from_int(self.serverTimestamp)
        result["currentClientTimestamp"] = from_int(self.currentClientTimestamp)
        result["tag"] = from_list(lambda x: to_class(Tag, x), self.tag)
        result["user"] = from_list(lambda x: to_class(User, x), self.user)
        result["budget"] = from_list(lambda x: to_class(Budget, x), self.budget)
        result["account"] = from_list(lambda x: to_class(Account, x), self.account)
        result["company"] = from_list(lambda x: to_class(Company, x), self.company)
        result["country"] = from_list(lambda x: to_class(Country, x), self.country)
        result["merchant"] = from_list(lambda x: to_class(Merchant, x), self.merchant)
        result["reminder"] = from_list(lambda x: to_class(Reminder, x), self.reminder)
        result["instrument"] = from_list(lambda x: to_class(Instrument, x), self.instrument)
        result["transaction"] = from_list(lambda x: to_class(Transaction, x), self.transaction)
        result["reminderMarker"] = from_list(lambda x: to_class(ReminderMarker, x), self.reminderMarker)
        result["deletion"] = from_list(lambda x: to_class(Deletion, x), self.deletion)
        result["forceFetch"] = self.forceFetch
        # todo подумать как изменить этот кусок кода, чтобы формировать dict уже по единому алгоритму
        return remove_empty_attributes(data=result)
