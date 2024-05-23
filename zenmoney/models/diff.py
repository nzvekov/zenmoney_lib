from dataclasses import dataclass
from typing import List, Any, Optional

from zenmoney.helpers import from_list, to_class, from_int
from zenmoney.models.account import Account
from zenmoney.models.budget import Budget
from zenmoney.models.company import Company
from zenmoney.models.country import Country
from zenmoney.models.instrument import Instrument
from zenmoney.models.merchant import Merchant
from zenmoney.models.reminder import Reminder
from zenmoney.models.reminder_marker import ReminderMarker
from zenmoney.models.tag import Tag
from zenmoney.models.transaction import Transaction
from zenmoney.models.user import User


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
        return result
