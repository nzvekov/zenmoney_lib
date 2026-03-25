"""Base mixins for Zenmoney models."""

from typing import Any

from pydantic import BaseModel


class DictMixin:
    to_dict_by_alias: bool = True
    to_dict_mode: str | None = "json"
    to_dict_exclude_none: bool = False

    @classmethod
    def from_dict(cls: type[BaseModel], obj: dict) -> Any:
        return cls.model_validate(obj)

    def to_dict(self) -> dict:
        kwargs: dict[str, Any] = {
            "by_alias": self.to_dict_by_alias,
            "exclude_none": self.to_dict_exclude_none,
        }
        if self.to_dict_mode is not None:
            kwargs["mode"] = self.to_dict_mode
        return self.model_dump(**kwargs)
