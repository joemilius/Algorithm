function destroyer(arr) {
    let argumentsArray = Object.values(arguments)
    let filtered = argumentsArray[0]
  
    for(let i = 1; i < argumentsArray.length; i++){
      filtered = filtered.filter(item => item !== argumentsArray[i])
    }
    console.log(filtered)
    return filtered;
  }
  
  destroyer([1, 2, 3, 1, 2, 3], 2, 3);

  /*
You will be provided with an initial array (the first argument in the destroyer function), 
followed by one or more arguments. Remove all elements from the initial array that are of 
the same value as these arguments.

Note: You have to use the arguments object.
  */