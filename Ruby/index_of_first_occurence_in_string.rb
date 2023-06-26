# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def str_str(haystack, needle)
    index = 0
    haystack.each_char do |char|
        
            if haystack[index..(index + needle.length - 1)] == needle
                return index
            end
        index += 1
    end
    return -1
end

str_str("sadbutsad", "sad")
str_str("leetcode", "leeto")