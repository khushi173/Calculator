import unittest
def Check_Armstrong(num):
    sum = 0
    order = len(str(num))
    copy_num = num

    while(num > 0):
        digit = num%10
        sum += digit **order
        num = num//10

    if (sum == copy_num):
        print("The number is Armstrong")
    else:
        print("The number is Not Armstrong")

class Armstrong(unittest.TestCase):
    def test_case1(self):
        num =121
        result = Check_Armstrong(num)
        self.assertTrue(num , result)
if __name__=="__main__":
    unittest.main()