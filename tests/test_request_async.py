import asyncio
import json

import httpx
import pytest

from zenmoney import AsyncZenmoneyRequest
from zenmoney.async_request import _httpx_timeout
from zenmoney.constant import DIFF_URL, SUGGEST_URL
from zenmoney.exception import ZenmoneyRequestError
from zenmoney.models import Diff


def _client_with(handler) -> AsyncZenmoneyRequest:
    """AsyncZenmoneyRequest whose httpx client is backed by an in-memory transport."""
    request = AsyncZenmoneyRequest(token="test_token")
    request.client._transport = httpx.MockTransport(handler)
    return request


class TestAsyncZenmoneyRequest:
    def test_raw_diff_posts_json_with_bearer(self, sample_diff_data):
        seen = {}

        def handler(req: httpx.Request) -> httpx.Response:
            seen["url"] = str(req.url)
            seen["auth"] = req.headers["Authorization"]
            seen["content_type"] = req.headers["Content-Type"]
            seen["body"] = json.loads(req.content)
            return httpx.Response(200, json=sample_diff_data)

        async def run():
            async with _client_with(handler) as client:
                return await client.raw_diff(sample_diff_data)

        assert asyncio.run(run()) == sample_diff_data
        assert seen == {
            "url": DIFF_URL,
            "auth": "Bearer test_token",
            "content_type": "application/json",
            "body": sample_diff_data,
        }

    def test_diff_returns_parsed_model(self, sample_diff_data):
        async def run():
            async with _client_with(lambda req: httpx.Response(200, json=sample_diff_data)) as client:
                return await client.diff(Diff(server_timestamp=0, current_client_timestamp=1))

        result = asyncio.run(run())
        assert isinstance(result, Diff)
        assert result.server_timestamp == sample_diff_data["serverTimestamp"]

    def test_raw_suggest(self):
        def handler(req: httpx.Request) -> httpx.Response:
            assert str(req.url) == SUGGEST_URL
            return httpx.Response(200, json={"payee": "McDonalds"})

        async def run():
            async with _client_with(handler) as client:
                return await client.raw_suggest({"payee": "mcd"})

        assert asyncio.run(run()) == {"payee": "McDonalds"}

    @pytest.mark.parametrize(
        "response",
        [httpx.Response(401, json={}), httpx.Response(200, content=b"not json")],
    )
    def test_errors_wrapped(self, response):
        async def run():
            async with _client_with(lambda req: response) as client:
                await client.raw_diff({})

        with pytest.raises(ZenmoneyRequestError):
            asyncio.run(run())

    def test_network_error_wrapped(self):
        def handler(req: httpx.Request) -> httpx.Response:
            raise httpx.ConnectError("boom", request=req)

        async def run():
            async with _client_with(handler) as client:
                await client.raw_diff({})

        with pytest.raises(ZenmoneyRequestError):
            asyncio.run(run())

    def test_aexit_closes_client(self):
        async def run():
            async with _client_with(lambda req: httpx.Response(200, json={})) as client:
                pass
            return client

        assert asyncio.run(run()).client.is_closed

    def test_timeout_passed_to_client(self):
        client = AsyncZenmoneyRequest("t", timeout=(3, 30))
        assert (client.client.timeout.connect, client.client.timeout.read) == (3, 30)

    def test_timeout_translation(self):
        assert _httpx_timeout(10).read == 10
        t = _httpx_timeout((3, 30))
        assert (t.connect, t.read) == (3, 30)
        assert _httpx_timeout(None).read is None
