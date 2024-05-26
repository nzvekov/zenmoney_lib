from models import Diff

from .base import BaseZenmoneyRequest
from .constant import URI_DIFF, URI_SUGGEST


class ZenmoneyRequest(BaseZenmoneyRequest):
    def __init__(self, token: str):
        super().__init__()
        self.set_headers(token)

    def set_headers(self, token):
        self.session.headers['Authorization'] = f"Bearer {token}"
        self.session.headers['Content-Type'] = 'application/json'

    def raw_diff(self, data: dict) -> dict:
        return self.post_and_parse_response_json(URI_DIFF, data)

    def diff(self, params: Diff) -> Diff:
        return Diff.from_dict(self.raw_diff(params.to_dict()))

    def raw_suggest(self, data: dict) -> dict:
        return self.post_and_parse_response_json(URI_SUGGEST, data)
