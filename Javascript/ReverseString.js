function reverseString(str) {
    let reverseArray = []

    for(let i = 0; i < str.length; i++){
        reverseArray.unshift(str[i])
    }
    
    let reverseString = reverseArray.join('')
    console.log(reverseString);
  }
  
  reverseString("hello")
  reverseString("Howdy")
  reverseString("Greetings from Earth")