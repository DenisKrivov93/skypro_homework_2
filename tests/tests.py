from datetime import datetime


def date_func(date: str) -> str:
    return datetime.fromisoformat(date).strftime('%d.%m.%Y')


print(date_func("2018-07-11T02:26:18.671407"))
