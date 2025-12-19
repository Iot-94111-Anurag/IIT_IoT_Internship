def reverse_string(string):
    rev = ""
    for i in range(len(string) - 1, -1, -1):
        rev += string[i]
    return rev

def count_vowels(string):
    count = 0
    for ch in string:
        if ch in "aeiouAEIOU":
            count += 1
    return count


