from typing import Any, Callable

from src.masks import account_mask, card_mask


def test_account_mask(account_fixture: Callable[[], str]) -> Any:
    assert account_mask("12345678909876543210") == "**3210"


def test_card_mask(card_fixture: Callable[[], str]) -> Any:
    assert card_mask("1234567876543210") == "1234 56** **** 3210"
