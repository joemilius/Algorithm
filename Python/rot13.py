# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

def rotation_cipher_13(string):
    cipher_dict_rot13 = {'a': 'n', 'A':'N', 'b':'o', 'B':'O', 'c':'p', 'C':'P', 'd':'q', 'D':'Q', 'e':'r', 'E':'R', 'f':'s', 'F':'S', 'g':'t', 'G':'T', 'h': 'u', 'H':'U', 'i':'v', 'I':'V', 'j':'w', 'J':'W', 'k':'x', 'K':'X', 'l':'y', 'L':'Y', 'm':'z', 'M':'Z', 'n':'a', 'N':'A', 'o':'b', 'O':'B', 'p':'c', 'P':'C', 'q':'d', 'Q':'D', 'r':'e', 'R':'E', 's':'f', 'S':'F', 't':'g', 'T':'G', 'u': 'h', 'U':'H', 'v':'i', 'V':'I', 'w':'j', 'W':'J', 'x':'k', 'X':'K', 'y':'l', 'Y':'L', 'z':'m', 'Z':'M'}
    cipher_string = ''
    for letter in string:
        if letter in cipher_dict_rot13:
            cipher_string += cipher_dict_rot13[letter]
        else:
            cipher_string += letter

    return cipher_string


print(rotation_cipher_13('test')) # 'grfg'
print(rotation_cipher_13('Test')) # 'Grfg'
print(rotation_cipher_13('aA bB zZ 1234 *!?%')) # 'nN oO mM 1234 *!?%'


#####
# import string
# from codecs import encode as _dont_use_this_

# def rot13(message):
#     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     outputMessage = ""
#     for letter in message:
#         if letter in alpha.lower():
#             outputMessage += alpha[(alpha.lower().index(letter) +13) % 26].lower()
#         elif letter in alpha:
#             outputMessage += alpha[(alpha.index(letter) +13) % 26]
#         else:
#             outputMessage += letter
#     return outputMessage

#####
# def rot13(message):
#     return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

#####
# def rot13(message):
#     result = ''
#     for char in message:
#         if char.isalpha() and char.isupper():
#             result += chr((((ord(char) - 65) + 13) % 26) + 65)
#         elif char.isalpha() and char.islower():
#             result += chr((((ord(char) - 97) + 13) % 26) + 97)
#         else:
#             result += char
#     return result

#####
# def rot13(message):
#     return ''.join(chr((65 if c.isupper() else 97) + ((ord(c) - (65 if c.isupper() else 97)) + 13)%26) if c.isalpha() else c for c in message)