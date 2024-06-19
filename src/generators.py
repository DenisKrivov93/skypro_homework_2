from typing import List, Dict


def filter_by_currency(transactions: List[Dict[str, str]], currency: str):
    """принимает список словарей с банковскими операциями
    и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта."""
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, str]]):
    """принимает список словарей и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        description = transaction.get("description", "Описание отсутствует")
        yield description


def card_number_generator(start, end):
    """генерирует номера карт в заданном диапозоне"""
    for num in range(start, end + 1):
        card_number = "{:04d} {:04d} {:04d} {:04d}".format(
            (num // 10**12) % 10**4, (num // 10**8) % 10**4, (num // 10**4) % 10**4, num % 10**4
        )
        yield card_number
