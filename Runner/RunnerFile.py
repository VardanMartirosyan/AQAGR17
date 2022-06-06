import unittest
from TestSuites.GeneralSuite import GenerSuite

class RunClass():
    def run(self, suite):
        runner = unittest.TextTestRunner()
        runner.run(suite)


if __name__ == "__main__":
    runner = RunClass()
    suite = GenerSuite.GenralSuiteClass()
    runner.run(suite.generate_suite())
