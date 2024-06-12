import time
from dataclasses import dataclass


@dataclass
class Token:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str

    @property
    def is_valid(self) -> bool:
        return int(time.time()) < self.expires_in
