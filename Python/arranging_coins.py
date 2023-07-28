# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution(object):
    def arrangeCoins(self, n):
        i = 1

        while i <= n:
            n -= i
            if n > i:
                i += 1
            
        return i


arrangeCoins(5) # 2
arrangeCoins(8) # 3