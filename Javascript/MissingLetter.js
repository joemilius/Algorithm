function fearNotLetter(str) {
    let alphabet = 'abcdefghijklmnopqrstuvwxyz'
    let newStart = alphabet.split(`${str[0]}`)[1]
    
    let strChar = 1
    let newStartChar = 0
    let missingLetter = undefined
  
    while(strChar < str.length){
       
      if(str[strChar] !== newStart[newStartChar]){
        missingLetter = newStart[newStartChar]
        strChar = str.length
      }
        strChar++
        newStartChar++
      }
      console.log(missingLetter)
      return missingLetter
    }
  
  fearNotLetter("abce");
  fearNotLetter("stvwx")
  fearNotLetter("abcdefghjklmno")
  fearNotLetter("abcdefghijklmnopqrstuvwxyz")