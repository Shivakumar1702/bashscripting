import sys

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

a = float(sys.argv[1])
b = sys.argv[2]
c = float(sys.argv[3])

if b == "addition":
    print(addition(a,c))
elif b == "subtraction":
    print(subtraction(a,c))
elif c == "multiply":
    print(multiply(a,c))
else:
    print("wrong selection")