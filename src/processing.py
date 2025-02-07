def filter_by_state(list_of_dictionary: list, choose_state: str = "EXECUTED") -> list:
    """Функция, принимающая список словарей и возвращающая новый, где state соответствует
    значению, по умолчанию EXECUTED"""
    new_list_of_dictionary = []
    for dictionary in list_of_dictionary:
        if dictionary.get("state") == choose_state:
            new_list_of_dictionary.append(dictionary)
    return new_list_of_dictionary


def sort_by_date(list_of_dictionary: list, sort: bool = True) -> list:
    """Функция, принимающая список словарей, сортирующая по дате, по умолчанию - убывание"""
    sorted_list = sorted(list_of_dictionary, key = lambda x: x["date"], reverse = sort)
    return sorted_list
