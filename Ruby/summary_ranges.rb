# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

def summary_ranges(nums)

    start = nums[0]
    last = nums[0]
    range_array =[]

    nums.each_with_index do |num, index|
        next_number = nums[index + 1]
        if next_number == last + 1
            last = next_number
        elsif start == last
            range_array << "#{start}"
            start = next_number
            last = next_number
        else
            range_array << "#{start}->#{last}"
            start = next_number
            last = next_number
        end
   
    end
    range_array
    
end

summary_ranges([0,1,2,4,5,7]) ## ["0->2","4->5","7"]
summary_ranges([0,2,3,4,6,8,9]) ## ["0","2->4","6","8->9"]