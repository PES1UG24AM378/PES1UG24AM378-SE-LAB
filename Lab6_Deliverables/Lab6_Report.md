# Lab 6 — Code and Branch Coverage Analysis

**Student:** Mohammed Shahid Javed Mokashi  
**SRN:** PES1UG24AM378  
**Course:** Software Engineering Laboratory  
**Application:** Coupon Validator

## 1. Introduction

The objective of this lab is to understand code coverage and branch coverage, use the Python coverage tool to measure test completeness, interpret coverage reports, and improve tests to exercise edge cases and decision branches.

## 2. Application overview

The Coupon Validator application contains three functions:

- `coupon_discount()`: evaluates WELCOME10, WEEKEND20, and FLAT100 coupon rules.
- `best_discount()`: selects the highest applicable discount and caps it at 40% of the cart total.
- `is_expired()`: determines whether a coupon has expired based on its validity period.

## 3. Methodology

The tests use pytest and coverage.py. Test scenarios include positive and non-positive cart totals, new and existing users, weekend and weekday coupon conditions, cart-value thresholds, unknown coupon codes, discount selection and capping, and coupon-expiry boundaries.

## 4. Results

| Metric | Code coverage suite | Branch coverage suite |
|---|---:|---:|
| Tests passed | 23 | 21 |
| Statements | 32 | 32 |
| Missing statements | 0 | 0 |
| Branches | — | 24 |
| Partial branches | — | 0 |
| Coverage | **100%** | **100%** |

Both test suites exceed the lab's minimum requirement of 90%. The branch report records 24 branches and zero partial branches.

## 5. Execution commands

### Code coverage

```powershell
py -m coverage erase
py -m coverage run --source=coupon_validator -m pytest -q CodeCoverageTest_coupon_validator.py
py -m coverage report -m
```

### Branch coverage

```powershell
py -m coverage erase
py -m coverage run --branch --source=coupon_validator -m pytest -q BranchCoverageTest_coupon_validator.py
py -m coverage report -m
```

## 6. Analysis and conclusion

Statement coverage confirms that all executable statements were run. Branch coverage additionally checks alternate decision outcomes. The supplied terminal runs show 100% for both measures, with all 24 measured branches covered and no partial branches in the branch report.

## 7. Screenshot evidence

The accompanying PDF report contains the two terminal screenshots supplied for this lab:
- Code coverage terminal output: 23 tests passed, 100% coverage.
- Branch coverage terminal output: 21 tests passed, 100% coverage.

**Evidence note:** The screenshots are embedded in the generated PDF report. This Markdown copy summarizes the results; it does not reproduce the screenshot images.
