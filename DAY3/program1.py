str1 ="ANURAG PRABHAKAR"
str2  = "MANGLEKAR"

str3 =str1.capitalize() # capitalize() = 1st letter is become capital reaminng letter are small
print(str3)
str3 =str2.capitalize()
print(str3)

print("\n")
print(str1.swapcase()) # swapcase() = it convert capital to small &&  small to capital
print(str2.swapcase())

print("\n")
print(str1.title()) # title() = 1st letter of each world is become capital
print(str2.title())

print()
num1 = "1234"
num2 = "1x23"
print(num1.isnumeric()) # isnumeric() = if sting containt only numbers then it returns true
print(num2.isnumeric()) # isnumeric() = if sting does not containt only numbers then it returns false

print()
print(str1.isupper()) # isupper() = it check string containt only upper case (true)
print(str1.isupper()) # isupper() = it check string containt only upper case (true)

print()
str3 = "ANURAG"
print(str1.islower()) # islower() = it check string containt only upper case (true)
print(str3.islower()) # islower() = it check string containt only upper case (true)

print()
str4 = "A"
str5 = "NG"
print(str1.count(str4,0,200)) #(jay chay madhe find karay cha)count((finding valu),startig point ,ending point) =  it givs how may times substring occurs inn main string
print(str2.count(str5,0))
print(str1.count(str4))

print()
print(str1.replace("U","_")) # replace() = it is used to replace the character