import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "account_card, mask_account",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ]
)
def test_mask_account_card(account_card: str, mask_account: str) -> None:
    assert mask_account_card(account_card) == mask_account


def test_mask_account_card_dif(account):
    assert mask_account_card("Visa Platinum 70007922896") == account

    assert mask_account_card("Счет 7365410843013587430545654") == account


@pytest.mark.parametrize(
    "date, result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.4255722", "30.06.2018"),
    ],
)
def test_get_date(date: str, result: str) -> None:
    """Функция передает строку с датой"""
    assert get_date(date) == result


def test_get_date_dif(different_date):
    assert get_date("30.06.2018") == different_date

    assert get_date("2019-07-03T18:35:29") == different_date
