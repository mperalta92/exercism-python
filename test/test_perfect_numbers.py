import unittest
from perfect_numbers import classify

class TestPerfectNumbers(unittest.TestCase):

    def test_negative_number_is_rejected(self):
        with self.assertRaises(ValueError):
            classify(-1)
        

    def test_zero_is_rejected(self):
        with self.assertRaises(ValueError):
            classify(0)

    def test_six_is_perfect(self):
        self.assertEqual('Perfect', classify(6))
