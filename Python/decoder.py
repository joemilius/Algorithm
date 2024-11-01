# In this exercise, you will develop a function named decode(message_file). This function should read an encoded message from a .txt file and return its decoded version as a string.

# Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).

# Your function must be able to process an input file with the following format:

# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 I
# 5 you
# In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers increase consecutively, like so:

#   1
#  2 3
# 4 5 6
# The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message words are:

# 1: I
# 3: love
# 6: computers
# and your function should return the string "I love computers".


file = open('message_file.txt')
text = file.read()
file2 = open('coding_qual_input.txt')
text2 = file2.read()
print(file2)
# text2_list = text2.split('\n')
# text2_list.remove('')

# print(sorted(text2_list, key=lambda pair: int(pair.split(' ')[0])))

# nums = sorted(text2.split('\n'))

# sorted(text2.split('\n'), key=lambda pair: int(pair.split(' ')[0]))


def decode(message_file):
    file = open(message_file)
    message_str = file.read()
    message_file_list = message_str.split('\n')
    # message_file_list.remove('') This only removes one instance
    cleaned_message_file_list = [message for message in message_file_list if message != ''] # This removes all instances
    sorted_message_list = sorted(cleaned_message_file_list, key=lambda pair: int(pair.split(' ')[0]))
    step = 1
    decode_string = ''
   
    while len(sorted_message_list) != 0:
        if len(sorted_message_list) >= step and step == 1:
            print(sorted_message_list[0:step][-1].split(' ')[1])
            decode_string += sorted_message_list[0:step][-1].split(' ')[1]
            sorted_message_list = sorted_message_list[step:]
            step += 1
        elif len(sorted_message_list) >= step:
            print(sorted_message_list[0:step][-1].split(' ')[1])
            decode_string += " " + sorted_message_list[0:step][-1].split(' ')[1]
            sorted_message_list = sorted_message_list[step:]
            step += 1
        
    return decode_string

# print(decode(text))
print(decode('coding_qual_input.txt'))

