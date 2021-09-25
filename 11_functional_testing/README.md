# Functional testing

> The goal of **Functional testing** (also called end-to-end testing or integration testing) is to test whether a complete program meets its requirements.

When doing functional testing we need to set up a separate repository for our testing code. Our automation suite will consist of the code needed to execute certain actions (that mimic user actions) and ascertain that the result produced by the program is the specified one by the functional requirements.

The structure of a functional testing project should be as follows:

``` txt
root-directory
  |
  |_ tests
  |   |_ test_*.py
  |
  |_ pytest.ini
  |
  |_ other_files
```
