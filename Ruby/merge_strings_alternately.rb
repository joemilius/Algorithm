# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

def merge_alternately(word1, word2)
    combined_string = ""
    index = 0

    if word1.length > word2.length
       while index < word2.length
        combined_string += word1[index]
        combined_string += word2[index]
        index += 1
       end
       puts word1[index..-1]
       combined_string += word1[index..-1]

    elsif word1.length < word2.length
        while index < word1.length
            combined_string += word1[index]
            combined_string += word2[index]
            index += 1
        end
        puts word2[(index)..-1]
        combined_string += word2[index..-1]

    else
        while index < word1.length
            combined_string += word1[index]
            combined_string += word2[index]
            index += 1
        end
        combined_string
    end

end

merge_alternately("abc", "pqr")
merge_alternately("ab", "pqrs")
merge_alternately("abcd", "pq")