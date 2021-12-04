function getBias(n){
let bias = 0
let first = 0
let second = 1

let sorted = n.sort((a,b) => a - b)

while(second <= sorted.length){
    bias = bias + (Math.abs(sorted[first]-sorted[second]))
    first = first + 2
    second = second + 2
}
console.log(bias)
}

getBias([2, 3, 1, 5])
//=> 3
getBias([1, 6, 6, 1])
//=>0

/*
- a company wants to reduce the amount of skill level bias between employees
- each employee has a numerical value to represent their skill level
- bias occurs when there is a gap in the skill level (the greater the gap the greater the bias)

create a function getBias that is given an array of numbers(representing each employee on a team by their skill level)
-the function should pair employees by their closest skill level and find the difference in skill level
-the difference will be the bias
-then the total bias would be the differences of each pair added together

Conditions:
- arrays will always have an even number of values
- all values will be positive integers
*/
function getBias(n){
   
    }
    
    getBias([2, 3, 1, 5])
    //=> 3
    getBias([1, 6, 6, 1])
    //=> 0