import Calculator
import unittest
class TestCalculator(unittest.TestCase):
    def test_add(self):
        #ARRANGE
        x = 10
        y = 20
        #ACT
        result = Calculator.add(x,y)
        #assert
        self.assertEqual(result,x+y)

    def test_sub(self):
        x = 20
        y = 10
        result = Calculator.sub(x,y)
        self.assertEqual(result,x-y)
    def test_mul(self):
        x = 10
        y = 20
        result = Calculator.mul(x,y)
        self.assertEqual(result,x*y)
    def test_div(self):
        x = 100
        y = 20
        result = Calculator.div(x,y)
        self.assertEqual(result,x/y)


if __name__=="__main__":
    unittest.main()