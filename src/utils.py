import json


def get_operation(file_path: str) -> list:
    """Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    with open(file_path, "r") as file:
        try:
            operations = json.load(file)
            if len(operations) == 0:
                return []
            else:
                return operations
        except Exception:
            return ("Ошибка")
