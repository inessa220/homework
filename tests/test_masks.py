import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, mask_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
    ],
)
def test_mask_card(card_number: str, mask_card: str) -> None:
    assert get_mask_card_number(card_number) == mask_card


def test_masks_card_dif(card):
    assert get_mask_card_number("7000792289606361123") == card

    assert get_mask_card_number("") == card


@pytest.mark.parametrize(
    "account_number, mask_account",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ]
)
def test_mask_account(account_number: str, mask_account: str) -> None:
    assert get_mask_account(account_number) == mask_account


def test_mask_account_dif(account):
    assert get_mask_account("736541084301358367864533") == account

    assert get_mask_account("") == account
