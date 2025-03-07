import logging
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(cur_dir, "../logs", "masks.log")
abs_file_path = os.path.abspath(path)

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(abs_file_path, "w")
file_formatter = logging.Formatter('%(acstime)s - %(name)s - %(level)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    logger.info("Создаем маску банковской карты")
    if len(str(card_number)) != 16:
        logger.error("Ошибка! Введен некорректный номер карты")
        return "Проверьте номер карты"
    else:
        logger.info("Создание маски карты успешно")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    if len(str(account_number)) != 20:
        return "Проверьте номер счета"
    return f"**{account_number[-4:]}"
