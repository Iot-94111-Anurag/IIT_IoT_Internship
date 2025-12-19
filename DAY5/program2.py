import calculator



num1 = int(input("Enter The First Number:"))
num2 = int(input("Enter The Second Number:"))

def function1(): 
    print(f"sum of{num1 ,num2} = {calculator.add(num1,num2)}")

print(f"subtraction of{num1 ,num2} = {calculator.subtract(num1,num2)}")

print(f"multiplication of{num1 ,num2} = {calculator.multiply(num1,num2)}")

print(f"division of{num1 ,num2} = {calculator.divide(num1,num2)}")

print(f"modulus of{num1 ,num2} = {calculator.mod(num1,num2)}")

 
function1()
