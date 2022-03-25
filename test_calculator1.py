import Calculator
import unittest
class TestCalculator1(unittest.TestCase):

    def setUp(self):
        self.x=34
        self.y=30
    def tearDown(self):
        self.x = 0
        self.y = 0
    def test_add1(self):
        #ACT
        result = Calculator.add(self.x,self.y)
        #assert
        self.assertEqual(result,self.x+self.y)

    def test_sub1(self):
        result = Calculator.sub(self.x,self.y)
        self.assertEqual(result,self.x-self.y)
    def test_mul1(self):
        result = Calculator.mul(self.x,self.y)
        self.assertEqual(result,self.x*self.y)
    def test_div1(self):
        result = Calculator.div(self.x,self.y)
        self.assertEqual(result,self.x/self.y)


if __name__=="__main__":
    unittest.main()