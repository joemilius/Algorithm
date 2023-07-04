# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

### Too Slow ###
# class Solution(object):
#     def buddyStrings(self, s, goal):
#         """
#         :type s: str
#         :type goal: str
#         :rtype: bool
#         """
#         index1 = 0
#         index2 = 1
#         string_array = list(s)
#         valid = False

#         print(len(string_array) - 1)
        
#         while index1 < len(string_array) - 1:
#             value1 = string_array[index1]
#             value2 = string_array[index2]
#             string_array[index1] = value2
#             string_array[index2] = value1
#             print(index1)
#             if ''.join(string_array) == goal:
#                 valid = True
#             else:
#                 string_array[index1] = value1
#                 string_array[index2] = value2


#             if index2 < len(string_array) - 1:
#                 index2 += 1
#             else:
#                 index1 += 1
#                 index2 = index1 + 1

#         return valid

class Solution:
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)
        
        diff_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_indices.append(i)
                if len(diff_indices) > 2:
                    return False
        
        return len(diff_indices) == 2 and s[diff_indices[0]] == goal[diff_indices[1]] and s[diff_indices[1]] == goal[diff_indices[0]]

    buddyStrings("ab", "ba") #true
    buddyStrings("ab", "ab") #false
    buddyStrings("aa", "aa") #true
    buddyStrings("aaaaaaabc", "aaaaaaacb")