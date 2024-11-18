import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test(self):
        self.assertEqual(self.calc.add(1, -2), -1)
        self.assertEqual(self.calc.add(-1, -2), -3)

        self.assertEqual(self.calc.subtract(1, -2), 3)
        self.assertEqual(self.calc.subtract(-1, -2), 1)

        self.assertEqual(self.calc.multiply(-1, -2), 2)
        self.assertEqual(self.calc.multiply(2, -3), -6)

        self.assertEqual(self.calc.divide(1, -2), 0)
        self.assertEqual(self.calc.divide(-10, -8), 1)

        self.assertEqual(self.calc.modulo(1, 2), 1)
        self.assertEqual(self.calc.modulo(8, 2), 0)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()