function myReplace(str, before, after) {
    let words = str.split(' ')
    
    for(let i = 0; i < words.length; i++){
      if(words[i] === before){
        words.splice(i, 1, after)
      }
    }
    console.log(words.join(' '))
    return str;
}
  
myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped");
myReplace("He is Sleeping on the couch", "Sleeping", "sitting")
myReplace("His name is Tom", "Tom", "john")
myReplace("This has a spellngi error", "spellngi", "spelling")