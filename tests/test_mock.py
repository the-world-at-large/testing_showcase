from unittest.mock import patch

from src.utils import fetch_data


def test_fetch_data():
    with patch("src.utils.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"key": "value"}
        assert fetch_data("https://fakeapi.com") == {"key": "value"}
        mock_get.assert_called_once_with("https://fakeapi.com", timeout=5)
