# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

def can_construct(ransom_note, magazine)
    mag_sort = magazine.split('').sort
    ransom_sort = ransom_note.split('').sort.reverse


    mag_sort.each do |letter|
        if letter === ransom_sort[-1]
            ransom_sort.pop
        end
    end

    ransom_sort.empty?

end

can_construct("a", "b")
can_construct("aa", "ab")
can_construct("aa", "aab")

## Refactor ##
# def can_construct(ransom_note, magazine)
#     return true if ransom_note == magazine
    
#     count = Hash.new(0)
#     magazine.chars.each do |letter|
#         count[letter] += 1
#     end

#     ransom_note.chars.each do |letter|
#         return false if count[letter] == 0
#         count[letter] -= 1
#     end

#     return true
    
# end