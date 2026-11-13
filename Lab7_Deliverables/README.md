# Lab 7 — Fuzzing for Input Validation Bugs

**Student:** Mohammed Shahid Javed Mokashi  
**SRN:** PES1UG24AM378  
**Course:** Software Engineering Laboratory

## Files
- `processor.py` — hardened implementation of the three assigned functions.
- `test_processor.py` — Hypothesis property-based tests and focused validation tests.
- `original_processor.py` — original buggy implementation retained for comparison.
- `baseline_probe.py` / `fixed_probe.py` — reproducible malformed-input probes.
- `Lab7_FuzzTesting_Report.md` — report summary and evidence status.
- `Lab7_FuzzTesting_Report.pdf` — formatted report supplied separately in chat.

## Run
```powershell
py -m pip install -r requirements.txt
py processor.py
py -m pytest -v test_processor.py
```

## Input contracts
- `split_code`: PREFIX-NUMBER, non-empty alphanumeric prefix, non-negative integer suffix.
- `most_expensive`: non-empty CSV of finite, non-negative prices.
- `expiry_days`: real date in strict YYYY-MM-DD format; computes calendar-day offset from 2024-01-01.

Invalid types raise TypeError; malformed values raise ValueError.

## Verification note
The build environment had no Hypothesis package and could not reach the package index. The Hypothesis test suite is authored but its execution remains pending on the student's machine. The report does not claim unrun Hypothesis results.
