"""Test Generation"""

# run test
# python3 .\test\test_generation.py -v
# or
# python3 -m unittest discover -s './test' -v
# run main
# python3 -m lytrax_afm

import package_resolve
import unittest
import re

from lytrax_afm import validate_afm, \
    generate_afm, \
    generate_valid_afm, \
    generate_invalid_afm
from helpers import *


class TestRandomInteger(unittest.TestCase):
    def test_default(self):
        """(default)"""
        for i in range(iterations):
            value = generate_afm()
            valid = validate_afm(value)
            self.assertTrue(valid)

            value_valid = generate_valid_afm()
            valid_valid = validate_afm(value_valid)
            self.assertTrue(valid_valid)

            value_invalid = generate_invalid_afm()
            invalid_invalid = validate_afm(value_invalid)
            self.assertFalse(invalid_invalid)
    
    def test_force_first_digit(self):
        """force_first_digit"""
        for i in range(iterations):
            for force_first_digit in range(10):
                value = generate_afm(force_first_digit=force_first_digit)
                valid = validate_afm(value)
                first_digit = int(value[0])
                self.assertTrue(valid)
                self.assertEqual(force_first_digit, first_digit)

                value_valid = generate_valid_afm(force_first_digit=force_first_digit)
                valid_valid = validate_afm(value_valid)
                first_digit_valid = int(value_valid[0])
                self.assertTrue(valid_valid)
                self.assertEqual(force_first_digit, first_digit_valid)

                value_invalid = generate_invalid_afm(force_first_digit=force_first_digit)
                invalid_invalid = validate_afm(value_invalid)
                first_digit_invalid = int(value_invalid[0])
                self.assertFalse(invalid_invalid)
                self.assertEqual(force_first_digit, first_digit_invalid)

    def test_pre99(self):
        """pre99"""
        for i in range(iterations):
            value = generate_afm(pre99=True)
            valid = validate_afm(value)
            first_digit = int(value[0])
            self.assertTrue(valid)
            self.assertEqual(first_digit, 0)

            value_valid = generate_valid_afm(pre99=True)
            valid_valid = validate_afm(value_valid)
            first_digit_valid = int(value_valid[0])
            self.assertTrue(valid_valid)
            self.assertEqual(first_digit_valid, 0)

            value_invalid = generate_invalid_afm(pre99=True)
            invalid_invalid = validate_afm(value_invalid)
            first_digit_invalid = int(value_invalid[0])
            self.assertFalse(invalid_invalid)
            self.assertEqual(first_digit_invalid, 0)

    def test_individual(self):
        """individual"""
        re_test = r"^[1-4]{1}$"
        for i in range(iterations):
            value = generate_afm(individual=True)
            valid = validate_afm(value)
            first_digit = value[0]
            self.assertTrue(valid)
            self.assertRegex(first_digit, re_test)

            value_valid = generate_valid_afm(individual=True)
            valid_valid = validate_afm(value_valid)
            first_digit_valid = value_valid[0]
            self.assertTrue(valid_valid)
            self.assertRegex(first_digit_valid, re_test)

            value_invalid = generate_invalid_afm(individual=True)
            invalid_invalid = validate_afm(value_invalid)
            first_digit_invalid = value_invalid[0]
            self.assertFalse(invalid_invalid)
            self.assertRegex(first_digit_invalid, re_test)

    def test_legal_entity(self):
        """legal_entity"""
        re_test = r"^[7-9]{1}$"
        for i in range(iterations):
            value = generate_afm(legal_entity=True)
            valid = validate_afm(value)
            first_digit = value[0]
            self.assertTrue(valid)
            self.assertRegex(first_digit, re_test)

            value_valid = generate_valid_afm(legal_entity=True)
            valid_valid = validate_afm(value_valid)
            first_digit_valid = value_valid[0]
            self.assertTrue(valid_valid)
            self.assertRegex(first_digit_valid, re_test)

            value_invalid = generate_invalid_afm(legal_entity=True)
            invalid_invalid = validate_afm(value_invalid)
            first_digit_invalid = value_invalid[0]
            self.assertFalse(invalid_invalid)
            self.assertRegex(first_digit_invalid, re_test)

    def test_repeat_tolerance(self):
        """repeat_tolerance"""
        re_test = r"(.)\1+"
        for i in range(iterations):
            for repeat_tolerance in range(4):
                value = generate_afm(repeat_tolerance=repeat_tolerance)
                valid = validate_afm(value)
                body = value[:8]
                self.assertTrue(valid)
                
                if(repeat_tolerance == 0):
                    repeats = re.findall(re_test, body)
                    self.assertEqual(len(repeats), 0)
                else:
                    repeats = re.finditer(re_test, body)
                    for repeat in repeats:
                        repeated_digits = repeat.group()
                        self.assertLessEqual(len(repeated_digits), repeat_tolerance + 1)

                value_valid = generate_valid_afm(repeat_tolerance=repeat_tolerance)
                valid_valid = validate_afm(value_valid)
                body_valid = value_valid[:8]
                self.assertTrue(valid_valid)

                if(repeat_tolerance == 0):
                    repeats = re.findall(re_test, body_valid)
                    self.assertEqual(len(repeats), 0)
                else:
                    repeats = re.finditer(re_test, body_valid)
                    for repeat in repeats:
                        repeated_digits = repeat.group()
                        self.assertLessEqual(len(repeated_digits), repeat_tolerance + 1)

                value_invalid = generate_invalid_afm(repeat_tolerance=repeat_tolerance)
                invalid_invalid = validate_afm(value_invalid)
                body_invalid = value_invalid[:8]
                self.assertFalse(invalid_invalid)

                if(repeat_tolerance == 0):
                    repeats = re.findall(re_test, body_invalid)
                    self.assertEqual(len(repeats), 0)
                else:
                    repeats = re.finditer(re_test, body_invalid)
                    for repeat in repeats:
                        repeated_digits = repeat.group()
                        self.assertLessEqual(len(repeated_digits), repeat_tolerance + 1)

if __name__ == '__main__':
    unittest.main()
