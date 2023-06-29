# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

## Solution Takes too long ##
# def is_power_of_two(n)
#     for number in 0..(n) do
#         if n == 2**number
#            return true
#         end
#     end
#     false
# end

def is_power_of_two(n)
    n > 0 && (n & (n - 1)) == 0
end

is_power_of_two(1)
is_power_of_two(16)
is_power_of_two(3)
is_power_of_two(131073)
is_power_of_two(262145)
is_power_of_two(4)