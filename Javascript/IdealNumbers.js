function idealNumbers(low, high){
    let idealNumbers = []
    let total = 0
    for(let x = 0; total <= high; x++){
        for(let y = 0; total <= high; y++){
            if((3**x) * (5**y) >= low && (3**x) * (5**y) <= high){
                idealNumbers.push((3**x) * (5**y))
            }
            total = ((3**x) * (5**y))
        }
        total = (3**x)
    }
    console.log(idealNumbers)
    console.log(idealNumbers.length)
}

idealNumbers(225, 405)
// => 4 (numbers)
idealNumbers(25, 125)
// => 6 (numbers)

/*
ideal numbers can be described as 3**x * 5**y
how many ideal numbers fall into the range of the low and high numbers provided?
*/

/*
create a function idealNumbers that takes in the arguments low and high
find how many ideal numbers can be found within the range of two numbers
ideal numbers are be described as 3**x * 5**y
how many ideal numbers fall into the range of the low and high numbers provided?
*/
function idealNumbers(low, high){
    
}

idealNumbers(225, 405)
// => 4 (numbers)
idealNumbers(25, 125)
// => 6 (numbers)
