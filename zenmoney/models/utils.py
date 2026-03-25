OBJECT_CLASS_NAMES = (
    "account",
    "budget",
    "company",
    "instrument",
    "merchant",
    "reminder",
    "reminderMarker",
    "tag",
    "transaction",
    "user",
)


def check_object_class_name_list(obj: str) -> None:
    if obj not in OBJECT_CLASS_NAMES:
        raise ValueError(f"The object {obj} is unknown")


def remove_empty_attributes(data: dict) -> dict:
    return {k: v for k, v in data.items() if v not in ([], {}, None)}
