"""Unit tests for three_five.py"""

import unittest
import doctest
import three_five


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(three_five))
    return tests


if __name__ == "main":
    unittest.main()
