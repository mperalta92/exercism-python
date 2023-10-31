import unittest
from all_your_base import rebase, divide, decimal_to_output_base, map_input_base_to_decimal, input_base_to_decimal

class TestAllYourBase(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide(10, 2), (5, 0))
        self.assertEqual(divide(10, 3), (3, 1))
        self.assertEqual(divide(10, 4), (2, 2))

    def test_decimal_to_output_base(self):
        self.assertEqual(decimal_to_output_base(10, 2), [1,0,1,0])
        self.assertEqual(decimal_to_output_base(10, 3), [1,0,1])
        self.assertEqual(decimal_to_output_base(10, 4), [2,2])

    def test_map_input_base_to_decimal(self):
        self.assertEqual(map_input_base_to_decimal('A'), 10)
        self.assertEqual(map_input_base_to_decimal('F'), 15)
        self.assertEqual(map_input_base_to_decimal('Z'), 35)
        self.assertEqual(map_input_base_to_decimal('0'), 0)
        self.assertEqual(map_input_base_to_decimal('9'), 9)

    def test_input_base_to_decimal(self):
        self.assertEqual(input_base_to_decimal(2, [1,0,1,0]), 10)
        self.assertEqual(input_base_to_decimal(3, [1,0,1]), 10)
        self.assertEqual(input_base_to_decimal(4, [2,2]), 10)

    def test_single_bit_one_to_decimal(self):
        self.assertEqual(rebase(2, [1], 10), [1])
        self.assertEqual(rebase(10, [0], 2), [0])
      