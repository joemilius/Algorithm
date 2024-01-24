# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!

def create_phone_number(numberArray):
    phone_number = ''
    i = 0
    while i < len(numberArray):
        if i == 0:
            phone_number += ('(' + str(numberArray[i]))
        elif i == 2:
            phone_number += (str(numberArray[i]) + ') ')
        elif i == 5:
            phone_number += (str(numberArray[i]) + '-')
        else:
            phone_number += str(numberArray[i])

        i += 1

    return phone_number


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # "(123) 456-7890"
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) # "(111) 111-1111"
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # "(123) 456-7890"
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])) # "(023) 056-0890"
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # "(000) 000-0000"


# def create_phone_number(n):
#     m = ''.join(map(str, n))
#     return f"({m[:3]}) {m[3:6]}-{m[6:]}"


# def create_phone_number(n):
# 	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# def create_phone_number(n):
#   d='('
#   #for loop to go through the array
#   for i in range(len(n)):
#   #get the first part of the final string
#       if i<3:
#           d=d+str(n[i])
#           if i==2:
#               d=d+') '
#   #get the middle part of the final string
#       elif i>=3 and i<6:
         
#           d=d+str(n[i])
#           if i==5:
#               d=d+'-'
#   #get the last 4 string members of the final string
#       elif i>=6 and i<10:
   
#           d=d+str(n[i])
#   # return the entire string        
#   return d