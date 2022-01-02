var isValid = function(s) {
    if (s.length <=1) return false
    
    let stack = []
    let hash = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    
    for(let i = 0; i < s.length; i++){
        if (hash[s[i]]) stack.push(hash[s[i]])
        else if (s[i] !== stack.pop()) return false
    }
    return !stack.length
};

/*
// var isValid = function(s) {
//     let first = 0
//     let next = 1
//     valid = 0
//     while(next < s.length){
//         if(s[first] === '(' && s[next] === ')'){
//             valid = valid
//         }else if(s[first] === '{' && s[next] === '}'){
//             valid = valid
//         }else if(s[first] === '[' && s[next] === ']'){
//             valid = valid
//         }else {
//             valid++
//         } 
//         first += 2
//         next += 2
//     }
//     return valid === 0
// };
*/

/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
*/