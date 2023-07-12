# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution(object):
    def shuffle(self, nums, n):
        shuffled = []
        index2 = n

        for index1 in range(0, len(nums) - n):
            shuffled.append(nums[index1])
            shuffled.append(nums[index2])
            index2 += 1

        return shuffled


shuffle([2,5,1,3,4,7], 3) # [2,3,5,4,1,7]
shuffle([1,2,3,4,4,3,2,1], 4) # [1,4,2,3,3,2,4,1]
shuffle([1,1,2,2], 2) # [1,2,1,2]