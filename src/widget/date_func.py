from datetime import datetime


def date_func(date: str) -> str:
    """Принимает дату и возвращает в привычном формате"""
    return datetime.fromisoformat(date).strftime("%d.%m.%Y")
