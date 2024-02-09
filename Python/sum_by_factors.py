# Given an array of positive or negative integers

#  I= [i1,..,in]

# you have to produce a sorted array P of the form

# [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

# P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

# Example:
# I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
# [2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

# Notes:

# It can happen that a sum is 0 if some numbers are negative!
# Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

# In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

## Too Slow but Works##
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def sum_by_factor(int_list):
    prime_factors = {}

    for n in int_list:

        i = 2
        while i <= abs(n):
            
            if n % i != 0:
                i += 1
            else:
                if i in prime_factors:
                    prime_factors[i] += n
                else:
                    prime_factors[i] = n
            i += 1
            
                

    dict_to_lists = [ [key]+[value] for key, value in zip(prime_factors.keys(), prime_factors.values()) ]
    return sorted(dict_to_lists, key=lambda x: x[0])





sum_by_factor([12, 15]) # [[2, 12], [3, 27], [5, 15]]
sum_by_factor([15, 30, -45]) # [[3, 0], [5, 0], [2, 30]]
sum_by_factor([15,21,24,30,45]) # [[2, 54], [3, 135], [5, 90], [7, 21]]
sum_by_factor([15,21,24,30,-45]) # [[2, 54], [3, 45], [5, 0], [7, 21]]
sum_by_factor([107, 158, 204, 100, 118, 123, 126, 110, 116, 100]) # [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]
sum_by_factor([-29804, -4209, -28265, -72769, -31744]) # [ [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], [7451, -29804] ]



#####
## Does Not Return a list of lists (ChatGPT Refactor)##
# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     i = 3
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 2
#     return True

# def sum_by_factor(int_list):
#     prime_factors = {}

#     for n in int_list:
#         if n == 0:
#             continue

#         abs_n = abs(n)
#         i = 2
#         while i * i <= abs_n:
#             if abs_n % i == 0:
#                 if is_prime(i):
#                     if i in prime_factors:
#                         prime_factors[i] += n
#                     else:
#                         prime_factors[i] = n
#                 factor = abs_n // i
#                 if factor != i and is_prime(factor):
#                     if factor in prime_factors:
#                         prime_factors[factor] += n
#                     else:
#                         prime_factors[factor] = n
#             i += 1
#     print(prime_factors.items())
#     return sorted(prime_factors.items())