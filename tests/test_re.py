from main import search_by_string, count_operations
from src.read_csv_excel import read_file_csv


def test_search_by_string():
    """Тестирование функции поиска операций по описанию"""
    transactions = [{"description": "Payment for service"}, {"description": "Refund for service"}]
    filtered = search_by_string(transactions, "Payment")
    assert filtered == [{"description": "Payment for service"}]


def test_failed_search_by_string():
    """Проверка некорректного описания для поиска или не найденного в списке операций"""
    transactions = [{"description": "Payment for service"}, {"description": "Refund for service"}]
    zero_result = search_by_string(transactions, "Открытие вклада")
    assert zero_result == []


def test_count_operations():
    """Тестирование функции подсчета операций"""
    operations = read_file_csv(r"C:\Users\Инесса\Desktop\PythonProject2\data\transactions.csv")
    count_result1 = count_operations(
        operations, ["Перевод с карты на карту", "Перевод со счета на счет", "Перевод организации"]
    )
    assert count_result1 == {
        "Перевод организации": 117,
        "Перевод с карты на карту": 587,
        "Перевод со счета на счет": 110,
    }
