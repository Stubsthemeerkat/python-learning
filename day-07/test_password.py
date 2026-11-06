import unittest

from main import (
    check_length,
    check_uppercase,
    check_digit,
    check_lower,
    check_punctuation,
)

class TestPassword(unittest.TestCase):

    def test_valid_length(self):
        result = check_length("1234567890123451")
        self.assertTrue(result)

    def test_invalid_15(self):
        result = check_length("123456789012345")
        self.assertFalse(result)

    def test_valid_17(self):
        result = check_length("12345678901234517")
        self.assertTrue(result)

    def test_invalid_length(self):
        result = check_length("Invalid")
        self.assertFalse(result)

    def test_uppercase(self):
        result = check_uppercase("ValidPass123")
        self.assertTrue(result)

    def test_no_uppercase(self):
        result = check_uppercase("invalidpass123")
        self.assertFalse(result)

    def test_valid_digit(self):
        result = check_digit("ValidPass123")
        self.assertTrue(result)

    def test_no_digit(self):
        result = check_digit("ValidPass")
        self.assertFalse(result)

    def test_valid_lower(self):
        result = check_lower("ValidPass123")
        self.assertTrue(result)

    def test_no_lower(self):
        result = check_lower("VALIDPASS123")
        self.assertFalse(result)

    def test_valid_punctuation(self):
        result = check_punctuation("ValidPass123!")
        self.assertTrue(result)

    def test_no_punctuation(self):
        result = check_punctuation("ValidPass123")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()