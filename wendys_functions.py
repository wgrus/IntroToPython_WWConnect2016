def print_5times(string):
    '''prints the input string 5 times'''
    print(string*5)
    
def contains_orange(string):
    '''takes in a sentence and returns a boolean indicating 
    if the string contains the word orange'''
    return "orange" in string
    
def is_vowel(string):
    '''takes in a character and returns a boolean indicating 
    if the character is a vowel'''
    return string.lower() in ['a', 'e', 'i', 'o', 'u']