# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.

class Solution(object):
    def countSegments(self, s):
        return len(s.split())
    
countSegments("Hello, my name is John") # 5
countSegments("Hello") # 1