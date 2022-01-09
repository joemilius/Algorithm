/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	            -1 if num is lower than the guess number
 *			             1 if num is higher than the guess number
 *                       otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
 var guessNumber = function(n) {
    let pick = 0
    
    for(let i = 0; i <= n; i++){
        if(guess(i) == 0){
            pick = i
        }   
    }
    console.log(pick)
    return pick
};

/* Faster Solution
var guessNumber = function(n) {
    let left = 0;
    let right = n;
    
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (guess(mid) == 0) {
            return mid;
        } else if (guess(mid) == -1) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return 0;
*/

/*
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.
*/