try:
    import httpx
except ImportError as err:
    raise ImportError("AsyncZenmoneyRequest requires httpx: pip install 'zenmoney-py[async]'") from err

from .constant import DEFAULT_TIMEOUT, DIFF_URL, SUGGEST_URL
from .exception import ZenmoneyRequestError
from .models import Diff


def _httpx_timeout(timeout: float | tuple[float, float] | tuple[float, None] | None) -> httpx.Timeout:
    """Translate a requests-style timeout (single value or ``(connect, read)``) to httpx."""
    if isinstance(timeout, tuple):
        connect, read = timeout
        return httpx.Timeout(read, connect=connect)
    return httpx.Timeout(timeout)


class AsyncZenmoneyRequest:
    """Async counterpart of ``ZenmoneyRequest``. One instance belongs to one event loop."""

    def __init__(
        self,
        token: str,
        *,
        timeout: float | tuple[float, float] | tuple[float, None] | None = DEFAULT_TIMEOUT,
        diff_url: str = DIFF_URL,
        suggest_url: str = SUGGEST_URL,
    ):
        self._diff_url = diff_url
        self._suggest_url = suggest_url
        self.client = httpx.AsyncClient(
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            timeout=_httpx_timeout(timeout),
        )

    async def _post(self, url: str, data: dict) -> dict:
        try:
            response = await self.client.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as err:
            raise ZenmoneyRequestError(f"Request error: {err}") from err
        except ValueError as err:
            raise ZenmoneyRequestError(f"Failed to convert response to JSON: {err}") from err

    async def raw_diff(self, data: dict) -> dict:
        return await self._post(self._diff_url, data)

    async def diff(self, params: Diff) -> Diff:
        return Diff.from_dict(await self.raw_diff(params.to_dict()))

    async def raw_suggest(self, data: dict) -> dict:
        return await self._post(self._suggest_url, data)

    async def aclose(self) -> None:
        await self.client.aclose()

    async def __aenter__(self) -> "AsyncZenmoneyRequest":
        return self

    async def __aexit__(self, *exc_info) -> None:
        await self.aclose()
