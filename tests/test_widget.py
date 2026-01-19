import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_account, mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("", "Введите корректные данные"),
        ("Счет 26551", "Введите корректные данные"),
        ("Maestro 15905199", "Введите корректные данные"),
        ("azjkhdkjashdkjahsdjk", "Введите корректные данные"),
        ("7894561321534684321", "Введите корректные данные"),
        ("7897546", "Введите корректные данные"),
    ],
)
def test_mask_account_card(card_account, mask):
    assert mask_account_card(card_account) == mask


@pytest.mark.parametrize(
    "date_name, date_mask",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-04-11T02:26:18.671407", "11.04.2025"),
        ("asdasd", "Введите корректную дату"),
        ("2024-03-11T02:26:", "Введите корректную дату"),
        ("213123123", "Введите корректную дату"),
        ("2024-03-11T02:26:18-671407asd", "Введите корректную дату"),
    ],
)
def test_date_mask(date_name, date_mask):
    assert get_date(date_name) == date_mask
