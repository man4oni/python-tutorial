import unittest

import calculator

class CalculatorTestCase(unittest.TestCase):

    def test_add(self):

        result=calculator.add(2,2)
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, 4)
        self.assertEqual(calculator.add(3, 2), 5)
        self.assertRaises(TypeError,calculator.add('six','ten'))

    def test_subtract(self):
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.subtract(2, 1), 1)
        self.assertEqual(calculator.subtract(5, 2.5), 2.5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 3), 9)
        self.assertEqual(calculator.multiply(1.5, 6), 9.0)
        self.assertEqual(calculator.multiply(2, 0), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(3, 3), 1)
        self.assertEqual(calculator.divide(3.0, 2), 1.5)
        self.assertEqual(calculator.divide(6, 2), 3)
        with self.assertRaises( ZeroDivisionError):
            calculator.divide(3, 0)



if __name__ == "__main__":
    unittest.main()