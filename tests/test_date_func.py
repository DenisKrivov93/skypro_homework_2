from src.widget.date_func import date_func


def test_date_func():
    assert date_func("2019-07-03T18:35:29.512364") == "03.07.2019"
