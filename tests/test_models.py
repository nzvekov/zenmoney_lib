import pytest
from datetime import datetime, timedelta
import time

from zenmoney.models import Token


class TestToken:
    """Тесты модели токена"""

    def test_token_creation(self, valid_token_data):
        """Проверяет создание токена"""
        token = Token(**valid_token_data)
        assert token.access_token == valid_token_data['access_token']
        assert token.token_type == valid_token_data['token_type']
        assert token.expires_in == valid_token_data['expires_in']
        assert token.refresh_token == valid_token_data['refresh_token']

    def test_token_is_valid(self, valid_token_data):
        """Проверяет валидность токена"""
        token = Token(**valid_token_data)
        assert token.is_valid is True

    def test_token_is_invalid(self, expired_token_data):
        """Проверяет невалидность истекшего токена"""
        token = Token(**expired_token_data)
        assert token.is_valid is False

    def test_token_from_dict(self, valid_token_data):
        """Проверяет создание токена из словаря"""
        token = Token(**valid_token_data)
        assert token.access_token == valid_token_data['access_token']
        assert token.token_type == valid_token_data['token_type']
        assert token.expires_in == valid_token_data['expires_in']
        assert token.refresh_token == valid_token_data['refresh_token']

    def test_token_missing_fields(self):
        """Проверяет создание токена с отсутствующими полями"""
        with pytest.raises(TypeError):
            Token(
                access_token='test_access_token',
                token_type='bearer'
                # Missing expires_in and refresh_token
            ) 