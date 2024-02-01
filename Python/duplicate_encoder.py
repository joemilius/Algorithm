# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

def duplicate_encoder(string):
    encoder = ''
    for letter in string.lower():
        copyOfString = string.lower().replace(letter, '', 1)
       
        if letter in copyOfString:
            encoder += ')'
        else:
            encoder += '('

    return encoder


print(duplicate_encoder('din')) # "((("
print(duplicate_encoder("recede")) # "()()()"
print(duplicate_encoder("Success")) # ")())())"
print(duplicate_encoder("(( @")) # "))(("

# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])



# def duplicate_encode(word):
#     """a new string where each character in the new string is '(' 
#     if that character appears only once in the original word, or ')' 
#     if that character appears more than once in the original word. 
#     Ignores capitalization when determining if a character is a duplicate. """
#     word = word.upper()
#     result = ""
#     for char in word:
#         if word.count(char) > 1:
#             result += ")"
#         else:
#             result += "("
            
#     return result

#####
# from collections import Counter

# def duplicate_encode(word):
#     word = word.lower()
#     counter = Counter(word)
#     return ''.join(('(' if counter[c] == 1 else ')') for c in word)
#####


# def duplicate_encode(word):
#     word = word.lower()
    
#     dict = {}
#     for char in word:
#         dict[char] = ')' if char in dict else '('
    
#     return ''.join( dict[char] for char in word )