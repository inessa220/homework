from src.masks import get_mask_card_number
from src.masks import get_mask_account


card_number = input("Введите номер карты: ")
print(get_mask_card_number(card_number))

account_number = input("Введите номер счета: ")
print(get_mask_account(account_number))
