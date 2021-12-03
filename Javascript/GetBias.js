function getBias(nums){
let bias = 0
let first = 0
let second = 1

let sorted = nums.sort((a,b) => a - b)

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