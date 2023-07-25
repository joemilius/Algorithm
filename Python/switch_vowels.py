# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution(object):
    def reverseVowels(self, s):
        vowel_list = []
        word_list = []
        string_list = [letter for letter in s]

        for letter in string_list:
            downcase = letter.lower()
            if downcase == 'a' or downcase == 'e' or downcase == 'i' or downcase == 'o' or downcase == 'u':
                vowel_list.insert(0, letter)
                word_list.append("_")
            else:
                word_list.append(letter)
        
        for index in range(len(word_list)):
            if word_list[index] == "_":
                word_list[index] = vowel_list.pop(0)

        
        return ''.join(word_list)


reverseVowels("hello") # holle
reverseVowels("boomerang") # baemorong 
reverseVowels("aA") # Aa
