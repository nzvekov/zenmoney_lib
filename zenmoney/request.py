from .base import BaseZenmoneyRequest
from .constant import DEFAULT_TIMEOUT, DIFF_URL, SUGGEST_URL
from .models import Diff
from .utils import convert_response_to_json


class ZenmoneyRequest(BaseZenmoneyRequest):
    def __init__(
        self,
        token: str,
        *,
        timeout: float | tuple[float, float] | tuple[float, None] | None = DEFAULT_TIMEOUT,
        diff_url: str = DIFF_URL,
        suggest_url: str = SUGGEST_URL,
    ):
        super().__init__(timeout=timeout)
        self._diff_url = diff_url
        self._suggest_url = suggest_url
        self._set_headers(token)

    def _set_headers(self, token) -> None:
        self.session.headers['Authorization'] = f"Bearer {token}"
        self.session.headers['Content-Type'] = 'application/json'

    def raw_diff(self, data: dict) -> dict:
        return convert_response_to_json(self._post(self._diff_url, json=data))

    def diff(self, params: Diff) -> Diff:
        return Diff.from_dict(self.raw_diff(params.to_dict()))

    def raw_suggest(self, data: dict) -> dict:
        return convert_response_to_json(self._post(self._suggest_url, json=data))
