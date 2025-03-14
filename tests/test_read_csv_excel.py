from unittest.mock import patch
from typing import Any

from src.read_csv_excel import read_file_csv, read_file_excel


@patch("pandas.read_csv")
def test_read_csv_file(mock_read_csv: Any) -> None:
    """Тестирование функции считывания CSV-файла"""
    mock_read_csv.return_value.to_dict.return_value = [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]
    result = read_file_csv("test_file_path.csv")
    assert result == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]



def test_read_not_csv() -> None:
    assert read_file_csv("test_file.json") == []


@patch("pandas.read_excel")
def test_read_excel_file(mock_read_excel: Any) -> None:
    """Тестирование функции считывания EXCEL-файла"""
    mock_read_excel.return_value.to_dict.return_value = [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"}
    ]
    result = read_file_excel("test_file_path.xlsx")
    assert result == [{"test_dict": "01", "test_key": "test_value_1"}, {"test_dict": "02", "test_key": "test_value_2"}]


def test_read_not_excel() -> None:
    assert read_file_csv("test_file.json") == []