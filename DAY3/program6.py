
def Addition(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

def Subtraction(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")

def Multiplication(num1, num2):
    print(f"{num1} * {num2} = {num1 * num2}")

def Division(num1, num2):
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division by zero is not allowed")

def Modulus(num1, num2):
    print(f"{num1} % {num2} = {num1 % num2}")


num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))
operand = input("Enter the operand (+, -, *, /, %): ")

if operand == "+":
    Addition(num1, num2)
elif operand == "-":
    Subtraction(num1, num2)
elif operand == "*":
    Multiplication(num1, num2)
elif operand == "/":
    Division(num1, num2)
elif operand == "%":
    Modulus(num1, num2)
else:
    print("Invalid operator")
    