import requests
from requests.exceptions import RequestException

from .constant import DEFAULT_TIMEOUT
from .exception import ZenmoneyRequestError


class BaseZenmoneyRequest(object):
    def __init__(self, timeout: float | tuple[float, float] | tuple[float, None] | None = DEFAULT_TIMEOUT):
        self.session = requests.Session()
        self.timeout = timeout

    def _request(self, method: str, url: str, **kwargs) -> requests.Response:
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            return response
        except RequestException as err:
            raise ZenmoneyRequestError(f"Request error: {err}") from err

    def _get(self, url: str, **kwargs) -> requests.Response:
        return self._request('GET', url, **kwargs)

    def _post(self, url: str, **kwargs) -> requests.Response:
        return self._request('POST', url, **kwargs)
