'''
Description:

Create a function isAlt() that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.

is_alt("amazon")  # True
is_alt("apple")   # False
is_alt("banana")  # True

Arguments consist of only lowercase letters.
'''

def is_alt(s):
    vowels = 'aeiou'
    print(s)
    for i in range(len(s) - 1):
        if s[i] not in vowels and s[i+1] not in vowels or s[i] in vowels and s[i+1] in vowels:
            return False
    return True
