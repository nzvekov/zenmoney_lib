import pytest
from unittest.mock import Mock, patch, MagicMock
from http import HTTPStatus
from urllib.parse import urlparse

from zenmoney.oauth2 import ZenmoneyOAuth2
from zenmoney.exception import ZenmoneyRequestError
from zenmoney.models import Token


class TestZenmoneyOAuth2:
    @pytest.fixture
    def oauth_client(self):
        return ZenmoneyOAuth2(
            consumer_key='test_key',
            consumer_secret='test_secret',
            username='test_user',
            password='test_pass'
        )

    def test_init(self, oauth_client):
        assert oauth_client.consumer_key == 'test_key'
        assert oauth_client.consumer_secret == 'test_secret'
        assert oauth_client.username == 'test_user'
        assert oauth_client.password == 'test_pass'
        assert oauth_client._token is None

    def test_get_token_success(self, oauth_client):
        mock_response = MagicMock()
        mock_response.status_code = HTTPStatus.OK
        mock_response.json.return_value = {
            'access_token': 'test_access_token',
            'token_type': 'bearer',
            'expires_in': 3600,
            'refresh_token': 'test_refresh_token'
        }

        with patch.object(oauth_client, '_get_code', return_value='test_code'), \
             patch.object(oauth_client, '_post', return_value=mock_response):
            token = oauth_client._get_token()
            assert isinstance(token, Token)
            assert token.access_token == 'test_access_token'
            assert token.token_type == 'bearer'
            assert token.expires_in == 3600
            assert token.refresh_token == 'test_refresh_token'

    def test_get_token_failure(self, oauth_client):
        mock_response = MagicMock()
        mock_response.status_code = HTTPStatus.BAD_REQUEST
        mock_response.text = 'Invalid request'

        with patch.object(oauth_client, '_get_code', return_value='test_code'), \
             patch.object(oauth_client, '_post', return_value=mock_response):
            with pytest.raises(ZenmoneyRequestError) as exc_info:
                oauth_client._get_token()
            assert "Failed to get token: Invalid request" in str(exc_info.value)

    def test_get_code_success(self, oauth_client):
        mock_auth_response = MagicMock()
        mock_auth_response.status_code = HTTPStatus.FOUND
        mock_auth_response.next = MagicMock()
        mock_auth_response.next.url = 'https://example.com/callback?code=test_code'

        with patch.object(oauth_client, '_get'), \
             patch.object(oauth_client, '_post', return_value=mock_auth_response):
            code = oauth_client._get_code()
            assert code == 'test_code'

    def test_get_code_failure(self, oauth_client):
        mock_auth_response = MagicMock()
        mock_auth_response.status_code = HTTPStatus.UNAUTHORIZED

        with patch.object(oauth_client, '_get'), \
             patch.object(oauth_client, '_post', return_value=mock_auth_response):
            with pytest.raises(ZenmoneyRequestError) as exc_info:
                oauth_client._get_code()
            assert "Authorization failed" in str(exc_info.value)

    def test_token_property(self, oauth_client):
        mock_token = MagicMock()
        mock_token.is_valid = True

        with patch.object(oauth_client, '_get_token', return_value=mock_token) as mock_get_token:
            # First call should get new token
            token = oauth_client.token
            assert token == mock_token
            mock_get_token.assert_called_once()

            # Second call should use cached token
            token = oauth_client.token
            assert token == mock_token
            mock_get_token.assert_called_once()  # Still only called once

    def test_token_property_invalid_token(self, oauth_client):
        mock_token = MagicMock()
        mock_token.is_valid = False

        with patch.object(oauth_client, '_get_token', return_value=mock_token) as mock_get_token:
            # First call with invalid token should get new token
            token = oauth_client.token
            assert token == mock_token
            mock_get_token.assert_called_once()

            # Second call should get new token again since previous was invalid
            token = oauth_client.token
            assert token == mock_token
            assert mock_get_token.call_count == 2 