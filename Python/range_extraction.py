# DESCRIPTION:
# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

# Example:

# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

def range_extraction(num_list):
    num1 = num_list[0]
    num2 = num_list[0]
    range_list = []

    for n in num_list:
        
        if num_list.index(n) + 1 < len(num_list) and num_list[num_list.index(n) + 1] == n + 1:
            num2 = num_list[num_list.index(n) + 1]
        else:
            if num2 - num1 >= 2:
                range_list.append(f'{num1}-{num2}')
            elif num2 - num1 == 1:
                range_list.append(f'{num1}')
                range_list.append(f'{num2}')
            else:
                range_list.append(f'{num1}')
                

            if num_list.index(n) + 1 < len(num_list): 
                num1 = num_list[num_list.index(n) + 1]
                num2 = num_list[num_list.index(n) + 1]


    return ','.join(range_list)





print(range_extraction([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])) # "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
print(range_extraction([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) # '-6,-3-1,3-5,7-11,14,15,17-20'
print(range_extraction([-3,-2,-1,2,10,15,16,18,19,20])) # '-3--1,2,10,15,16,18-20'

#####
# def solution(args):
#     out = []
#     beg = end = args[0]
    
#     for n in args[1:] + [""]:        
#         if n != end + 1:
#             if end == beg:
#                 out.append( str(beg) )
#             elif end == beg + 1:
#                 out.extend( [str(beg), str(end)] )
#             else:
#                 out.append( str(beg) + "-" + str(end) )
#             beg = n
#         end = n
    
#     return ",".join(out)


#####
# def solution(args):
#     result = ""
#     i = 0
#     while i<len(args):
#         val = args[i]
#         while i+1<len(args) and args[i]+1==args[i+1]:
#             i+=1
#         if val == args[i]:
#             result += ",%s"%val
#         elif val+1 == args[i]:
#             result += ",%s,%s"%(val, args[i])
#         else:
#             result += ",%s-%s"%(val, args[i])
#         i+=1
#     return result.lstrip(",")


#####
# def printable(arr):
#     return (','.join(str(x) for x in arr) if len(arr) < 3  # one or two consecutive integers : comma separated
#             else f'{arr[0]}-{arr[-1]}')                    # more : dash separated first and last integer

# def solution(args):
#     chunk, ret = [], []                                    # instantiate variables

#     for i in args:                                         # for each integer
#         if not len(chunk) or i == chunk[-1] + 1:           #     if first or consecutive
#             chunk.append(i)                                #         add to current chunk
#         else:                                              #     else, it's a gap
#             ret.append(printable(chunk))                   #         save current chunk
#             chunk = [i]                                    #         and restart a new one

#     ret.append(printable(chunk))                           # do not forget last chunk !

#     return ','.join(ret)                                   # return comma separated chunks