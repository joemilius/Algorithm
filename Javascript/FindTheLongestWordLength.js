function findLongestWordLength(str) {
    let array = str.split(' ')
    let word = ''
  
  
    for(let i = 0; i < array.length; i++){
      if(array[i].length > word.length){
        word = array[i]
      }
    }
    
    console.log(word.length);
  }
  
  findLongestWordLength("The quick brown fox jumped over the lazy dog");