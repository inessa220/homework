from src.masks import get_mask_card_number, get_mask_account



def mask_account_card (card: str) -> str | None:
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
    else:
        numb_mask = get_mask_account(numb)
        mask = name + numb_mask
        return mask


def get_date (date: str) -> str:
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


