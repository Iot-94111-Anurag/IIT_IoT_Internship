num1 = int(input("Enter a five digit number: "))

temp = num1
rev = 0

while num1 > 0:
    num2 = num1 % 10
    rev = rev * 10 + num2
    num1 = num1 // 10

if temp == rev:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

 
