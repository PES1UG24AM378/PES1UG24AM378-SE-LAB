# Lab 7 — Fuzzing for Input Validation Bugs

**Student:** Mohammed Shahid Javed Mokashi  
**SRN:** PES1UG24AM378  
**Course:** Software Engineering Laboratory

## Objective
Use fuzz testing to discover and fix input-validation bugs in the assigned Python functions with Hypothesis.

## Functions covered
- `split_code()`: parse PREFIX-NUMBER coupon codes.
- `most_expensive()`: find the maximum in comma-separated prices.
- `expiry_days()`: validate YYYY-MM-DD and calculate calendar-day offset from 2024-01-01.

## Bugs found in the starter
The original code can leak AttributeError for None, ValueError for malformed price lists, and incorrectly accepts impossible dates such as 2024-02-30. Its date formula assumes every month has 30 days and ignores leap years.

## Fixes
The updated code validates types and formats, rejects empty/malformed values, disallows non-finite or negative prices, validates real calendar dates, and uses datetime date arithmetic. Invalid types raise TypeError; invalid values raise ValueError.

## Hypothesis suite
The test suite uses arbitrary strings and None, generated valid coupon codes, generated numeric price lists, and generated calendar dates. It checks both clean rejection of invalid input and invariants for valid input.

## Evidence
Four actual local command-output captures are included under `evidence/`: original app, original malformed-input probe, fixed app, and fixed malformed-input probe. These are deterministic execution captures, not Hypothesis test-run screenshots.

**Important execution status:** Hypothesis was unavailable in the build environment and package installation could not reach the package index. Therefore, the Hypothesis suite has been authored but not executed here. Install dependencies with `py -m pip install -r requirements.txt`, then run `py -m pytest -v test_processor.py` and capture the required failing-before/passing-after Hypothesis terminal screenshots in your lab environment.
