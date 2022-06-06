import unittest
from TestCases import GoogleNotSimpleTestCase
from TestCases import GoogleSimpleTestCase


class GenralSuiteClass(unittest.TestSuite):
    def generate_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(GoogleNotSimpleTestCase.GoogleTest('test_not_mygoogletest'))
        suite.addTest(GoogleNotSimpleTestCase.GoogleTest('test_not_mygoogletest'))
        suite.addTest(GoogleSimpleTestCase.GoogleTest('test_mygoogletest'))
        suite.addTest(GoogleSimpleTestCase.GoogleTest('test_mygoogletest_2'))
        return suite

if __name__ == "__main__":
    suiteObj = GenralSuiteClass()
    runner = unittest.TextTestRunner()
    runner.run(suiteObj.generate_suite())
