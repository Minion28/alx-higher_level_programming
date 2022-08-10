#!/usr/bin/python3
import unittest
from models.base import Base
"""Test case for base class"""


class TestBase(unittest.TestCase):
    """Tests base model"""

    def test_valid_id(self):
        """Tests for valid id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_is_valid_string(self):
        """Testing string inputs"""
        b2 = Base("ALX")
        self.assertEqual(b2.id, "ALX")

    def test_is_valid_multiple(self):
        """Tests valid multiple"""
        pass


if __name__ == '__main__':
    unittest.main()
