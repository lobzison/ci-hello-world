"""
Tests for the basic function
"""

import unittest
from context import ci_hello_world


class myTestSuite(unittest.TestCase):
    """
    Simple test case
    """

    def test_1(self):
        """sqrt(0) = None"""
        self.assertEqual(ci_hello_world.my_very_smart_func(0), None)

    def test_2(self):
        """sqrt(1) == 1"""
        self.assertEqual(ci_hello_world.my_very_smart_func(1), 1)

    def test_3(self):
        """sqrt(25) == 5"""
        self.assertEqual(ci_hello_world.my_very_smart_func(25), 5)


if __name__ == '__main__':
    unittest.main()
