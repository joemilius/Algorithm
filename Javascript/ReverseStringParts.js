var reverseStr = function(s, k) {
    let stringArray = []
    let reversedParts = []
    
    let index = 0
    
    while(index <= s.length){
        stringArray.push(s.slice(index, index + k))
        reversedParts.push(stringArray[stringArray.length - 1].split('').reverse().join(''))
        reversedParts.push(s.slice(index + k, index + k + k))
        console.log(reversedParts)
        index += k + k
    }
    return reversedParts.join('')
};

/*
var reverseStr = function(s, k) {
    if (k > s.length)
        return s.split('').reverse().join('');
    for (let i = 0; i < s.length; i += 2 * k) {
        s = s.substring(0, i) + s.substr(i, k).split('').reverse().join('') + s.substring(i + k);
    }
    return s;
};
*/

/*
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
*/