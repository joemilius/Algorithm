def is_palindrome(s)
    # if s.length == 1
    #     return true
    # end
    
    alpha_string = s.delete('^a-zA-Z0-9').downcase
    beginning = 0
    ending = alpha_string.length - 1
    palindrome = true

    while beginning < alpha_string.length / 2 do

        if alpha_string[beginning] != alpha_string[ending]
            palindrome = false
        end
        beginning += 1
        ending -= 1
    end
    
    puts palindrome
    palindrome
    
end

is_palindrome("A man, a plan, a canal: Panama")
is_palindrome("race a car")
is_palindrome(" ")
is_palindrome("a")
is_palindrome("ab")
