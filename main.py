from src.widget import mask_account_card, get_date


card = input("Введите номер карты: ")
print(mask_account_card(card))


date = input("Введите дату: ")
print(get_date(date))
