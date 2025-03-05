import os

from unittest.mock import patch
from src.external_api import get_transaction


from dotenv import load_dotenv

load_dotenv(".env")

api_key = os.getenv("API_KEY")


def test_get_transaction():
    """Тестирование функции на получение суммы в рублях"""
    rub_data = {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount": {
        "amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719", "to": "Счет 74489636417521191160"}
    assert get_transaction(rub_data) == 43318.34


@patch("requests.get")
def test_get_transaction_USD(mock_get):
    """Тестирование функции конвертации на получение суммы в рублях"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.0}
    transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}
    result = get_transaction(transaction)
    assert result == 75.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1", headers={"apikey": api_key}
    )


@patch("requests.get")
def test_get_transaction_invalid(mock_get):
    """Тестирование функции конвертации иностранных валют в рубли"""
    mock_get.return_value.status_code = 404
    mock_get.return_value.reason = "The requested resource doesn't exist."
    assert get_transaction(mock_get) == 0.0
