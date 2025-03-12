from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card: str) -> str | None:
    """Функция, маскирующая номер карты или счета"""
    numb = ""
    name = ""
    for c in card:
        if c.isdigit():
            numb += str(c)
        else:
            name += str(c)
    if len(numb) == 16:
        numb_mask = get_mask_card_number(numb)
        mask = name + numb_mask
        return mask
    elif len(numb) == 20:
        numb_mask = get_mask_account(numb)
        mask = name + numb_mask
        return mask
    else:
        numb_mask = get_mask_account(numb)
        mask = numb_mask
        return mask


def get_date(date: str) -> str:
    """Функция, форматирующая дату"""
    if len(date) < 26:
        return "Неверный формат даты"
    else:
        date_slice = date[0:10].split("-")
        result = ".".join(date_slice[::-1])
        return result
