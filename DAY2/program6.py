num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

while True:
    print("\n1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        case 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        case 3:
            print(f"{num1} * {num2} = {num1 * num2}")
        case 4:
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Division by zero not allowed")
        case 5:
            print("Exiting program")
            break
        case _:
            print("Invalid choice")
