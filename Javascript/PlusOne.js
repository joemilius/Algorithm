var plusOne = function(digits) {
    let addOne = BigInt(digits.join('')) + BigInt(1)
    
    return addOne.toString().split('')
};

plusOne([1, 2, 3])
plusOne([4, 3, 2, 1])
plusOne([9, 9])
plusOne([1, 2, 3, 5, 6, 7, 3, 4, 8, 2, 9, 1, 5, 6, 3, 7, 8, 5, 9, 0, 2, 5, 7, 1 , 0, 7])