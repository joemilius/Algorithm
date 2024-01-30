# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

def hashtag_generator(string):
    # if(not string):
    #     return False
    
    hash_string = '#' + ''.join([word[0].upper() + word[1:len(word)].lower() for word in string.split(' ') if word])
    if len(hash_string) > 1 and len(hash_string) <= 140:
        return hash_string
    else:
        return False
    


print(hashtag_generator(" Hello there thanks for trying my Kata")) # "#HelloThereThanksForTryingMyKata"
print(hashtag_generator("    Hello     World   ")) # "#HelloWorld"
print(hashtag_generator("")) # False
print(hashtag_generator("Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat")) # False
print(hashtag_generator("ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq")) # '#ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq'
print(hashtag_generator('Codewars')) # '#Codewars'
print(hashtag_generator("Codewars      ")) # '#Codewars'
print(hashtag_generator("      Codewars")) # '#Codewars'
print(hashtag_generator("Codewars Is Nice")) # '#CodewarsIsNice'
print(hashtag_generator("codewars is nice")) # '#CodewarsIsNice'
print(hashtag_generator("CoDeWaRs is niCe")) # '#CodewarsIsNice'
print(hashtag_generator("c i n")) # '#CIN'
print(hashtag_generator("codewars  is  nice")) # '#CodewarsIsNice'

print(len('#ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq'))


# def generate_hashtag(s):
#     output = "#"
    
#     for word in s.split():
#         output += word.capitalize()
    
#     return False if (len(s) == 0 or len(output) > 140) else output


# def generate_hashtag(s):
#     ans = '#'+ str(s.title().replace(' ',''))
#     return s and not len(ans)>140 and ans or False

# def generate_hashtag(s):
#     return '#' + ''.join([word.title() for word in s.split(' ')]) if s and len(s) <= 140 else False