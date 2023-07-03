# You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.

# Return the total number of beautiful pairs in nums.

# Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.

def count_beautiful_pairs(nums)

    i = 0
    j = 1
    total = 0

    while i < nums.length - 1 do
        first_digit = nums[i].to_s()[0].to_i
        last_digit = nums[j].to_s()[-1].to_i
        puts first_digit
        puts last_digit
        puts first_digit.gcd(last_digit)

        if first_digit.gcd(last_digit) == 1
            total += 1
        end

        if j < nums.length - 1
            j += 1
        else
            i += 1
            j = i + 1
        end
    end

    total
    
end

count_beautiful_pairs([2,5,1,4])
count_beautiful_pairs([11,21,12])
count_beautiful_pairs([31,25,72,79,74])