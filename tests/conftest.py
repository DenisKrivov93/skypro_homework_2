import pytest


@pytest.fixture
def account_fixture() -> str:
    return "**3210"


@pytest.fixture
def card_fixture() -> str:
    return "1234 56** **** 3210"
