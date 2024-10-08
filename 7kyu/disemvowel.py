'''
Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
'''

def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    newString = ''
    for i in string_:
        if i not in vowels:
            newString += i
    return newString
    
'''
Good approach

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

'''
