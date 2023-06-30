# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
def move_zeroes(nums)
    zeros = []
    nums.each do |num|
        if num == 0
            zeros << 0
        end
    end
    nums.delete(0)

    nums.concat(zeros)

end

move_zeroes([0,1,0,3,12])
move_zeroes([0])
move_zeroes([0,0,1])
move_zeroes([0,0,0,0,0,0,1,1,1])

