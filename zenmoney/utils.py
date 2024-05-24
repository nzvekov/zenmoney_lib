from datetime import datetime

from constant import OBJECT_CLASS_NAME_LIST


def timestamp(date: datetime = None) -> int:
    if date:
        return int(datetime.timestamp(date))

    return int(datetime.timestamp(datetime.now()))


def check_object_class_name_list(obj: str) -> None:
    if obj not in OBJECT_CLASS_NAME_LIST:
        raise ValueError(f'The object {obj} is unknown')
