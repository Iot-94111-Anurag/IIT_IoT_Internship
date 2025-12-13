def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

print("Prime numbers are:")
for n in range(start, end + 1):
    if is_prime(n):
        print(n, end=" ")