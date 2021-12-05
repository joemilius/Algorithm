function myReplace(str, before, after) {
    let words = str.split(' ')
    let newWord = after
    
    if(before.split('')[0] === before.split('')[0].toUpperCase()){
      newWord = after.split('')
      newWord.splice(0, 1, after[0].toUpperCase())
      newWord = newWord.join('')
      console.log(newWord)
    }else {
      newWord = after.split('')
      newWord.splice(0, 1, after[0].toLowerCase())
      newWord = newWord.join('')
      console.log(newWord)
    }
    
    for(let i = 0; i < words.length; i++){
      if(words[i] === before){
        words.splice(i, 1, newWord)
      }
    }
    console.log(words.join(' '))
    return words.join(' ');
  }
  
  myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped");
  myReplace("He is Sleeping on the couch", "Sleeping", "sitting")
  myReplace("His name is Tom", "Tom", "john")
  myReplace("This has a spellngi error", "spellngi", "spelling")
  myReplace("Let us go to the store", "store", "mall")