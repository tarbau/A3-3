"""
Utility functions for the financial analyzer application.
This file only uses basic Python features, similar to
what is shown in the book "Python for Everybody".
"""

import logging


def setup_logging(level=logging.INFO):
    """
    Set up logging configuration for the application.
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def validate_ticker(ticker):
    """
    Check if a ticker has sensible format such as AAPL, GOOGL, BTC-USD, ETH-USD, etc.
    
    Returns True if it looks ok, False if not.
    """
    # If nothing was given, it's not valid
    if not ticker:
        return False



    # If it's now empty, it's not valid
    if len(ticker)==0:
        return False

    # Go through each character
    for ch in ticker:
        # If the character is not a letter, not a number, and not '-'
        if not ch.isalnum() and ch != "-":
            return False

    # If we reach here, everything was okay
    return True


def format_currency(value: float, currency: str = "USD") -> str:
    """
    Format a number as currency.
    
    Args:
        value: Numeric value to format
        currency: Currency symbol (default: USD)
        
    Returns:
        Formatted currency string
    """
    if value is None:
        return "N/A"
    
    if currency == "USD":
        return f"${value:,.2f}"
    return f"{value:,.2f} {currency}"


def format_percentage(value: float, decimals: int = 2) -> str:
    """
    Format a number as percentage.
    
    Args:
        value: Numeric value to format (e.g., 0.05 for 5%)
        decimals: Number of decimal places
        
    Returns:
        Formatted percentage string
    """
    if value is None:
        return "N/A"
    
    return f"{value * 100:.{decimals}f}%"


def format_number(value: float, decimals: int = 2) -> str:
    """
    Format a number with commas and specified decimals.
    
    Args:
        value: Numeric value to format
        decimals: Number of decimal places
        
    Returns:
        Formatted number string
    """
    if value is None:
        return "N/A"
    
    return f"{value:,.{decimals}f}"





