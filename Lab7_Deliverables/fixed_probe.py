from processor import split_code, most_expensive, expiry_days
cases=[("split_code(None)",lambda:split_code(None)),("split_code('SAVE')",lambda:split_code("SAVE")),("most_expensive('1,,2')",lambda:most_expensive("1,,2")),("most_expensive('')",lambda:most_expensive("")),("expiry_days('2024-02-30')",lambda:expiry_days("2024-02-30")),("expiry_days(None)",lambda:expiry_days(None))]
for label,call in cases:
    try: print(f"{label} -> {call()!r} [UNEXPECTED ACCEPTANCE]")
    except (TypeError,ValueError) as exc: print(f"{label} -> handled: {type(exc).__name__}")
