"""Tests suite for opener package"""

import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    ".."))
sys.path.insert(0, BASEDIR)
import opener


class TestOpener(unittest.TestCase):
    """Test class of the package"""

    def test_get_keys_three_digits(self):
        """Test 3 digits lock"""
        number_of_positions = 3
        invalid_digits = (5, 2, 3)
        similarity_conditions = (
            ([9, 6, 4], 2),
            ([2, 8, 6], 1),
            ([1, 4, 7], 1),
            ([1, 8, 9], 1)
        )
        invalid_positioned_values = ((9, 1), (6, 8, 4), (4, 6, 7))
        valid_positioned_values = ((1,), (8,), (9,))
        unlock_keys = opener.get_keys(number_of_positions,
                                      similarity_conditions,
                                      invalid_digits,
                                      invalid_positioned_values,
                                      valid_positioned_values)
        self.assertListEqual(unlock_keys, ["679"])

    def test_get_keys_four_digits(self):
        """Test 4 digits lock"""
        number_of_positions = 4
        invalid_digits = (5, 1, 2, 4)
        similarity_conditions = (
            ([3, 5, 4, 8], 1),
            ([4, 6, 7, 1], 2),
            ([3, 7, 8, 1], 2),
            ([8, 3, 9, 7], 3),
            ([2, 9, 3, 4], 1),
            ([5, 1, 3, 6], 1),
        )
        invalid_positioned_values = ((3, 8, 2), (5, 7, 3, 9),
                                     (4, 8, 9, 3), (8, 1, 7, 4))
        valid_positioned_values = ((5,), (1,), (3,), (6,))
        unlock_keys = opener.get_keys(number_of_positions,
                                      similarity_conditions,
                                      invalid_digits,
                                      invalid_positioned_values,
                                      valid_positioned_values)
        self.assertListEqual(unlock_keys, ["9876"])


if __name__ == "__main__":
    unittest.main()
