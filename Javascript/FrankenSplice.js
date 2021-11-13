function frankenSplice(arr1, arr2, n) {
    let arr2Copy = arr2.slice()
    
    for(let i = 0; i < arr1.length; i++){
      arr2Copy.splice(n, 0, arr1[i])
      n++
    }
  
    console.log(arr2Copy)
    return arr2Copy;
  }
  
  frankenSplice([1, 2, 3], [4, 5, 6], 1);