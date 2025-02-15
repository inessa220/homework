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
