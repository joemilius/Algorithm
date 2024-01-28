# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.


## Too Slow ##
# def max_sequence(array):
#     i = 0
#     j = 1
#     largest_sum = 0
#     sum_array = []
    
#     while i < len(array) - 1:
        
#         if sum(array[i:j]) > largest_sum:
#             largest_sum = sum(array[i:j])
#             sum_array = array[i:j]
                

#         if j == len(array):
#             i += 1
#             j = i + 1
              
#         else:
#             j += 1


#     print(sum_array)
#     return largest_sum

def max_sequence(arr):
    maximum = 0
    local_maximum = 0
    for i in arr:
        if local_maximum > 0:
            local_maximum += i
            if local_maximum < 0:
                local_maximum = 0
            elif local_maximum > maximum:
                maximum = local_maximum
        elif i > 0:
            local_maximum += i

    return maximum
    

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # return 6 from subarray [4, -1, 2, 1]
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4])) # 0
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43])) # 155

# def maxSequence(arr):
#     max,curr=0,0
#     for x in arr:
#         curr+=x
#         if curr<0:curr=0
#         if curr>max:max=curr
#     return max


# def maxSequence(arr):
#     maxl = 0
#     maxg = 0
#     for n in arr:
#         maxl = max(0, maxl + n)
#         maxg = max(maxg, maxl)
#     return maxg


# def maxSequence(arr):
# 	lowest = ans = total = 0
# 	for i in arr:
# 		total += i
# 		lowest = min(lowest, total)
# 		ans = max(ans, total - lowest)
# 	return ans