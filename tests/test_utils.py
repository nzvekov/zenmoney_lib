from unittest.mock import MagicMock

import pytest
import requests

from zenmoney.exception import ZenmoneyRequestError
from zenmoney.utils import convert_response_to_json


class TestConvertResponseToJson:
    """Тесты функции convert_response_to_json"""

    def test_invalid_json_raises_zenmoney_request_error(self):
        """Проверяет, что при невалидном JSON выбрасывается ZenmoneyRequestError"""
        mock_response = MagicMock()
        mock_response.json.side_effect = requests.exceptions.JSONDecodeError("Expecting value", "", 0)

        with pytest.raises(ZenmoneyRequestError) as exc_info:
            convert_response_to_json(mock_response)

        assert "Failed to convert response to JSON" in str(exc_info.value)
        assert exc_info.value.__cause__ is mock_response.json.side_effect
