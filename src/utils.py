import json
import logging
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(cur_dir, "../logs", "utils.log")
abs_file_path = os.path.abspath(path)


logger = logging.getLogger("masks")
file_handler = logging.FileHandler(abs_file_path, "w")
file_formatter = logging.Formatter('%(acstime)s - %(name)s - %(level)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_operation(file_path: str) -> list:
    """Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    logger.info(f"Открытие JSON файла {file_path}")
    with open(file_path, "r") as file:
        try:
            operations = json.load(file)
            if len(operations) == 0 or type(operations) is not list:
                logger.error("Файл пустой")
                return []
            else:
                logger.info("Список транзакций успешно создан")
                return operations
        except Exception:
            logger.error("Ошибка")
            return []
