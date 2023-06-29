# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

def remove_trailing_zeros(num)
    num_array = num.split('')
    index = num.size - 1

    while index >= 0 do
        puts num_array[index]
        if num_array[index] == '0'
            num_array[index] = ''
        else
            return num_array.join('')
        end
        index -= 1
    end
end

remove_trailing_zeros("51230100")
remove_trailing_zeros("123")
remove_trailing_zeros("9")
remove_trailing_zeros("50")