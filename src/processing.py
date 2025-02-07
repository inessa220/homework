def filter_by_state(list_of_dictionary: list, choose_state: str = "EXECUTED") -> list:
    """Функция, принимающая список словарей и возвращающая новый, где state соответствует
    значению, по умолчанию EXECUTED"""
    new_list_of_dictionary = []
    for dictionary in list_of_dictionary:
        if dictionary.get("state") == choose_state:
            new_list_of_dictionary.append(dictionary)
    return new_list_of_dictionary



