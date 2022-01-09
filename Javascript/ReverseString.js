function reverseString(str) {
    let reverseArray = []

    for(let i = 0; i < str.length; i++){
        reverseArray.unshift(str[i])
    }
    
    let reverseString = reverseArray.join('')
    console.log(reverseString);
  }
  
  reverseString("hello")
  reverseString("Howdy")
  reverseString("Greetings from Earth")

/* Easier Solution

var reverseString = function(s) {
    return s.reverse()
};

reverseString(["H","a","n","n","a","h"])
reverseString(["h","e","l","l","o"])

*/

/*
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
*/