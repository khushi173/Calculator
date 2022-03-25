
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
if __name__=="__main__":
    num1 = int(input("ENTER FIRST NUMBER: "))
    num2 = int(input("ENTER SECOND NUMBER: "))
    print(add(num1,num2))
    print(sub(num1,num2))
    print(mul(num1,num2))
    print(div(num1,num2))