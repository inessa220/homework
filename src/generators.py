from typing import Iterable, Iterator


def filter_by_currency(transactions: Iterable[dict], currency: str) -> Iterator[dict]:
    """Функция, принимающая список словарей и валюту операции и
    возвращает поочередно транзации с заданной валютой"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: Iterable[dict]) -> Iterator[str]:
    """Функция, принимающая список словарей с транзакциями и возвращающая
    описание каждой операции поочереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор банковских номеров"""
    for num in range(start, stop + 1):
        number = "0" * (16 - len(str(num))) + str(num)
        return_string = ""
        block = 0
        for digit in number:
            block += 1
            if block <= 4:
                return_string += digit
            else:
                return_string += " " + digit
                block = 1
        yield return_string
