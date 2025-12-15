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
  

while True:
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))
    

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    

    choice = int(input("Enter Your Choice: "))

    match choice:
        case 1:
            Addition(num1, num2)
        case 2:
            Subtraction(num1, num2)
        case 3:
            Multiplication(num1, num2)
        case 4:
            Division(num1, num2)
        case 5:
            Modulus(num1, num2)
        case _:
            print("Invalid Choice")
