# Домашняя работа skypro

## Описание:

Домашняя работа skypro - это работа над виджетом банковских операций клиента.

## Установка:

Клонируйте репозиторий:
```
git clone https://github.com/inessa220/homework.git
```
## Использование:

1. Откройте работу для проверки на вашем устройстве.
2. Проверьте работу.
3. Сообщите об ошибках, если они имеются

## Документация:

Для получения дополнительной информации обратитесь к README.md

## Тестирование:

### Модуль masks

Функция get_mask_card_number: Тестирование правильности маскирования номера карты.
Функция get_mask_account: Тестирование правильности маскирования номера счета.

### Модуль widget

Функция mask_account_card: Тестирование, что функция распознает и применяет нужный тип маскировки,
в зависимости от типа входных данных.
Функция get_date: Тестирование правильности преобразования даты.

### Модуль processing

Функция filter_by_state: Тестирование фильтрации списка словарей по заданному статусу.
Функция sort_by_date: Тестирование сортировки списка словарей по датам.


## Тестирование:

### Модуль masks

Функция get_mask_card_number: Тестирование правильности маскирования номера карты.
Функция get_mask_account: Тестирование правильности маскирования номера счета.

### Модуль widget

Функция mask_account_card: Тестирование, что функция распознает и применяет нужный тип маскировки,
в зависимости от типа входных данных.
Функция get_date: Тестирование правильности преобразования даты.

### Модуль processing

Функция filter_by_state: Тестирование фильтрации списка словарей по заданному статусу.
Функция sort_by_date: Тестирование сортировки списка словарей по датам.

###  Модуль generators

Функция filter_by_currency: Тестирование корректной фильтрации списка транзаций по заданной валюте.
Функция transaction_descriptions: Тестирование корректных описаний для каждой транзации.
Функция card_number_generator: Тестирование выдачи правильных номеров карт.

### Модуль decorators

Декоратор log: Тестирование записи логов в файл или в консоль.

### Модуль utils

Функция get_operation: Тестирование возврата корректных данных из JSON-файла.

### Модуль external_api

Функция get_transaction: Тестирование вывода корректной суммы транзакции в рублях.

### Модуль read_csv_excel

Функция read_file_csv: Тестирование чтения файла CSV и преобразования данных в список транзакций.
Функция read_file_excel: Тестирование чтения файла EXCEL и преобразования данных в список транзакций.

### Модуль main

Написана функция, отвечающая за основную логику проекта и связывающая функциональности между собой.