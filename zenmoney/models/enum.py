from enum import Enum


class BalanceCorrectionType(Enum):
    createCorrection = "createCorrection"
    disabled = "disabled"
    request = "request"


class Interval(Enum):
    day = "day"
    month = "month"
    year = "year"


class TypeEnum(Enum):
    cash = "cash"
    ccard = "ccard"
    checking = "checking"
    debt = "debt"
    deposit = "deposit"
    loan = "loan"


class State(Enum):
    deleted = "deleted"
    planned = "planned"
    processed = "processed"


class Source(Enum):
    api = "api"
    plugin = "plugin"
    push = "push"
    sms = "sms"
    split = "split"
