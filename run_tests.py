import os
import unittest


def load_tests() -> unittest.TestSuite:
    current_dir = os.path.join(os.path.dirname(__file__), 'tests')
    loader = unittest.TestLoader()
    package_tests = loader.discover(start_dir=os.path.join(os.path.dirname(__file__), 'tests'))
    suite = unittest.TestSuite()
    suite.addTests(package_tests)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(load_tests())
