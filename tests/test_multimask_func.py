from src.widget.multimask_func import multimask_func
import pytest


@pytest.mark.parametrize("string, expected", [
    ("Счет 12345678909876543210", "Счет **3210"),
    ("Visa Classic 1234567876543210", "Visa Classic 1234 56** **** 3210"),
    ("Visa Gold 1234567876543210", "Visa Gold 1234 56** **** 3210"),
    ("Maestro 1234567876543210", "Maestro 1234 56** **** 3210"),
    ("MasterCard 1234567876543210", "MasterCard 1234 56** **** 3210")
])
def test_multimask_func(string, expected):
    assert multimask_func(string) == expected


