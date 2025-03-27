from dataclasses import dataclass

from .utils import check_dict_type, from_bool, from_int, from_none, from_str, from_union


@dataclass
class User:
    id: int
    email: str
    changed: int
    country: int
    currency: int
    paid_till: int
    country_code: str
    plan_settings: str
    month_start_day: int
    plan_balance_mode: str
    is_forecast_enabled: bool
    login: str | None = None
    subscription_renewal_date: int | None = None
    subscription: str | None = None
    parent: int | None = None

    @staticmethod
    def from_dict(obj: dict) -> 'User':
        check_dict_type(obj)

        return User(
            id=from_int(obj.get("id")),
            email=from_str(obj.get("email")),
            changed=from_int(obj.get("changed")),
            country=from_int(obj.get("country")),
            currency=from_int(obj.get("currency")),
            paid_till=from_int(obj.get("paidTill")),
            country_code=from_str(obj.get("countryCode")),
            plan_settings=from_str(obj.get("planSettings")),
            month_start_day=from_int(obj.get("monthStartDay")),
            plan_balance_mode=from_str(obj.get("planBalanceMode")),
            is_forecast_enabled=from_bool(obj.get("isForecastEnabled")),
            login=from_union([from_none, from_str], obj.get("login")),
            subscription_renewal_date=from_none(obj.get("subscriptionRenewalDate")),
            subscription=from_union([from_none, from_str], obj.get("subscription")),
            parent=from_union([from_none, from_int], obj.get("parent")),
        )

    def to_dict(self) -> dict:
        return {
            "id": from_int(self.id),
            "email": from_str(self.email),
            "changed": from_int(self.changed),
            "country": from_int(self.country),
            "currency": from_int(self.currency),
            "paidTill": from_int(self.paid_till),
            "countryCode": from_str(self.country_code),
            "planSettings": from_str(self.plan_settings),
            "monthStartDay": from_int(self.month_start_day),
            "planBalanceMode": from_str(self.plan_balance_mode),
            "isForecastEnabled": from_bool(self.is_forecast_enabled),
            "login": from_union([from_none, from_str], self.login),
            "subscriptionRenewalDate": from_none(self.subscription_renewal_date),
            "subscription": from_union([from_none, from_str], self.subscription),
            "parent": from_union([from_none, from_int], self.parent),
        }
