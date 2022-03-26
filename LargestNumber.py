import unittest

def LargestNumber(x,y,z):
    if(x>y and x>z):
        return "First"
    elif (y>x and y>z):
        return "Second"
    else:
        return "Third"

class Largestnumber(unittest.TestCase):
    def test_case1(self):
        x = 200
        y = 100
        z = 150
        result = LargestNumber(x,y,z)
        self.assertEqual("First" ,result)

    def test_case2(self):
        x = 50
        y = 200
        z = 150
        result = LargestNumber(x,y,z)
        self.assertEqual("Second", result)

    def test_case3(self):
        x = 50
        y = 100
        z = 250
        result = LargestNumber(x,y,z)
        self.assertEqual("Third", result)
if __name__=="__main__":
    unittest.main()

