# Lab 6 — Run Instructions

Open PowerShell in this directory.

Install dependencies:

```powershell
py -m pip install pytest coverage
```

## Code coverage

```powershell
py -m coverage erase
py -m coverage run --source=coupon_validator -m pytest -q CodeCoverageTest_coupon_validator.py
py -m coverage report -m
```

Expected evidence shown in the submitted screenshot: 23 passed; 32 statements; 0 missing; 100%.

## Branch coverage

```powershell
py -m coverage erase
py -m coverage run --branch --source=coupon_validator -m pytest -q BranchCoverageTest_coupon_validator.py
py -m coverage report -m
```

Expected evidence shown in the submitted screenshot: 21 passed; 32 statements; 24 branches; 0 partial branches; 100%.
