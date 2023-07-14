# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution(object):
    def wordPattern(self, pattern, s):
        arr = s.split()
        if len(arr) != len(pattern):
            return False
        
        for i in range(len(arr)):
            print(pattern.find(pattern[i]))
            print(arr.index(arr[i]))
            if pattern.find(pattern[i]) != arr.index(arr[i]):
                return False
        return True


newObj = Solution()
wordPattern("abba", "dog cat cat dog") # True
wordPattern("abba", "dog cat cat fish") # False
wordPattern("aaaa", "dog cat cat dog") # False
wordPattern("abba", "dog dog dog dog") # False
wordPattern("abba", "dog cat dog cat") # False