var addBinary = function(a, b) {
    let sum = BigInt('0b' + a) + BigInt('0b' + b)
    console.log(sum.toString(2))
    
    return sum.toString(2)
};

addBinary('11', '1')
// => 100

addBinary('1010', '1011')
// => 10101