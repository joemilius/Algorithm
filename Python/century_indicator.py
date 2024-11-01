
# Output
# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28
# Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here

def century(year):
    # Finish this :)
    string = str(year)
    if(year < 101):
        return 1
    elif(year % 10 == 0):
        if(len(string) == 4 and year % 100 == 0):
            return int(string[:len(string) - 2])
        elif (len(string) == 3 and year % 100 == 0):
            return int(string[:len(string) - 1])
        else:
            return int(string[:len(string) - 2]) + 1
    else:
        return int(string[:len(string) - 2]) + 1
    

century(1705), 18, 'Testing for year 1705'
century(1900), 19, 'Testing for year 1900'
century(1601), 17, 'Testing for year 1601'
century(2000), 20, 'Testing for year 2000'
century(2340), 24, 'Testing for year 2340'
century(356), 4, 'Testing for year 356'
centruy(200), 2, 'Testing for year 2oo'
century(89), 1, 'Testing for year 89'

# def century(year):
#     return (year + 99) // 100


# import math

# def century(year):
#     return math.ceil(year / 100)