# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.

def array_to_binary(array):
    binary_string = ''.join(str(n) for n in array)
    return int(binary_string ,2)

print(array_to_binary([0, 0, 0, 1])) # 1
print(array_to_binary([0, 0, 1, 0])) # 2
print(array_to_binary([0, 1, 0, 1])) # 5
print(array_to_binary([1, 0, 0, 1])) # 9
print(array_to_binary([0, 0, 1, 0])) # 2
print(array_to_binary([0, 1, 1, 0])) # 6
print(array_to_binary([1, 1, 1, 1])) # 15
print(array_to_binary([1, 0, 1, 1])) # 11
print(array_to_binary([1, 0, 1, 1, 0, 0, 0, 1])) # 177


# def binary_array_to_number(arr):
#     return int("".join(map(str, arr)), 2)