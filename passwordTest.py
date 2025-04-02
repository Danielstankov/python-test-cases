import unittest
from password import password_checker


class TestPassword(unittest.TestCase):
    def test_for_length(self):
        self.assertFalse(password_checker("Pass123"))

    def test_for_no_upper(self):
        self.assertFalse(password_checker("password@12345"))

    def test_for_no_numbers(self):
        self.assertFalse(password_checker("PasswordPassword"))

    def test_for_no_letters(self):
        self.assertFalse(password_checker("123456789"))

    def test_for_valid(self):
        self.assertTrue(password_checker("Password@12345"))


if __name__ == '__main__':
    unittest.main()
