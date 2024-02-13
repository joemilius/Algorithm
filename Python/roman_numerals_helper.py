# Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

# 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
# 2008 is written as 2000=MM, 8=VIII; or MMVIII
# 1666 uses each Roman symbol in descending order: MDCLXVI.
# Input range : 1 <= n < 4000

# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

# Examples
# to roman:
# 2000 -> "MM"
# 1666 -> "MDCLXVI"
#   86 -> "LXXXVI"
#    1 -> "I"

# from roman:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "LXXXVI"  ->   86
# "I"       ->    1
# Help
# +--------+-------+
# | Symbol | Value |
# +--------+-------+
# |    M   |  1000 |
# |   CM   |   900 |
# |    D   |   500 |
# |   CD   |   400 |
# |    C   |   100 |
# |   XC   |    90 |
# |    L   |    50 |
# |   XL   |    40 |
# |    X   |    10 |
# |   IX   |     9 |
# |    V   |     5 |
# |   IV   |     4 |
# |    I   |     1 |
# +--------+-------+


class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        int_roman_dict = {'1':'I','5':'V','10':'X','50':'L','100':'C','500':'D','1000':'M','4':'IV','9':'IX','40':'XL','90':'XC','400':'CD','900':'CM'}
        int_string = str(val)[::-1]
        roman = []
        current_num = int_string[0]

        for i in int_string:
            new_number = list(current_num)
            new_number[0] = i
            current_num = ''.join(new_number)
            if current_num in int_roman_dict:
                roman.insert(0, int_roman_dict[current_num])
            elif 1 < int(current_num[0]) < 4:
                current_int = int(current_num) / int(current_num[0])
                added_string = int_roman_dict[str(int(current_int))] * int(current_num[0])
                roman.insert(0, added_string)
            elif 5 < int(current_num[0]) < 9:
                place_value = int(current_num) / int(current_num[0])
                multiplier = int(current_num[0]) - 5
                added_string = int_roman_dict[str(5 * int(place_value))] + (int_roman_dict[str(int(place_value))] * multiplier)
                roman.insert(0, added_string)

            
            current_num += '0'
            
        print(''.join(roman))
        return ''.join(roman)

    @staticmethod
    def from_roman(roman_num : str) -> int:
        roman_to_int_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(roman_num):
            if i+1<len(roman_num) and roman_num[i:i+2] in roman_to_int_dict:
                num+=roman_to_int_dict[roman_num[i:i+2]]
                i+=2
            else:
                #print(i)
                num+=roman_to_int_dict[roman_num[i]]
                i+=1
        print(num)
        return num
        
    


print(RomanNumerals.to_roman(1000)) # 'M'
print(RomanNumerals.to_roman(4)) # 'IV'
print(RomanNumerals.to_roman(1)) # 'I'
print(RomanNumerals.to_roman(1990)) # 'MCMXC'
print(RomanNumerals.to_roman(2008)) # 'MMVIII'

print(RomanNumerals.from_roman('XXI')) # 21
print(RomanNumerals.from_roman('I')) # 1
print(RomanNumerals.from_roman('IV')) # 4
print(RomanNumerals.from_roman('MMVIII')) # 2008
print(RomanNumerals.from_roman('MDCLXVI')) # 1666

#####
# from collections import OrderedDict
# import re


# ROMAN_NUMERALS = OrderedDict([
#     ('M', 1000),
#     ('CM', 900),
#     ('D', 500),
#     ('CD', 400),
#     ('C', 100),
#     ('XC', 90),
#     ('L', 50),
#     ('XL', 40),
#     ('X', 10),
#     ('IX', 9),
#     ('V', 5),
#     ('IV', 4),
#     ('I', 1),
# ])

# DECIMAL_TO_ROMAN = [(v, k) for k, v in ROMAN_NUMERALS.items()]

# ROMAN_RE = '|'.join(ROMAN_NUMERALS)


# class RomanNumerals(object):
#     @staticmethod
#     def from_roman(roman):
#         return sum(ROMAN_NUMERALS[d] for d in re.findall(ROMAN_RE, roman))

#     @staticmethod
#     def to_roman(decimal):
#         result = []
#         for number, roman in DECIMAL_TO_ROMAN:
#             while decimal >= number:
#                 decimal -= number
#                 result.append(roman)
#         return ''.join(result)


#####
# class RomanNumerals:

#     def to_roman(val):
#         onesRoman = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
#         tensRoman = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
#         hundsRoman = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
#         thousRoman = ["","M","MM","MMM","MMMM"]
            
#         ones =  onesRoman[val % 10]
#         tens = tensRoman[val // 10 % 10]
#         hunds = hundsRoman[val // 100 % 10]
#         thous = thousRoman[val // 1000]
        
            
#         return thous + hunds + tens + ones

#     def from_roman(roman_num):
#         out = 0 
#         mx = 0
#         for cur in map(lambda c: { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 } [c], roman_num[::-1]):
#             if cur >= mx: 
#                 out += cur
#                 mx = cur
#             else:
#                 out -= cur
        
#         return out

#####
# class RomanNumerals:
#     @staticmethod
#     def from_roman(s):
#         X=[dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))[x]for x in s]
#         return int(sum((x,-x)[x<y]for x,y in zip(X,X[1:]))+X[-1])
#     @staticmethod
#     def to_roman(i,o=' I II III IV V VI VII VIII IX'.split(' ')):
#         r=lambda n:o[n]if n<10 else''.join(dict(zip('IVXLC','XLCDM'))[c]for c in r(n//10))+o[n%10]
#         return r(i)

#####
# class RomanNumerals():

#     def to_roman(num):
#         R2M = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
#         string = ''
#         for k, v in R2M.items():
#             count = num // v
#             num %= v
#             string += count * k

#         return string

#     def from_roman(roman):
#         R2M = {'M':1000, 'i':900, 'D':500, 'j':400, 'C':100, 'k':90, 'L':50, 'l':40, 'X':10, 'm':9, 'V':5, 'n':4, 'I':1}
#         roman = roman.replace('CM', 'i').replace('CD', 'j').replace('XC', 'k').replace('XL', 'l').replace('IX', 'm').replace('IV', 'n')
#         return sum(R2M[i] for i in roman)