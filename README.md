# Lab 6: Code and Branch Coverage Analysis

Name: Aman Priyansh
SRN: PES1UG24AM030
Section: A
Application: Vending Machine (L6_L7_30)

All Lab 6 files are inside the [lab6](lab6) folder.

| Deliverable | File |
|---|---|
| Code coverage test file | [lab6/CodeCoverageTest_AM030_application.py](lab6/CodeCoverageTest_AM030_application.py) |
| Code coverage screenshot (100% line coverage) | [lab6/code_coverage_screenshot.png](lab6/code_coverage_screenshot.png) |
| Branch coverage test file | [lab6/BranchCoverageTest_AM030_application.py](lab6/BranchCoverageTest_AM030_application.py) |
| Branch coverage screenshot (100% branch coverage) | [lab6/branch_coverage_screenshot.png](lab6/branch_coverage_screenshot.png) |
| Analysis report (code and branch coverage) | [lab6/Lab6_Coverage_Report_AM030.pdf](lab6/Lab6_Coverage_Report_AM030.pdf) |
| Application under test (unchanged) | [lab6/vending_machine.py](lab6/vending_machine.py) |

How to run (from inside the lab6 folder):

```
coverage run -m pytest CodeCoverageTest_AM030_application.py
coverage report -m

coverage run --branch -m pytest BranchCoverageTest_AM030_application.py
coverage report -m
```
