import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(3, 0), 0)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(5,2),2)
        self.assertEqual(self.calc.divide(21,3),7)
        self.assertEqual(self.calc.divide(144,12),12)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(5,2),1)
        self.assertEqual(self.calc.modulo(2,4),2)
        self.assertEqual(self.calc.modulo(14,2),0)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main(verbosity=2)