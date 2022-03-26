import unittest
def check(x):
    if x % 2 == 0:
        return "The number is Even"
    else:
        return "The number is Odd"

class EvenOdd(unittest.TestCase):
    def test_case_even_check(self):
        x = 200
        result = check(x)
        self.assertEqual('The number is Even', result)

    def test_case_odd_check(self):
        x = 91
        result = check(x)
        self.assertEqual('The number is Odd', result)

if __name__=="__main__":
    unittest.main()