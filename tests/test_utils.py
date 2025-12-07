"""
Unit tests for utility functions.
"""

import unittest
from src.utils import validate_ticker, format_currency, format_percentage


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_validate_ticker_valid(self):
        """Test valid ticker symbols."""
        self.assertTrue(validate_ticker("AAPL"))
        self.assertTrue(validate_ticker("GOOGL"))
        self.assertTrue(validate_ticker("BTC-USD"))
        self.assertTrue(validate_ticker("ETH-USD"))
    
    def test_validate_ticker_invalid(self):
        """Test invalid ticker symbols."""
        self.assertFalse(validate_ticker(""))
        self.assertFalse(validate_ticker("   "))
        self.assertFalse(validate_ticker("A" * 25))  # Too long
        self.assertFalse(validate_ticker("AAPL@"))
        self.assertFalse(validate_ticker("AAPL#"))
    
    def test_format_currency(self):
        """Test currency formatting."""
        self.assertEqual(format_currency(1234.56), "$1,234.56")
        self.assertEqual(format_currency(1000000), "$1,000,000.00")
        self.assertEqual(format_currency(None), "N/A")
    
    def test_format_percentage(self):
        """Test percentage formatting."""
        self.assertEqual(format_percentage(0.05), "5.00%")
        self.assertEqual(format_percentage(0.1234), "12.34%")
        self.assertEqual(format_percentage(None), "N/A")


if __name__ == "__main__":
    unittest.main()

