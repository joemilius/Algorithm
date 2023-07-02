# You are given an integer n that consists of exactly 3 digits.

# We call the number n fascinating if, after the following modification, the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0's:

# Concatenate n with the numbers 2 * n and 3 * n.
# Return true if n is fascinating, or false otherwise.

# Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.

def is_fascinating(n)
    check_number = 1
    times_two = n * 2
    times_three = n * 3
    number_array = "#{n}#{times_two}#{times_three}".split("").sort
    check = true
    number_array.each do |num|
        if "#{check_number}" != num
            check = false
        end
        check_number += 1
    end

    check
    
end

is_fascinating(192) #true
is_fascinating(100) #false