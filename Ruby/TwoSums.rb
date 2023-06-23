def two_sum(nums, target)
    index1 = 0
    index2 = 1
    while index1 < nums.length() do
        if (nums[index1] + nums[index2] == target)
            return [index1, index2]
        end
        
        if (index2 + 1 == nums.length())
            index1 += 1
            index2 = index1 + 1
        else
            index2 += 1
        end

    end
end

two_sum([2,7,11,15], 9)
two_sum([3,2,4], 6)
two_sum([3,3], 6)

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.