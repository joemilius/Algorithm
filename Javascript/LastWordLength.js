var lengthOfLastWord = function(s) {
    let stringArray = s.split(' ')
    let words = stringArray.filter((word) => word !== '')
    
    return words[words.length -1].length
};

lengthOfLastWord("Hello World")
// => 5

lengthOfLastWord("   fly me   to   the moon  ")
// => 4

lengthOfLastWord("luffy is still joyboy")
// => 6