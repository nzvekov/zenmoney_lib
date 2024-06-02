from dataclasses import dataclass
from typing import Optional

from .utils import check_dict_type, from_bool, from_int, from_none, from_str, from_union


@dataclass
class User:
    id: int
    email: str
    login: str
    changed: int
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
    def from_dict(obj: dict) -> 'User':
        check_dict_type(obj)

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
        return {
            "id": from_int(self.id),
            "email": from_str(self.email),
            "login": from_str(self.login),
            "changed": from_int(self.changed),
            "country": from_int(self.country),
            "currency": from_int(self.currency),
            "paidTill": from_int(self.paid_till),
            "countryCode": from_str(self.country_code),
            "planSettings": from_str(self.plan_settings),
            "subscription": from_str(self.subscription),
            "monthStartDay": from_int(self.month_start_day),
            "planBalanceMode": from_str(self.plan_balance_mode),
            "isForecastEnabled": from_bool(self.is_forecast_enabled),
            "subscriptionRenewalDate": from_none(self.subscription_renewal_date),
            "parent": from_union([from_none, from_int], self.parent),
        }
