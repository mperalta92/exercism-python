import unittest
from sublist import sublist, SUBLIST, SUPERLIST, EQUAL, UNEQUAL


class TestSublist(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(
            sublist([], []),
            EQUAL
        )

    def test_empty_list_within_non_empty_list(self):
        self.assertEqual(
            sublist([], [1, 2, 3]),
            SUBLIST
        )
    
    def test_non_empty_list_contains_empty_list(self):
        self.assertEqual(
            sublist([1, 2, 3], []),
            SUPERLIST
        )
    
    def test_list_equals_itself(self):
        self.assertEqual(
            sublist([1, 2, 3], [1, 2, 3]),
            EQUAL
        )

    def test_different_lists(self):
        self.assertEqual(
            sublist([1, 2, 3], [2, 3, 4]),
            UNEQUAL
        )

    def test_false_start(self):
        self.assertEqual(
            sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]),
            SUBLIST
        )

    def test_consecutive(self):
        self.assertEqual(
            sublist([1, 1, 2], [0, 1, 1, 1, 2, 1, 2]),
            SUBLIST
        )

    def test_sublist_at_start(self):
        self.assertEqual(
            sublist([0, 1, 2], [0, 1, 2, 3, 4, 5]),
            SUBLIST
        )

    def test_sublist_in_middle(self):
        self.assertEqual(
            sublist([2, 3, 4], [0, 1, 2, 3, 4, 5]),
            SUBLIST
        )
    
    def test_sublist_at_end(self):
        self.assertEqual(
            sublist([3, 4, 5], [0, 1, 2, 3, 4, 5]),
            SUBLIST
        )
    
    