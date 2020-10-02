# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    ".."))
sys.path.insert(0, BASEDIR)
import opener


class TestOpener(unittest.TestCase):
    def test_get_keys(self):
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


if __name__ == "__main__":
    unittest.main()
