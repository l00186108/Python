'''
Script: test.py
By: NMC
Purpose: Functions for Tests.
Date: 12DEC23
''' 
import unittest
import formatter

class TestFormatter(unittest.TestCase):
    def test_lower(self):
        test_text = "JOHN ORAW"
        result = formatter.convert_lower(test_text)
        self.assertEqual(result, "john oraw")

    def test_upper(self):
        test_text = "John ORaw"
        result = formatter.convert_upper(test_text)
        self.assertEqual(result, "JoHN ORAW")

if __name__ =="__main__":
    unittest.main()