from .base import BaseZenmoneyRequest
from .constant import API_URL
from models.diff import Diff


class ZenmoneyRequestRaw(BaseZenmoneyRequest):
    def __init__(self, token: str):
        super().__init__()
        self.session.headers['Authorization'] = f"Bearer {token}"
        self.session.headers['Content-Type'] = 'application/json'
        self.json_diff = None

    def diff(self, params: dict) -> dict:
        uri_diff = API_URL + '/v8/diff/'
        response = self.post(uri_diff, json=params)
        return response.json()

    def suggest(self, transaction: dict) -> dict:
        uri_suggest = API_URL + '/v8/suggest/'
        response = self.post(uri_suggest, json={'transaction': transaction})
        return response.json()


class ZenmoneyRequest(ZenmoneyRequestRaw):
    def diff(self, params: Diff) -> Diff:
        return Diff.from_dict(super().diff(params.to_dict()))
