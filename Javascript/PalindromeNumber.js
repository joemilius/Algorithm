var isPalindrome = function(x) {
    let original = x.toString().split('').join('')
    let reversed = x.toString().split('').reverse().join('')
    
    if(original === reversed){
        return true
    }else {
        return false
    }
};

isPalindrome(121)
// => true
isPalindrome(-121)
// => false
isPalindrome(10)
// => false
isPalindrome(-101)
// => false