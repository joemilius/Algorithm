function largestOfFour(arr) {
    let largestNumbers = []
    for(let i = 0; i < arr.length; i++){
      arr[i].sort((a,b)=> a-b)
      largestNumbers.push(arr[i][arr[i].length - 1])
    }
    
    console.log(largestNumbers);
  }
  
  largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);