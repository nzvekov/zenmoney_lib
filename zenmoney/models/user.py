from dataclasses import dataclass
from typing import Optional

from typing_extensions import Any

from zenmoney.helpers import from_str, from_int, from_bool, from_none, from_union


@dataclass
class User:
    id: int
    email: str
    login: str
    changed: int
    country: int
    currency: int
    paidTill: int
    countryCode: str
    planSettings: str
    subscription: str
    monthStartDay: int
    planBalanceMode: str
    isForecastEnabled: bool
    subscriptionRenewalDate: None
    parent: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        id = from_int(obj.get("id"))
        email = from_str(obj.get("email"))
        login = from_str(obj.get("login"))
        changed = from_int(obj.get("changed"))
        country = from_int(obj.get("country"))
        currency = from_int(obj.get("currency"))
        paidTill = from_int(obj.get("paidTill"))
        countryCode = from_str(obj.get("countryCode"))
        planSettings = from_str(obj.get("planSettings"))
        subscription = from_str(obj.get("subscription"))
        monthStartDay = from_int(obj.get("monthStartDay"))
        planBalanceMode = from_str(obj.get("planBalanceMode"))
        isForecastEnabled = from_bool(obj.get("isForecastEnabled"))
        subscriptionRenewalDate = from_none(obj.get("subscriptionRenewalDate"))
        parent = from_union([from_none, from_int], obj.get("parent"))
        return User(
            id,
            email,
            login,
            changed,
            country,
            currency,
            paidTill,
            countryCode,
            planSettings,
            subscription,
            monthStartDay,
            planBalanceMode,
            isForecastEnabled,
            subscriptionRenewalDate,
            parent,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["email"] = from_str(self.email)
        result["login"] = from_str(self.login)
        result["changed"] = from_int(self.changed)
        result["country"] = from_int(self.country)
        result["currency"] = from_int(self.currency)
        result["paidTill"] = from_int(self.paidTill)
        result["countryCode"] = from_str(self.countryCode)
        result["planSettings"] = from_str(self.planSettings)
        result["subscription"] = from_str(self.subscription)
        result["monthStartDay"] = from_int(self.monthStartDay)
        result["planBalanceMode"] = from_str(self.planBalanceMode)
        result["isForecastEnabled"] = from_bool(self.isForecastEnabled)
        result["subscriptionRenewalDate"] = from_none(self.subscriptionRenewalDate)
        result["parent"] = from_union([from_none, from_int], self.parent)
        return result
