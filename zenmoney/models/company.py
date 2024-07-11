from dataclasses import dataclass

from .utils import check_dict_type, from_bool, from_int, from_none, from_str, from_union


@dataclass
class Company:
    id: int
    title: str
    deleted: bool
    changed: int
    www: str | None = None
    country: int | None = None
    full_title: str | None = None
    country_code: str | None = None

    @staticmethod
    def from_dict(obj: dict) -> 'Company':
        check_dict_type(obj)

        return Company(
            id=from_int(obj.get("id")),
            title=from_str(obj.get("title")),
            changed=from_int(obj.get("changed")),
            deleted=from_bool(obj.get("deleted")),
            www=from_union([from_none, from_str], obj.get("www")),
            country=from_union([from_none, from_int], obj.get("country")),
            full_title=from_union([from_none, from_str], obj.get("fullTitle")),
            country_code=from_union([from_none, from_str], obj.get("countryCode")),
        )

    def to_dict(self) -> dict:
        return {
            "id": from_int(self.id),
            "title": from_str(self.title),
            "changed": from_int(self.changed),
            "deleted": from_bool(self.deleted),
            "www": from_union([from_none, from_str], self.www),
            "country": from_union([from_none, from_int], self.country),
            "fullTitle": from_union([from_none, from_str], self.full_title),
            "countryCode": from_union([from_none, from_str], self.country_code),
        }
