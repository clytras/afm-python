"""Test Validation"""

# run test
# python3 .\test\test_validation.py -v
# or
# python3 -m unittest discover -s './test' -v
# run main
# python3 -m lytrax_afm

import package_resolve
import unittest

from lytrax_afm import validate_afm
from helpers import *


class TestRandomInteger(unittest.TestCase):
    def test_validate_valid_afm_numbers(self):
        """Validate valid AFM numbers"""
        for i in range(iterations):
            for afm in static_valid_numbers:
                result = validate_afm(afm)
                self.assertTrue(result)
    
    def test_invalidate_invalid_afm_numbers(self):
        """Invalidate invalid AFM numbers"""
        for i in range(iterations):
            for afm in static_invalid_numbers:
                result = validate_afm(afm)
                self.assertFalse(result)

    def test_invalidate_length_error(self):
        """Invalidate 'length' error"""
        afm = invalid_errors['length']
        result = validate_afm(afm)
        self.assertFalse(result)

    def test_invalidate_nan_error(self):
        """Invalidate 'nan' error"""
        afm = invalid_errors['nan']
        result = validate_afm(afm)
        self.assertFalse(result)

    def test_invalidate_zero_error(self):
        """Invalidate 'zero' error"""
        afm = invalid_errors['zero']
        result = validate_afm(afm)
        self.assertFalse(result)

    def test_invalidate_invalid_error(self):
        """Invalidate 'invalid' error"""
        afm = invalid_errors['invalid']
        result = validate_afm(afm)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
