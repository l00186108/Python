'''
Script: test_formatter.py
By: NMC
Purpose: Functions for Tests.
Date: 12DEC23
''' 

# Import the neccessary modules.
import unittest
import formatter

# Create a test class that inherits from unittest.TestCase
class TestFormatter(unittest.TestCase):
    # Test case for the convert_lowercase function
    def test_lower(self):
        test_text = "JOHN ORAW"
        result = formatter.convert_lower(test_text)
        self.assertEqual(result, "john oraw")

    # Test case for the convert_uppercase function
    def test_upper(self):
        test_text = "John ORaw"
        result = formatter.convert_upper(test_text)
        self.assertEqual(result, "JOHN ORAW")

# Running the tests in main module.
if __name__ =="__main__":
    unittest.main()