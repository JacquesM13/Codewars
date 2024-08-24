'''
Description:

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

'''



# My solution

def pig_it(text):
    text = text.split(' ')
    out_string = ''
    for i in range(len(text)):
        if text[i].isalpha():
            text[i] = text[i][1:] + text[i][0:1] + 'ay'
    for i in range(len(text)):
        if i < len(text) - 1:
            out_string += text[i] + ' '
        else:
            out_string += text[i]
    return out_string

'''
Good solution
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
'''
