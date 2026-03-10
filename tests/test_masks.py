import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, card_mask",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("", "Введите корректный номер"),
        ("700079dasd606361", "Введите корректный номер"),
        ("145987", "Введите корректный номер"),
    ],
)
def test_mask_card_number(card_number, card_mask):
    assert get_mask_card_number(card_number) == card_mask


@pytest.mark.parametrize(
    "account_number, account_mask",
    [
        ("73654108430135874305", "Счет **4305"),
        ("73654108435874305", "Счет **4305"),
        ("", "Введите корректный номер"),
        ("456", "Введите корректный номер"),
        ("asdasd4123asd", "Введите корректный номер"),
    ],
)
def test_mask_account(account_number, account_mask):
    assert get_mask_account(account_number) == account_mask
