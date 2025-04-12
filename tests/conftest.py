import pytest
from unittest.mock import MagicMock
import time
from datetime import datetime

from zenmoney.oauth2 import ZenmoneyOAuth2
from zenmoney.models import Token, Diff, Tag, User, Account, Transaction


@pytest.fixture
def mock_response():
    """Создает мок ответа от сервера"""
    response = MagicMock()
    response.raise_for_status.return_value = None
    return response


@pytest.fixture
def valid_token_data():
    """Данные для создания валидного токена"""
    current_time = int(time.time())
    return {
        'access_token': 'test_access_token',
        'token_type': 'bearer',
        'expires_in': current_time + 3600,  # Expires in 1 hour
        'refresh_token': 'test_refresh_token'
    }


@pytest.fixture
def expired_token_data():
    """Данные для создания истекшего токена"""
    current_time = int(time.time())
    return {
        'access_token': 'test_access_token',
        'token_type': 'bearer',
        'expires_in': current_time - 1,  # Expired 1 second ago
        'refresh_token': 'test_refresh_token'
    }


@pytest.fixture
def mock_token(valid_token_data):
    """Создает валидный токен"""
    return Token(**valid_token_data)


@pytest.fixture
def oauth_client():
    """Создает клиент OAuth2 с тестовыми данными"""
    return ZenmoneyOAuth2(
        consumer_key='test_key',
        consumer_secret='test_secret',
        username='test_user',
        password='test_pass'
    )


@pytest.fixture
def sample_tag_data():
    """Данные для создания тегов"""
    return {
        "id": "123e4567-e89b-12d3-a456-426614174000",  # Валидный UUID
        "title": "Test Tag",
        "changed": 1234567890,
        "user": 1,
        "parent": None,
        "icon": None,
        "picture": None,
        "color": None,
        "showIncome": True,
        "showOutcome": True,
        "budgetIncome": True,
        "budgetOutcome": True,
        "required": False,
    }


@pytest.fixture
def sample_user_data():
    """Данные для создания пользователя"""
    return {
        "id": 1,
        "changed": 1234567890,
        "login": "test_user",
        "currency": 643,
        "countryCode": "RU",
        "parent": None,
        "company": None,
        "paidTill": None,
        "subscription": None,
        "email": "test@example.com",
        "planSettings": "free",
        "planBalanceMode": "default",
        "isForecastEnabled": False,
    }


@pytest.fixture
def sample_account_data():
    """Данные для создания счета"""
    return {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "user": 1,
        "instrument": 643,
        "type": "ccard",
        "role": None,
        "private": False,
        "title": "Test Account",
        "inBalance": True,
        "creditLimit": 0,
        "startBalance": 0,
        "balance": 1000,
        "company": None,
        "archive": False,
        "enableCorrection": False,
        "enableSMS": False,
        "startDate": None,
        "capitalization": None,
        "percent": None,
        "changed": 1234567890,
        "syncID": None,
        "balanceCorrectionType": "request",
    }


@pytest.fixture
def sample_transaction_data():
    """Данные для создания транзакции"""
    return {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "user": 1,
        "income": 1000,
        "incomeInstrument": 643,
        "incomeAccount": "123e4567-e89b-12d3-a456-426614174000",
        "incomeBankID": None,
        "outcome": 1000,
        "outcomeInstrument": 643,
        "outcomeAccount": "123e4567-e89b-12d3-a456-426614174000",
        "outcomeBankID": None,
        "tag": ["123e4567-e89b-12d3-a456-426614174000"],
        "merchant": None,
        "payee": None,
        "comment": "Test transaction",
        "date": "2024-01-01T00:00:00Z",
        "reminderMarker": None,
        "created": 1234567890,
        "changed": 1234567890,
        "deleted": False,
        "qrCode": None,
        "latitude": None,
        "longitude": None,
        "viewed": False,
    }


@pytest.fixture
def sample_merchant_data():
    """Данные для создания продавца/магазина"""
    return {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "user": 1,
        "title": "Test Merchant",
        "changed": 1234567890,
        "parent": None,
        "icon": None,
        "picture": None,
        "color": None,
        "showIncome": True,
        "showOutcome": True,
        "budgetIncome": True,
        "budgetOutcome": True,
        "required": False,
    }


@pytest.fixture
def sample_reminder_data():
    """Данные для создания напоминания"""
    return {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "user": 1,
        "income": 1000,
        "incomeInstrument": 643,
        "incomeAccount": "123e4567-e89b-12d3-a456-426614174000",
        "outcome": 1000,
        "outcomeInstrument": 643,
        "outcomeAccount": "123e4567-e89b-12d3-a456-426614174000",
        "tag": ["123e4567-e89b-12d3-a456-426614174000"],
        "merchant": "123e4567-e89b-12d3-a456-426614174000",
        "payee": "Test Payee",
        "comment": "Test Reminder",
        "interval": None,
        "step": None,
        "points": None,
        "startDate": "2024-01-01",
        "endDate": None,
        "notify": True,
        "changed": 1234567890,
    }


@pytest.fixture
def sample_reminder_marker_data():
    """Данные для создания маркера напоминания"""
    return {
        "id": "4ece63b4-6f79-47e1-9c02-188613202211",
        "tag": ["0dfa6b37-2e78-4b76-9c83-75e6c7830d83"],
        "date": "2025-05-01",
        "user": 565145,
        "payee": "Тинькофф",
        "state": "planned",
        "income": 0,
        "notify": False,
        "changed": 1714516510,
        "comment": "Подписка \"Tinkoff Pro\"",
        "outcome": 1990,
        "merchant": None,
        "reminder": "b65bd69f-8024-4e60-a2e1-83422955f4c4",
        "isForecast": False,
        "incomeAccount": "b88e8d81-2fb8-4d50-966e-95c0a5d7a808",
        "outcomeAccount": "b88e8d81-2fb8-4d50-966e-95c0a5d7a808",
        "incomeInstrument": 2,
        "outcomeInstrument": 2
    }


@pytest.fixture
def sample_budget_data():
    """Данные для создания бюджета"""
    return {
        "tag": "2855c4f7-c9bf-4600-8ded-4578292b167a",
        "date": "2024-05-01",
        "user": 565145,
        "income": 119998,
        "changed": 1713778648,
        "outcome": 0,
        "incomeLock": False,
        "outcomeLock": False,
        "isIncomeForecast": False,
        "isOutcomeForecast": True
    }


@pytest.fixture
def sample_diff_data(sample_tag_data, sample_user_data, sample_account_data, sample_transaction_data, sample_merchant_data, sample_reminder_data, sample_reminder_marker_data, sample_budget_data):
    """Данные для создания Diff объекта"""
    current_time = int(time.time())
    return {
        "serverTimestamp": current_time,
        "currentClientTimestamp": current_time - 100,
        "tag": [sample_tag_data],
        "user": [sample_user_data],
        "account": [sample_account_data],
        "transaction": [{
            **sample_transaction_data,
            "viewed": False  # Добавляем поле viewed в транзакцию
        }],
        "merchant": [sample_merchant_data],
        "reminder": [sample_reminder_data],
        "reminderMarker": [sample_reminder_marker_data],
        "budget": [sample_budget_data],
        "forceFetch": ["tag", "user"],
    } 