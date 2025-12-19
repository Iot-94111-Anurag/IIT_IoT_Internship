from arithmatic import add , multiply
from string_ops import reverse_string , count_vowels

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
string = input("Enter the string: ")

def operation():
    print(f"Addition of {num1} and {num2} = {add(num1, num2)}")
    print(f"Multiplication of {num1} and {num2} = {multiply(num1, num2)}")
    print(f"Reversed string = {reverse_string(string)}")
    print(f"Vowel count = {count_vowels(string)}")

operation()
