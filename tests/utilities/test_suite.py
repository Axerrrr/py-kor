import unittest
from .scope_test import *


def create_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(ScopeTestCase('Test scope'))
    suite.addTest(EScopeTestCase('Test scope'))
    return suite
