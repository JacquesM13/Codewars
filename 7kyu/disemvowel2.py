def disemvowel(string_):
    return "".join(character for character in string_ if character.lower() not in 'aeiou')
