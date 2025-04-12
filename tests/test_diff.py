import pytest
from datetime import datetime

from zenmoney.models import Diff, Tag, User, Account, Transaction
from zenmoney.models.utils import check_dict_type


class TestDiff:
    """Тесты модели Diff"""

    def test_diff_creation(self, sample_diff_data):
        """Проверяет создание Diff объекта"""
        diff = Diff.from_dict(sample_diff_data)
        
        assert diff.server_timestamp == sample_diff_data["serverTimestamp"]
        assert diff.current_client_timestamp == sample_diff_data["currentClientTimestamp"]
        assert len(diff.tag) == 1
        assert len(diff.user) == 1
        assert len(diff.account) == 1
        assert len(diff.transaction) == 1
        assert len(diff.merchant) == 1
        assert len(diff.reminder) == 1
        assert len(diff.reminder_marker) == 1
        assert len(diff.budget) == 1
        assert diff.force_fetch == sample_diff_data["forceFetch"]

    def test_diff_with_empty_data(self):
        """Проверяет создание Diff объекта с пустыми данными"""
        data = {
            "serverTimestamp": 1234567890,
            "currentClientTimestamp": 1234567890,
        }
        diff = Diff.from_dict(data)
        
        assert diff.server_timestamp == data["serverTimestamp"]
        assert diff.current_client_timestamp == data["currentClientTimestamp"]
        assert diff.tag == []
        assert diff.user == []
        assert diff.account == []
        assert diff.transaction == []
        assert diff.force_fetch is None

    def test_diff_with_invalid_data(self):
        """Проверяет создание Diff объекта с невалидными данными"""
        with pytest.raises(TypeError):
            Diff.from_dict("invalid data")

    def test_diff_with_invalid_force_fetch(self):
        """Проверяет создание Diff объекта с невалидным force_fetch"""
        data = {
            "serverTimestamp": 1234567890,
            "currentClientTimestamp": 1234567890,
            "forceFetch": "invalid",  # Должен быть списком
        }
        with pytest.raises(TypeError):
            Diff.from_dict(data)

    def test_diff_to_dict(self, sample_diff_data):
        """Проверяет преобразование Diff объекта в словарь"""
        diff = Diff.from_dict(sample_diff_data)
        result = diff.to_dict()
        
        assert result["serverTimestamp"] == sample_diff_data["serverTimestamp"]
        assert result["currentClientTimestamp"] == sample_diff_data["currentClientTimestamp"]
        assert len(result["tag"]) == 1
        assert len(result["user"]) == 1
        assert len(result["account"]) == 1
        assert len(result["transaction"]) == 1
        assert result["forceFetch"] == sample_diff_data["forceFetch"]

    def test_diff_to_dict_with_empty_data(self):
        """Проверяет преобразование пустого Diff объекта в словарь"""
        data = {
            "serverTimestamp": 1234567890,
            "currentClientTimestamp": 1234567890,
        }
        diff = Diff.from_dict(data)
        result = diff.to_dict()
        
        assert result["serverTimestamp"] == data["serverTimestamp"]
        assert result["currentClientTimestamp"] == data["currentClientTimestamp"]
        assert "tag" not in result
        assert "user" not in result
        assert "account" not in result
        assert "transaction" not in result
        assert "forceFetch" not in result

    def test_diff_with_invalid_force_fetch_values(self):
        """Проверяет создание Diff объекта с невалидными значениями в force_fetch"""
        data = {
            "serverTimestamp": 1234567890,
            "currentClientTimestamp": 1234567890,
            "forceFetch": ["invalid_class_name"],  # Несуществующий класс
        }
        with pytest.raises(ValueError):
            Diff.from_dict(data)

    def test_diff_with_partial_data(self, sample_tag_data, sample_user_data):
        """Проверяет создание Diff объекта с частичными данными"""
        data = {
            "serverTimestamp": 1234567890,
            "currentClientTimestamp": 1234567890,
            "tag": [sample_tag_data],
            "user": [sample_user_data],
        }
        diff = Diff.from_dict(data)
        
        assert diff.server_timestamp == data["serverTimestamp"]
        assert diff.current_client_timestamp == data["currentClientTimestamp"]
        assert len(diff.tag) == 1
        assert len(diff.user) == 1
        assert diff.account == []
        assert diff.transaction == []
        assert diff.force_fetch is None 