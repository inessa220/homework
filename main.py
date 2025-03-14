import re

from src.utils import get_operation
from src.read_csv_excel import read_file_csv, read_file_excel
from src.processing import filter_by_state, sort_by_date
from collections import Counter
from src.widget import mask_account_card, get_date


def search_by_string(operations_list: list[dict], search_string: str) -> list[dict]:
    """Поиск в списке операций по заданной строке."""
    pattern = re.compile(search_string, re.IGNORECASE)
    filtered_transaction = [
        transaction for transaction in operations_list if pattern.search(transaction.get("description", ""))]
    return filtered_transaction


def count_operations(operations_list: list[dict], categories: list) -> dict:
    """Функция подсчета операций по категориям"""
    counted = Counter()
    for operation in operations_list:
        descr = str(operation["description"]).lower()
        if len(descr) > 0:
            for category in categories:
                if len(category) > 0:
                    if category.lower() in descr:
                        counted[category] += 1
                else:
                    print("Ошибка запроса")
                    return {}
        else:
            print("Ошибка запроса")
            return {}
    return dict(counted)


def main():
    """Общая функция, связывающая все функциональности"""
    while True:
        print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
              "Выберите необходимый пункт меню:\n"
              "1. Получить информацию о транзакциях из JSON-файла\n"
              "2. Получить информацию о транзакциях из CSV-файла\n"
              "3. Получить информацию о транзакциях из XLSX-файла)")
        answer_1 = input("Введите число: ")
        if answer_1 == "1":
            print("Для обработки выбран JSON-файл.")
            operation = get_operation(r"C:\Users\Инесса\Desktop\PythonProject2\data\operations.json")
            break
        elif answer_1 == "2":
            print("Для обработки выбран CSV-файл.")
            operation = read_file_csv(r"C:\Users\Инесса\Desktop\PythonProject2\data\transactions.csv")
            break
        elif answer_1 == "3":
            print("Для обработки выбран XLSX-файл.")
            operation = read_file_excel(r"C:\Users\Инесса\Desktop\PythonProject2\data\transactions_excel.xlsx")
        else:
            print("Ошибка ввода! Попробуйте еще раз.")

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.\n"
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING)")
        answer_2 = input("Введите ответ: ").upper()
        if answer_2 == "EXECUTED" or answer_2 == "CANCELED" or answer_2 == "PENDING":
            filter_operation = filter_by_state(operation, answer_2)
            print(f"Операции отфильтрованы по статусу {answer_2}")
            break
        else:
            print(f"Статус операции {answer_2} недоступен. Попробуйте еще раз.\n"
                  "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                  "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

    while True:
        print("Отсортировать операции по дате? Да/Нет?")
        filter_1 = input("Введите 'да' или 'нет': ").lower()
        if filter_1 == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            filter_2 = input("по возрастанию/по убыванию? ").lower()
            if filter_2 == "по убыванию":
                filter_date = sort_by_date(filter_operation, True)
                break
            elif filter_2 == "по возрастанию":
                filter_date = sort_by_date(filter_operation, False)
                break
            else:
                print("Ошибка ввода! Попробуйте еще раз.")
        elif filter_1 == "нет":
            filter_date = filter_operation
            break
        else:
            print("Ошибка ввода! Попробуйте еще раз.")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет?")
        filter_3 = input("Введите да или нет: ").lower()
        if filter_3 == "да":
            filter_currency = []
            for operation in filter_date:
                if answer_1 == "1":
                    if operation["operationAmount"]["currency"]["code"] == "RUB":
                        filter_currency.append(operation)
                        break
                elif answer_1 == "2" or answer_1 == "3":
                    if operation["currency_code"] == "RUB":
                        filter_currency.append(operation)
                        break
            if len(filter_currency) == 0:
                return "Рублевые транзакции не найдены"
            else:
                break
        elif filter_3 == "нет":
            filter_currency = filter_date
            break
        else:
            print("Ошибка ввода! Попробуйте еще раз.")

    while True:
        print("Отфильтровать список транзаций по определенному слову в описании? Да/Нет")
        filter_4 = input("Введите да или нет: ").lower()
        if filter_4 == "да":
            user_search = input("Введите слово или фразу для поиска: ")
            filtered = search_by_string(filter_currency, user_search)
            break
        elif filter_4 == "нет":
            filtered = filter_currency
            break
        else:
            print("Ошибка ввода! Попробуйте еще раз")
    if len(filtered) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return []

    print("Распечатываю итоговый список транзакций...")
    print(f"Банковских операций в выборке: {len(filtered)}")

    for operation in filtered:
        date = get_date(operation.get("date"))
        description = operation.get("description")
        print(f"{date} {description}")

        if operation.get("description") == "Открытие вклада":
            acc_number = mask_account_card(operation["to"])
            print(acc_number)
            if answer_1 == "1":
                amount = operation["operationAmount"]["amount"]
                currency_name = operation["operationAmount"]["currency"]["name"]
                print(f"Сумма: {amount} {currency_name}")
            elif answer_1 == "2" or answer_1 == "3":
                amount = operation["amount"]
                currency_name = operation["currency_name"]
                print(f"Сумма: {amount} {currency_name}")
        else:
            acc_number_from = mask_account_card(operation["from"])
            acc_number_to = mask_account_card(operation["to"])
            print(f"{acc_number_from} -> {acc_number_to}")
            if answer_1 == "1":
                amount = operation["operationAmount"]["amount"]
                currency_name = operation["operationAmount"]["currency"]["name"]
                print(f"Сумма: {amount} {currency_name}")
            elif answer_1 == "2" or answer_1 == "3":
                amount = operation["amount"]
                currency_name = operation["currency_name"]
                print(f"Сумма: {amount} {currency_name}")


if __name__ == "__main__":
    result = main()
