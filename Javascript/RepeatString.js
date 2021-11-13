function repeatStringNumTimes(str, num) {

    let repeat = []
  
    for(let i = 0; i < num; i++){
      repeat.push(str)
    }
    
    let joined = repeat.join('')
    
    return joined;
  }
  
  repeatStringNumTimes("abc", 3);