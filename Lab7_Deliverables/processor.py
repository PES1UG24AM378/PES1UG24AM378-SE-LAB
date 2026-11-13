"""Hardened input-processing functions for Lab 7 fuzz testing."""
from datetime import date
import math
import re

def split_code(code):
    """Return (uppercase prefix, integer value) for PREFIX-NUMBER codes."""
    if not isinstance(code, str):
        raise TypeError("coupon code must be a string")
    match = re.fullmatch(r"([A-Za-z0-9]+)-([0-9]+)", code.strip())
    if match is None:
        raise ValueError("coupon code must have the form PREFIX-NUMBER")
    return match.group(1).upper(), int(match.group(2))

def most_expensive(prices_csv):
    """Return the largest finite, non-negative price in comma-separated input."""
    if not isinstance(prices_csv, str):
        raise TypeError("prices must be supplied as a CSV string")
    parts = prices_csv.split(",")
    if not parts or any(not part.strip() for part in parts):
        raise ValueError("provide one or more comma-separated prices")
    prices = []
    for part in parts:
        try:
            price = float(part.strip())
        except ValueError as exc:
            raise ValueError(f"invalid price: {part!r}") from exc
        if not math.isfinite(price) or price < 0:
            raise ValueError("prices must be finite and non-negative")
        prices.append(price)
    return max(prices)

def expiry_days(date_text):
    """Return calendar days from 2024-01-01 to a strict YYYY-MM-DD date."""
    if not isinstance(date_text, str):
        raise TypeError("date must be a string in YYYY-MM-DD format")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_text) is None:
        raise ValueError("date must use the YYYY-MM-DD format")
    try:
        parsed = date.fromisoformat(date_text)
    except ValueError as exc:
        raise ValueError("date is not a valid calendar date") from exc
    return (parsed - date(2024, 1, 1)).days

def main():
    print("==== Running split_code ====")
    try:
        print("Prefix and Value:", split_code(input("Enter a coupon code (e.g. save-20): ")))
    except (TypeError, ValueError) as exc:
        print("Invalid coupon code:", exc)
    print("\n==== Running most_expensive ====")
    try:
        print("Most Expensive Item:", most_expensive(input("Enter item prices as CSV (e.g. 199,49.5,320): ")))
    except (TypeError, ValueError) as exc:
        print("Invalid prices:", exc)
    print("\n==== Running expiry_days ====")
    try:
        print("Days Since 2024-01-01:", expiry_days(input("Enter an expiry date as YYYY-MM-DD: ")))
    except (TypeError, ValueError) as exc:
        print("Invalid date:", exc)

if __name__ == "__main__":
    main()
