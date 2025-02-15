def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    if len(str(card_number)) != 16:
        return "Проверьте номер карты"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    if len(str(account_number)) != 20:
        return "Проверьте номер счета"
    return f"**{account_number[-4:]}"
