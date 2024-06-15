import pytest


@pytest.fixture
def account_fixture():
    return "**3210"


@pytest.fixture
def card_fixture():
    return "1234 56** **** 3210"
