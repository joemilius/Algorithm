function mutation(arr) {
    let first = arr[0].toLowerCase()
    let second = arr[1].toLowerCase()
    
    let firstLetters = first.split('')
    let secondLetters = second.split('')
    let truthArray = []
    
    let truthy = true
  
    for (let i = 0; i < secondLetters.length; i++){
    if(firstLetters.includes(secondLetters[i])){
      truthArray.push(true)
      
    }else if(!firstLetters.includes(secondLetters[i])){
      truthArray.push(false)
    }
    }
  
    if(truthArray.includes(false)){
      truthy = false
    }
    console.log(truthy)
    return truthy;
  }
  
  mutation(["hello", "hey"]);
  mutation(["hello", "Hello"])
  mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"])
  mutation(["Alien", "line"])
  mutation(["voodoo", "no"])