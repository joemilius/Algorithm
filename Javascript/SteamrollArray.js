function steamrollArray(arr) {
    const flattenedArray = [];
    // Loop over array contents
    for (let i = 0; i < arr.length; i++) {
      if (Array.isArray(arr[i])) {
        // Recursively flatten entries that are arrays
        //  and push into the flattenedArray
        flattenedArray.push(...steamrollArray(arr[i]));
      } else {
        // Copy contents that are not arrays
        flattenedArray.push(arr[i]);
      }
    }
    return flattenedArray;
  };

/*
With .flat() method 

function steamrollArray(arr) {
  
    let end = 0
    
    while(end < arr.length){
      arr = arr.flat()
      end++
      console.log(arr)
    }
    
    return arr;
  }

  
Flatten a nested array. You must account for varying levels of nesting.
  */