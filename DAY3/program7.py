def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

def power(num2,num3):
    if num3 ==0 :
        return 1
    else:
        return num2 * power(num2 , num3-1)


num = int(input("enter the number:"))
num1 = int(input("enter the power of number:"))
print("factorial:",factorial(num))
print("power of number:",power(num,num1))