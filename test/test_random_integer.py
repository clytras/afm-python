"""Test get_random_int"""

# run test
# python3 .\test\test_random_integer.py -v
# or
# python3 -m unittest discover -s './test' -v
# run main
# python3 -m lytrax_afm

import package_resolve
import unittest

from lytrax_afm._utils import get_random_int
from helpers import *


class TestRandomInteger(unittest.TestCase):
    def test_generate_integers_with_range(self):
        """Generate integers between 0 and 9"""
        for i in range(iterations):
            value = get_random_int(0, 9)
            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 9)

    def test_generate_integers_with_range_excluding_specific_digits(self):
        """Generate integers between 0 and 9 excluding specific digits"""
        for i in range(iterations):
            for not_equal in range(10):
                value = get_random_int(0, 9, not_equal)
                self.assertIsInstance(value, int)
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, 9)
                self.assertNotEqual(value, not_equal)


if __name__ == '__main__':
    unittest.main()
