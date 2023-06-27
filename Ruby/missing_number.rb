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

=begin

    summing and subtracting approach (built in method approach)
    
    time: O(n)
        I'm assuming sum still linear operation. 

    space: O(1)

    note:
        sum(0..nums.length) - sum(nums) using built in array methods.


def missing_number(nums)
    return (0..nums.length).sum - nums.sum
end

=end

=begin

    summing and subtracting approach
    
    time: O(n)
        Worst case you run the for loop n times the size of nums. 

    space: O(1)

    note:
        Clever trick sum(0..nums.length) - sum(nums)


def missing_number(nums)
    result = nums.length
 
     for i in (0..nums.length - 1)
         result += (i - nums[i])
     end
 
     return result 
 end

 =end

 =begin

    xor approach
    
    time: O(1)
        I'm assuming xor is a constant time operation.  

    space: O(1)

    note:
        Understand that xoring will give you the part that is missing wow!


def missing_number(nums)
    return nums.reduce(:^) ^ (0..nums.length).reduce(:^) 
end

=end