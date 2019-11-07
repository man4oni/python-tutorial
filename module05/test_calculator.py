import unittest
from unittest.mock import patch
from unittest import mock
from calculator import *
from selenium import webdriver
d=webdriver.chrome



class CalculatorTestCase(unittest.TestCase):
    def test_add(self):

        result=add(2,2)
        self.assertEqual(add(2, 2), 4)
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, 4)
        self.assertEqual(add(3, 2), 5)

    def test_subtract(self):
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(5, 2.5), 2.5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 3), 9)
        self.assertEqual(multiply(1.5, 6), 9.0)
        self.assertEqual(multiply(2, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(3, 3), 1)
        self.assertEqual(divide(3.0, 2), 1.5)
        self.assertEqual(divide(6, 2), 3)



    def test_action(self):
        pass


















if __name__ == "__main__":
    unittest.main()