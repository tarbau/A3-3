"""
Utility functions for the financial analyzer application.
"""

import logging
from typing import Optional
from datetime import datetime


def setup_logging(level: int = logging.INFO) -> None:
    """
    Set up logging configuration for the application.
    
    Args:
        level: Logging level (default: INFO)
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def validate_ticker(ticker: str) -> bool:
    """
    Validate ticker symbol format.
    
    Args:
        ticker: Ticker symbol to validate
        
    Returns:
        True if ticker appears valid, False otherwise
    """
    if not ticker or not isinstance(ticker, str):
        return False
    
    # Basic validation: should be alphanumeric with possible hyphens
    ticker_clean = ticker.strip().upper()
    if len(ticker_clean) < 1 or len(ticker_clean) > 20:
        return False
    
    # Allow alphanumeric and hyphens (for crypto like BTC-USD)
    return all(c.isalnum() or c == "-" for c in ticker_clean)


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





