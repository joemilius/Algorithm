function translatePigLatin(str) {
    let letters = str.split('')
    let pigLatin = []
    let i = 0
    if(letters[0]=== 'a' || letters[0] === 'e' ||     letters[0] === 'i' || letters[0] === 'o' || letters[0] === 'u'){
      letters.push('way')
      console.log(letters.join(''))
      return letters.join('')
    }else {
    while(i <= letters.length){
    if(letters[i] === 'a' || letters[i] === 'e' || letters[i] === 'i' || letters[i] === 'o' || letters[i] === 'u' || i === letters.length){
      pigLatin.push(letters.splice(0, i).join('') + 'ay')
      i = letters.length  
    }
    i++
    }
    console.log(letters.join('') + pigLatin)
    return letters.join('') + pigLatin
    }
    
  }
  
  translatePigLatin("consonant");
  translatePigLatin("glove")
  translatePigLatin("eight")
  translatePigLatin("rhythm")