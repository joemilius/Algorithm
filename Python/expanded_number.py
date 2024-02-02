# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!

def expanded_form(number):
    digit_list = list(reversed([*str(number)]))
    zeros_string = ''
    place_value_list = []

    for n in digit_list:
        if n != '0':
            place_value_list.insert(0, n + zeros_string)
            
        zeros_string += '0'
    

    return ' + '.join(place_value_list)



print(expanded_form(12)) # Should return '10 + 2'
print(expanded_form(42)) # Should return '40 + 2'
print(expanded_form(70304)) # Should return '70000 + 300 + 4'


# def expanded_form(num):
#     num = list(str(num))
#     return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

# def expanded_form(num):
#     return " + ".join([str(int(d) * 10**p) for p, d in enumerate(str(num)[::-1]) if d != "0"][::-1])