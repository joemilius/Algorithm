def is_anagram(s, t)
    string1 = s.split('').sort.join('')
    string2 = t.split('').sort.join('')
    return string1 == string2
end

is_anagram("anagram", "nagaram")
is_anagram("rat", "car")