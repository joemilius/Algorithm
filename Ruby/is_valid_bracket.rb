# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def is_valid(s)
    return true if s.empty?
    
    stack = []
    s.each_char do |c|
        case c
        when '(', '{', '['
            stack.push(c)
        when ')'
            return false if stack.pop() != '('
        when '}'
            return false if stack.pop() != '{'
        when ']'
            return false if stack.pop() != '['
        end
    end
    puts stack.empty?
    return stack.empty?
end

is_valid("()")
is_valid("()[]{}")
is_valid("(]")
is_valid("([)]")

## Refactored in if conditionals Slower ##
# def is_valid(s)
#     string_array =  s.split('')
#     puts string_array
#     stack = []
#     string_array.each do |para|
#         if para == '(' || para == '{' || para == '['
#             stack << para
#         elsif para == ')'
#             if stack.pop != '('
#                 return false
#             end
#         elsif para == '}'
#             if stack.pop != '{'
#                 return false
#             end
#         elsif para == ']'
#             if stack.pop != '['
#                 return false
#             end

#         end
#     end

#     return stack.empty?
# end