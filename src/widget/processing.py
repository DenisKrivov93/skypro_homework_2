from datetime import datetime
from typing import Dict, List


def filter_by_state(list_of_dicts: List[Dict[str, str]], target_state: str = "EXECUTED") -> List[Dict[str, str]]:
    """Принимает список словарей и возвращает новый список, содержащий только те словари, у которых ключ
    содержит переданное в функцию значение"""
    return [d for d in list_of_dicts if d.get("state") == target_state]


def sort_by_date(list_of_dicts: List[Dict[str, str]], reverse_order: bool = False) -> List[Dict[str, str]]:
    """Принимает список словарей и возвращает новый список, в котором исходные словари о
    тсортированы по убыванию даты"""
    return sorted(list_of_dicts, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=reverse_order)
