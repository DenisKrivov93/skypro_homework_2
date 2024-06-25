import unittest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тест первой функции
class TestFilterByCurrency(unittest.TestCase):

    def test_filter_by_currency(self):
        transactions = [
            {"currency": "USD", "amount": "100"},
            {"currency": "EUR", "amount": "200"},
            {"currency": "USD", "amount": "150"},
            {"currency": "GBP", "amount": "300"},
        ]
        currency = "USD"

        filtered_transactions = list(filter_by_currency(transactions, currency))

        self.assertEqual(len(filtered_transactions), 2)
        expected_transactions = [{"currency": "USD", "amount": "100"}, {"currency": "USD", "amount": "150"}]
        self.assertListEqual(filtered_transactions, expected_transactions)


# Тест второй функции
class TestTransactionDescriptions(unittest.TestCase):

    def test_transaction_descriptions(self):
        transactions = [
            {"description": "Перевод организации"},
            {"description": "Перевод со счета на счет"},
            {"description": "Перевод со счета на счет"},
            {"description": "Перевод с карты на карту"},
            {"description": "Перевод организации"},
        ]

        generator = transaction_descriptions(transactions)

        actual_descriptions = [next(generator) for _ in range(len(transactions))]
        expected_descriptions = [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]

        self.assertListEqual(actual_descriptions, expected_descriptions)

    def test_transaction_descriptions_no_description(self):
        transactions = [{"amount": "100"}, {"description": "Оплата услуг"}, {"description": "Покупка товаров"}]

        generator = transaction_descriptions(transactions)

        actual_descriptions = [next(generator) for _ in range(len(transactions))]
        expected_descriptions = ["Описание отсутствует", "Оплата услуг", "Покупка товаров"]

        self.assertListEqual(actual_descriptions, expected_descriptions)


# Тест третей функции
def test_card_number_generator():
    gen = card_number_generator(1, 5)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    assert next(gen) == "0000 0000 0000 0004"
    assert next(gen) == "0000 0000 0000 0005"
