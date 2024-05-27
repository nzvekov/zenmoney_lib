from dataclasses import dataclass
from typing import Any, Optional

from .mixins import ChangedMixin, IntIdMixin
from .utils import from_bool, from_int, from_none, from_str, from_union


@dataclass
class User(IntIdMixin, ChangedMixin):
    email: str
    login: str
    country: int
    currency: int
    paid_till: int
    country_code: str
    plan_settings: str
    subscription: str
    month_start_day: int
    plan_balance_mode: str
    is_forecast_enabled: bool
    subscription_renewal_date: None
    parent: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        if not isinstance(obj, dict):
            raise TypeError(f"Expected dict, got {type(obj).__name__}")

        return User(
            id=from_int(obj.get("id")),
            email=from_str(obj.get("email")),
            login=from_str(obj.get("login")),
            changed=from_int(obj.get("changed")),
            country=from_int(obj.get("country")),
            currency=from_int(obj.get("currency")),
            paid_till=from_int(obj.get("paidTill")),
            country_code=from_str(obj.get("countryCode")),
            plan_settings=from_str(obj.get("planSettings")),
            subscription=from_str(obj.get("subscription")),
            month_start_day=from_int(obj.get("monthStartDay")),
            plan_balance_mode=from_str(obj.get("planBalanceMode")),
            is_forecast_enabled=from_bool(obj.get("isForecastEnabled")),
            subscription_renewal_date=from_none(obj.get("subscriptionRenewalDate")),
            parent=from_union([from_none, from_int], obj.get("parent")),
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["email"] = from_str(self.email)
        result["login"] = from_str(self.login)
        result["changed"] = from_int(self.changed)
        result["country"] = from_int(self.country)
        result["currency"] = from_int(self.currency)
        result["paidTill"] = from_int(self.paid_till)
        result["countryCode"] = from_str(self.country_code)
        result["planSettings"] = from_str(self.plan_settings)
        result["subscription"] = from_str(self.subscription)
        result["monthStartDay"] = from_int(self.month_start_day)
        result["planBalanceMode"] = from_str(self.plan_balance_mode)
        result["isForecastEnabled"] = from_bool(self.is_forecast_enabled)
        result["subscriptionRenewalDate"] = from_none(self.subscription_renewal_date)
        result["parent"] = from_union([from_none, from_int], self.parent)
        return result
