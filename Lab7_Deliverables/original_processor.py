"""Unmodified buggy starter implementation retained for comparison."""
def split_code(code):
    prefix, value = code.strip().upper().split('-')
    return prefix, int(value)
def most_expensive(prices_csv):
    prices = [float(p) for p in prices_csv.split(',')]
    return max(prices)
def expiry_days(date_text):
    year, month, day = [int(p) for p in date_text.split('-')]
    return (year - 2024) * 365 + (month - 1) * 30 + day
def main():
    print("==== Running split_code ====")
    result = split_code(input("Enter a coupon code (e.g. save-20): "))
    print("Prefix and Value:", result)
    print("\n==== Running most_expensive ====")
    result = most_expensive(input("Enter item prices as CSV (e.g. 199,49.5,320): "))
    print("Most Expensive Item:", result)
    print("\n==== Running expiry_days ====")
    result = expiry_days(input("Enter an expiry date as YYYY-MM-DD: "))
    print("Days Since 2024:", result)
if __name__ == "__main__": main()
