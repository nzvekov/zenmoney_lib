from unittest.mock import patch

import pytest

from zenmoney.constant import DIFF_URL, SUGGEST_URL
from zenmoney.models import Diff
from zenmoney.request import ZenmoneyRequest


class TestZenmoneyRequest:
    """Тесты класса ZenmoneyRequest"""

    @pytest.fixture
    def zenmoney_request(self):
        """Создает экземпляр ZenmoneyRequest с тестовым токеном"""
        return ZenmoneyRequest(token="test_token")

    def test_raw_diff_success(self, zenmoney_request, sample_diff_data):
        """Проверяет успешный вызов raw_diff"""
        response_data = sample_diff_data.copy()

        with patch.object(zenmoney_request, "_post") as mock_post:
            mock_response = mock_post.return_value
            mock_response.json.return_value = response_data

            result = zenmoney_request.raw_diff(data=response_data)

            mock_post.assert_called_once_with(DIFF_URL, json=response_data)
            assert result == response_data

    def test_raw_diff_with_custom_url(self, sample_diff_data):
        """Проверяет вызов raw_diff с кастомным URL"""
        custom_url = "https://custom.example.com/diff/"
        request = ZenmoneyRequest(token="test", diff_url=custom_url)

        response_data = sample_diff_data.copy()

        with patch.object(request, "_post") as mock_post:
            mock_response = mock_post.return_value
            mock_response.json.return_value = response_data

            request.raw_diff(data=response_data)

            mock_post.assert_called_once_with(custom_url, json=response_data)

    def test_raw_suggest_success(self, zenmoney_request):
        """Проверяет успешный вызов raw_suggest"""
        suggest_data = {"query": "test_query", "limit": 10}
        response_data = {"items": [{"id": "1", "title": "Test"}]}

        with patch.object(zenmoney_request, "_post") as mock_post:
            mock_response = mock_post.return_value
            mock_response.json.return_value = response_data

            result = zenmoney_request.raw_suggest(data=suggest_data)

            mock_post.assert_called_once_with(SUGGEST_URL, json=suggest_data)
            assert result == response_data

    def test_raw_suggest_with_custom_url(self):
        """Проверяет вызов raw_suggest с кастомным URL"""
        custom_url = "https://custom.example.com/suggest/"
        request = ZenmoneyRequest(token="test", suggest_url=custom_url)

        suggest_data = {"query": "test"}
        response_data = {}

        with patch.object(request, "_post") as mock_post:
            mock_response = mock_post.return_value
            mock_response.json.return_value = response_data

            request.raw_suggest(data=suggest_data)

            mock_post.assert_called_once_with(custom_url, json=suggest_data)

    def test_diff_success(self, zenmoney_request, sample_diff_data):
        """Проверяет успешный вызов diff с преобразованием в Diff"""
        diff_obj = Diff.from_dict(sample_diff_data)
        response_data = sample_diff_data.copy()

        with patch.object(zenmoney_request, "raw_diff") as mock_raw_diff:
            mock_raw_diff.return_value = response_data

            result = zenmoney_request.diff(params=diff_obj)

            mock_raw_diff.assert_called_once_with(diff_obj.to_dict())
            assert isinstance(result, Diff)
            assert result.server_timestamp == sample_diff_data["serverTimestamp"]
            assert result.current_client_timestamp == sample_diff_data["currentClientTimestamp"]

    def test_diff_passes_data_correctly(self, zenmoney_request):
        """Проверяет, что diff передает правильные данные в raw_diff"""
        data = {
            "serverTimestamp": 1234567890,
            "currentClientTimestamp": 1234567800,
        }
        diff_obj = Diff.from_dict(data)

        with patch.object(zenmoney_request, "raw_diff") as mock_raw_diff:
            mock_raw_diff.return_value = data

            zenmoney_request.diff(params=diff_obj)

            call_args = mock_raw_diff.call_args[0][0]
            assert call_args["serverTimestamp"] == 1234567890
            assert call_args["currentClientTimestamp"] == 1234567800

    def test_init_sets_headers(self):
        """Проверяет установку заголовков при инициализации"""
        request = ZenmoneyRequest(token="my_token")

        assert request.session.headers["Authorization"] == "Bearer my_token"
        assert request.session.headers["Content-Type"] == "application/json"
