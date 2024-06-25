import unittest

from src.widget.decorators import add, divide


class TestLogDecorator(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_divide(self):
        result = divide(6, 2)
        self.assertEqual(result, 3)
