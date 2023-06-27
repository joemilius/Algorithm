# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missing_number(nums)
    for num in 0..(nums.size - 1) do
        if !nums.include?(num)
            return num
        end
    end
    nums.size
end

missing_number([3,0,1])
missing_number([0,1])
missing_number([9,6,4,2,3,5,7,0,1])