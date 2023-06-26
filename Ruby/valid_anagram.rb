# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def is_anagram(s, t)
    string1 = s.split('').sort.join('')
    string2 = t.split('').sort.join('')
    return string1 == string2
end

is_anagram("anagram", "nagaram")
is_anagram("rat", "car")