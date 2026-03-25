from pydantic import BaseModel, Field

from .base import DictMixin


class User(BaseModel, DictMixin):
    id: int
    email: str
    changed: int
    country: int
    currency: int
    paid_till: int | None = Field(None, alias="paidTill")
    country_code: str = Field(alias="countryCode")
    plan_settings: str = Field(alias="planSettings")
    month_start_day: int | None = Field(None, alias="monthStartDay")
    plan_balance_mode: str = Field(alias="planBalanceMode")
    is_forecast_enabled: bool = Field(alias="isForecastEnabled")
    login: str | None = None
    subscription_renewal_date: int | None = Field(None, alias="subscriptionRenewalDate")
    subscription: str | None = None
    parent: int | None = None

    model_config = {"populate_by_name": True}
