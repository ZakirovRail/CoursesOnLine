This is a notes for the book

The headquarters for pytest is https://docs.pytest.org.

** How to install pytest on venv:
1. $ pip3 install -U virtualenv
2. $ python3 -m virtualenv venv 
3. $ source venv/bin/activate
4. $ pip install pytest


Running pytest:
$pytest --help

Run specific files with tests (if you in the directory with tests):
$ pytest test_three.py test_four.py

Only collect tests:
$ pytest --collect-only

Run tests marked with 'smoke' mark in verbose mode (means with details)
$ pytest -v -m 'smoke' 

Run tests and show extra test summary info for skipped tests, if there are (in tests) mentioned reasons why it's
skipping (using the 'skipif')
$ pytest -rs test_unique_id_3.py

To run a single test function, add :: and the test function name:
$ pytest -v tests/func/test_add.py::test_add_returns_valid_id

To run tests only for a specific Test Class:
$ pytest -v tests/func/test_api_exceptions.py::TestUpdate

To run ONE test only from a specific Test Class:
$ pytest -v tests/func/test_api_exceptions.py::TestUpdate::test_bad_id


To run tests that have certain names specified by the expression as a substring of the test name
$ pytest -v -k _raises

To run tests that have certain names specified by the expression as a substring of the test name and exclude som other tests
$ pytest -v -k "_raises and not delete"



====================================

Tests naming convention:

Here’s a brief overview of the naming conventions to keep your test code discoverable by pytest:
1. Test files should be named test_<something>.py or <something>_test.py. 
2. Test methods and functions should be named test_<something>. 
3. Test classes should be named Test<Something>.

====================================
You can configure pytest to report the tests that pass but were marked with xfail to be reported as FAIL. 
This is done in a pytest.ini file:
[pytest]
xfail_strict=true
====================================





