function findElement(arr, func) {
    // let truthyArray = arr.filter(func) or
    
    let num = 0;
    let truthyArr = []
    
  
    for (let i = 0; i < arr.length; i++) {
      num = arr[i]
      
      if (func(num)) {
        truthyArr.push(num)
      }
    }
    return truthyArr[0];
  }
  
  findElement([1, 2, 3, 4], num => num % 2 === 0);
  
  
  
  // findElement([1, 2, 3, 4], num => num % 2 === 0); => 2
  // findElement([1, 3, 5, 8, 9, 10], function(num) { return num % 2 === 0; }) => 8
  
  // findElement([1, 3, 5, 9], function(num) { 
  //  return num % 2 === 0; 
  //  }) => undefined
  
  // loop over arr and return FIRST element that passes TRUTH TEST 
  // for each element we want it to go threw the truth test
  // set num to each element as is loops
  // Pass num to func()
  // if truth test is true => push into truthArr