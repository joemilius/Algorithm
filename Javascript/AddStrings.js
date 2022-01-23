var addStrings = function(num1, num2) {
    let num1Array = num1.split('').reverse()
    let num2Array = num2.split('').reverse()
    let sumArray = []
    
    let longest = 0
    
    if(num1Array.length > num2Array.length){
        longest = num1Array.length
    }else if(num1Array.length < num2Array.length){
        longest = num2Array.length
    }
    
    for(let i = 0; i < longest; i++){
        if(num1Array[i] && num2Array[i]){
        sumArray.push(parseInt(num1Array[i]) + parseInt(num2Array[i]))
        } else if(num1Array[i]){
            sumArray.push(parseInt(num1Array[i]))
        }else if(num2Array[i]){
            sumArray.push(parseInt(num2Array[i]))
        }
    }
    return sumArray.reverse()
};

/*
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
*/