import unittest
def checkDivisibilityby5(x):
    if x % 5 == 0:
        return True
    else:
        return False

class CheckDivisible(unittest.TestCase):
    def test_case1(self):
        x = 100
        result = checkDivisibilityby5(x)
        self.assertTrue(result)

    def test_case2(self):
        x = 22
        result = checkDivisibilityby5(x)
        self.assertFalse(result)

if __name__=="__main__":
    unittest.main()