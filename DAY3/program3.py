def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in 'aeiou':
            count += 1
    return count


def count_consonants(s):
    count = 0
    for ch in s.lower():
        if ch.isalpha() and ch not in 'aeiou':
            count += 1
    return count


def vowel_consonant_ratio(s):
    vowels = count_vowels(s)
    consonants = count_consonants(s)

    if consonants != 0:
        ratio = vowels / consonants
        print("Vowels:", vowels)
        print("Consonants:", consonants)
        print("Ratio (Vowels : Consonants) =", ratio)
    else:
        print("Consonants count is zero. Ratio cannot be calculated.")



string = input("Enter a string: ")
vowel_consonant_ratio(string)
