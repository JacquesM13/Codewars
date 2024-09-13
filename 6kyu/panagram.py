def is_pangram(s):
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s.lower():
            return False
    return True
