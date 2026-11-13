"""Hypothesis fuzz tests for all three Lab 7 input-processing functions."""
from datetime import date
import math
import pytest
from hypothesis import given, settings, strategies as st
from processor import split_code, most_expensive, expiry_days

FUZZ_SETTINGS = settings(max_examples=200, deadline=None)

def _valid_coupon_result(result):
    assert isinstance(result, tuple) and len(result) == 2
    prefix, number = result
    assert isinstance(prefix, str) and prefix and prefix == prefix.upper()
    assert isinstance(number, int) and number >= 0

@FUZZ_SETTINGS
@given(st.one_of(st.text(), st.none()))
def test_split_code_arbitrary_text_is_valid_or_rejected_cleanly(value):
    try:
        result = split_code(value)
    except (TypeError, ValueError):
        return
    _valid_coupon_result(result)

@FUZZ_SETTINGS
@given(st.text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", min_size=1, max_size=12), st.integers(min_value=0, max_value=10**9))
def test_split_code_valid_generated_codes(prefix, number):
    assert split_code(f"{prefix}-{number}") == (prefix.upper(), number)

@FUZZ_SETTINGS
@given(st.one_of(st.text(), st.none()))
def test_most_expensive_arbitrary_text_is_valid_or_rejected_cleanly(value):
    try:
        result = most_expensive(value)
    except (TypeError, ValueError):
        return
    assert isinstance(result, float) and math.isfinite(result) and result >= 0

@FUZZ_SETTINGS
@given(st.lists(st.floats(min_value=0, max_value=1e9, allow_nan=False, allow_infinity=False), min_size=1, max_size=20))
def test_most_expensive_generated_price_lists(prices):
    assert most_expensive(",".join(repr(p) for p in prices)) == max(prices)

@FUZZ_SETTINGS
@given(st.one_of(st.text(), st.none()))
def test_expiry_days_arbitrary_text_is_valid_or_rejected_cleanly(value):
    try:
        result = expiry_days(value)
    except (TypeError, ValueError):
        return
    assert isinstance(result, int)

@FUZZ_SETTINGS
@given(st.dates(min_value=date(1900, 1, 1), max_value=date(2200, 12, 31)))
def test_expiry_days_generated_calendar_dates(value):
    assert expiry_days(value.isoformat()) == (value - date(2024, 1, 1)).days

def test_split_code_rejects_missing_or_extra_parts():
    for value in ("", "SAVE", "SAVE-1-2", "-10", "SAVE-", "SAVE--2"):
        with pytest.raises(ValueError): split_code(value)

def test_most_expensive_rejects_empty_non_numeric_and_non_finite_values():
    for value in ("", "1,,2", "1,word", "nan", "inf", "-1,2"):
        with pytest.raises(ValueError): most_expensive(value)

def test_expiry_days_rejects_invalid_calendar_dates():
    for value in ("2024-02-30", "2024-13-01", "24-01-01", "2024/01/01"):
        with pytest.raises(ValueError): expiry_days(value)

@pytest.mark.parametrize("function", [split_code, most_expensive, expiry_days])
def test_functions_reject_none_with_type_error(function):
    with pytest.raises(TypeError): function(None)
