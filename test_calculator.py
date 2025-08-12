import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        
    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)
        
    def test_multiply(self):
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)
        
    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
        
    # Missing test for division by zero - this is intentional
    
    def test_power(self):
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
        
    def test_history(self):
        self.calc.add(1, 1)
        history = self.calc.get_history()
        self.assertTrue(len(history) > 0)

if __name__ == '__main__':
    unittest.main()
