import pytest
import requests
from unittest.mock import patch

from zenmoney.base import BaseZenmoneyRequest
from zenmoney.exception import ZenmoneyRequestError
from zenmoney.constant import DEFAULT_TIMEOUT


class TestBaseZenmoneyRequest:
    """Тесты базового класса для HTTP запросов"""

    @pytest.fixture
    def base_request(self):
        """Создает экземпляр базового запроса"""
        return BaseZenmoneyRequest()

    def test_init_with_default_timeout(self):
        """Проверяет инициализацию с таймаутом по умолчанию"""
        request = BaseZenmoneyRequest()
        assert request.timeout == DEFAULT_TIMEOUT

    def test_init_with_custom_timeout(self):
        """Проверяет инициализацию с пользовательским таймаутом"""
        custom_timeout = 10.0
        request = BaseZenmoneyRequest(timeout=custom_timeout)
        assert request.timeout == custom_timeout

    def test_request_success(self, base_request, mock_response):
        """Проверяет успешный HTTP запрос"""
        with patch.object(base_request.session, 'request', return_value=mock_response) as mock_request:
            response = base_request._request('GET', 'https://example.com')
            mock_request.assert_called_once_with(
                'GET', 'https://example.com', timeout=DEFAULT_TIMEOUT
            )
            assert response == mock_response

    def test_request_error(self, base_request):
        """Проверяет обработку ошибки HTTP запроса"""
        with patch.object(
            base_request.session, 
            'request', 
            side_effect=requests.exceptions.RequestException("Test error")
        ) as mock_request:
            with pytest.raises(ZenmoneyRequestError) as exc_info:
                base_request._request('GET', 'https://example.com')
            assert "Request error: Test error" in str(exc_info.value)

    def test_get_method(self, base_request, mock_response):
        """Проверяет GET запрос"""
        with patch.object(base_request.session, 'request', return_value=mock_response) as mock_request:
            response = base_request._get('https://example.com')
            mock_request.assert_called_once_with(
                'GET', 'https://example.com', timeout=DEFAULT_TIMEOUT
            )
            assert response == mock_response

    def test_post_method(self, base_request, mock_response):
        """Проверяет POST запрос"""
        test_data = {'key': 'value'}
        with patch.object(base_request.session, 'request', return_value=mock_response) as mock_request:
            response = base_request._post('https://example.com', data=test_data)
            mock_request.assert_called_once_with(
                'POST', 'https://example.com', timeout=DEFAULT_TIMEOUT, data=test_data
            )
            assert response == mock_response 