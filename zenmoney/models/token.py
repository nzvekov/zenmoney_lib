import time

from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    received_at: int = Field(default_factory=lambda: int(time.time()))

    @property
    def is_valid(self) -> bool:
        return int(time.time()) < self.received_at + self.expires_in
