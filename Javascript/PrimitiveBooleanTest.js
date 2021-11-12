function booWho(bool) {
    let primitiveTest = false
    if(bool === true || bool === false){
      primitiveTest = true
    }
    console.log(primitiveTest)
    return primitiveTest;
  }
  
booWho([1, 2, 3]);
booWho(true)
booWho(false)
booWho([1, 2, 3]) 
booWho([].slice) 
booWho({ "a": 1 }) 
booWho(1) 
booWho(NaN) 
booWho("a") 
booWho("true") 
booWho("false")