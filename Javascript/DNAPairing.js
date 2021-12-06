function pairElement(str) {
    console.log(str[0])
    let pair = []
    let allPairs = []
    for(let i = 0; i < str.length; i++){
      if(str[i] === 'G'){
        pair.push('G')
        pair.push('C')
        allPairs.push(pair)
        pair = []
      } else if(str[i] === 'C'){
        pair.push('C')
        pair.push('G')
        allPairs.push(pair)
        pair = []
      }else if(str[i] === 'A'){
        pair.push('A')
        pair.push('T')
        allPairs.push(pair)
        pair = []
      } else {
        pair.push('T')
        pair.push('A')
        allPairs.push(pair)
        pair = []
      }
    }
    console.log(allPairs)
    return allPairs;
  }
  
  pairElement("GCG");
  pairElement("ATCGA")