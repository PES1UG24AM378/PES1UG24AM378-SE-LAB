# Lab 6 — Code and Branch Coverage Deliverables

Assigned exercise: Coupon Validator (SRN: PES1UG24AM378).

## Contents

- `coupon_validator.py` — original application under test.
- `CodeCoverageTest_coupon_validator.py` — code coverage test suite.
- `BranchCoverageTest_coupon_validator.py` — branch coverage test suite.
- `CodeCoverage_Screenshot.png` — supplied terminal evidence: 23 tests passed, 32 statements, 0 missing, 100% coverage.
- `BranchCoverage_Screenshot.png` — supplied terminal evidence: 21 tests passed, 32 statements, 24 branches, 0 partial branches, 100% coverage.
- `RUN_INSTRUCTIONS.md` — commands to reproduce both reports.

## Run

Run commands from this folder:

```powershell
py -m pip install pytest coverage
py -m coverage erase
py -m coverage run --source=coupon_validator -m pytest -q CodeCoverageTest_coupon_validator.py
py -m coverage report -m
```

```powershell
py -m coverage erase
py -m coverage run --branch --source=coupon_validator -m pytest -q BranchCoverageTest_coupon_validator.py
py -m coverage report -m
```

The screenshots are the terminal screenshots supplied by the student. The reported results are 100% code coverage and 100% branch coverage.
