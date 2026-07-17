from time_converter import validate_time, convert_to_utc, convert_from_utc, format_time
import pytest

# Time Validation Tests
def test_validate_time_valid():
    """Test the times that should be accepted"""
    assert validate_time("10:30") == (10, 30)
    assert validate_time("00:00") == (0, 0)
    assert validate_time("23:59") == (23, 59)

def test_validate_time_invalid():
    """Tests for prohibited formats and values"""
    assert validate_time("24:00") is None
    assert validate_time("12:60") is None
    assert validate_time("cat") is None
    assert validate_time("9:30") == (9, 30) # If it accepts the zero without it, it returns the tuple.

# Tests for Conversion (Modular Arithmetic)
def test_convert_to_utc():
    """Test the return to ground zero (UTC)"""
    # Brasilia (-3): 10:00 local -> 13:00 UTC (10 - (-3))
    assert convert_to_utc(10, 0, "brasília") == (13, 0)
    # Tokyo (+9): 05:00 local -> 20:00 UTC the previous day ((5 - 9) % 24)
    assert convert_to_utc(5, 0, "tokyo") == (20, 0)

def test_convert_from_utc():
    """Test the UTC's journey to the destination city"""
    # From 13:00 UTC to New York (-5) -> 08:00
    assert convert_from_utc(13, 0, "new york") == (8, 0)
    # From 22:00 UTC to Dubai (+4) -> 02:00 the following day ((22 + 4) % 24)
    assert convert_from_utc(22, 0, "dubai") == (2, 0)

# Tests for Output Formatting
def test_format_time():
    """Ensures that the output string always has two digits"""
    assert format_time(8, 5) == "08:05"
    assert format_time(14, 30) == "14:30"
    assert format_time(0, 0) == "00:00"
