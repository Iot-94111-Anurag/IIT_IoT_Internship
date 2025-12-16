def overlapping(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

if overlapping(list1, list2):
    print("True")
else:
    print("False")
