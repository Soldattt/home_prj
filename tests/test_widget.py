import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_account, mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card(card_account, mask):
    assert mask_account_card(card_account) == mask


@pytest.mark.parametrize(
    "date_name, date_mask",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-04-11T02:26:18.671407", "11.04.2025"),
    ],
)
def test_date_mask(date_name, date_mask):
    assert get_date(date_name) == date_mask
