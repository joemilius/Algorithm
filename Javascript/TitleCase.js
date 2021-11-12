function titleCase(str) {
    str = str.toLowerCase();
    let wordArray = str.split(' ')
    
  
    for (let i = 0; i < wordArray.length; i++){
      wordArray[i] = wordArray[i].charAt(0).toUpperCase() + wordArray[i].slice(1)
    }
   let titleCase = wordArray.join(' ')
    return titleCase;
  }
  
  titleCase("I'm a little tea pot");