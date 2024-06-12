from datetime import datetime
from enum import Enum
from typing import Any, Callable, List, Type, TypeVar, cast

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def check_dict_type(value: Any) -> None:
    if not isinstance(value, dict):
        raise TypeError(f"Expected dict, got {type(value).__name__}")


def from_int(value: Any) -> int:
    if value and (not isinstance(value, int) or isinstance(value, bool)):
        raise TypeError(f"Expected int, got {type(value).__name__}")
    return value


def from_str(value: Any) -> str:
    if not isinstance(value, str):
        raise TypeError(f"Expected str, got {type(value).__name__}")
    return value


def from_bool(value: Any) -> bool:
    if not isinstance(value, bool):
        raise TypeError(f"Expected bool, got {type(value).__name__}")
    return value


def from_float(value: Any) -> float:
    if not isinstance(value, (float, int)) or isinstance(value, bool):
        raise TypeError(f"Expected float or int, got {type(value).__name__}")
    return float(value)


def from_none(value: Any) -> Any:
    if value is not None:
        raise TypeError(f"Expected None, got {type(value).__name__}")
    return value


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except TypeError:
            pass
    raise TypeError("No matching type found")


def from_list(f: Callable[[Any], T], value: Any) -> List[T]:
    if value and not isinstance(value, list):
        raise TypeError(f"Expected list, got {type(value).__name__}")

    if value:
        return [f(y) for y in value]

    return []


def from_datetime(value: Any) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except (ValueError, TypeError) as e:
        raise TypeError(f"Could not parse datetime from {value}") from e


def to_enum(c: Type[EnumT], obj: Any) -> EnumT:
    if not isinstance(obj, c):
        raise TypeError(f"Expected {c.__name__}, got {type(obj).__name__}")
    return obj.value


def to_float(value: Any) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected int or float, got {type(value).__name__}")
    return value


def is_type(t: Type[T], value: Any) -> T:
    if not isinstance(value, t):
        raise TypeError(f"Expected {t.__name__}, got {type(value).__name__}")
    return value


def to_class(c: Type[T], value: Any) -> dict:
    if not isinstance(value, c):
        raise TypeError(f"Expected {c.__name__}, got {type(value).__name__}")
    return cast(Any, value).to_dict()


def check_object_class_name_list(obj: str) -> None:
    object_class_name_list = (
        'account',
        'budget',
        'company',
        'instrument',
        'merchant',
        'reminder',
        'reminderMarker',
        'tag',
        'transaction',
        'user',
    )
    if obj not in object_class_name_list:
        raise ValueError(f'The object {obj} is unknown')
