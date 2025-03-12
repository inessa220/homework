from src.utils import get_operation
import os


def test_get_operations():
    """Тестирование функции получения данных из файла"""
    file_path = os.path.abspath("data/test_file.json")
    assert get_operation(file_path) == [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"},
    ]
