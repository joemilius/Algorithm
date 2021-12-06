function uniteUnique(arr) {
  
    let unique = arguments[0]
  
    for(let array = 1; array < arguments.length; array++){
      for(let index = 0; index < arguments[array].length; index++){
        if(!unique.includes(arguments[array][index])){
          unique.push(arguments[array][index])
        }
      }
    }
    console.log(unique)
    return arr;
  }
  
  uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);
  uniteUnique([1, 2, 3], [5, 2, 1])
  uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8])