function whatIsInAName(collection, source) {
    let sourceKeys = Object.keys(source)
     
    let filtered = collection.filter(item => {
      for (let i = 0; i < sourceKeys.length; i++){
      if (!item.hasOwnProperty(sourceKeys[i]) ||
          item[sourceKeys[i]] !== source[sourceKeys[i]]){
          return false;
        }
        return true;
      }
    })

  console.log(filtered)
    
    return filtered;
  }
  
  whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });
  whatIsInAName([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "cookie": 2 })