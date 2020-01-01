"""Test Validation"""

# run test
# python3 .\test\test_validation_with_extended_result.py -v
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
        expected = { 'valid': True }
        for afm in static_valid_numbers:
            result = validate_afm(afm, extended_result=True)
            self.assertIsInstance(result, dict)
            self.assertDictEqual(result, expected)
    
    def test_invalidate_invalid_afm_numbers(self):
        """Invalidate invalid AFM numbers"""
        expected = { 'valid': False, 'error': 'invalid' }
        for afm in static_invalid_numbers:
            result = validate_afm(afm, extended_result=True)
            self.assertIsInstance(result, dict)
            self.assertDictEqual(result, expected)

    def test_invalidate_length_error(self):
        """Invalidate 'length' error"""
        afm = invalid_errors['length']
        expected = { 'valid': False, 'error': 'length' }
        result = validate_afm(afm, extended_result=True)
        self.assertIsInstance(result, dict)
        self.assertDictEqual(result, expected)

    def test_invalidate_nan_error(self):
        """Invalidate 'nan' error"""
        afm = invalid_errors['nan']
        expected = { 'valid': False, 'error': 'nan' }
        result = validate_afm(afm, extended_result=True)
        self.assertIsInstance(result, dict)
        self.assertDictEqual(result, expected)

    def test_invalidate_zero_error(self):
        """Invalidate 'zero' error"""
        afm = invalid_errors['zero']
        expected = { 'valid': False, 'error': 'zero' }
        result = validate_afm(afm, extended_result=True)
        self.assertIsInstance(result, dict)
        self.assertDictEqual(result, expected)

    def test_invalidate_invalid_error(self):
        """Invalidate 'invalid' error"""
        afm = invalid_errors['invalid']
        expected = { 'valid': False, 'error': 'invalid' }
        result = validate_afm(afm, extended_result=True)
        self.assertIsInstance(result, dict)
        self.assertDictEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
