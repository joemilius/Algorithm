function mutation(arr) {
    let first = arr[0].toLowerCase()
    let second = arr[1].toLowerCase()
    
    console.log(first)
    console.log(second)
    
    let truthy = false
    if(first === second){
      truthy = true
    }
    console.log(truthy)
    return truthy;
  }
  
  mutation(["hello", "hey"]);
  mutation(["hello", "Hello"])


/*
mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]) should return true.

mutation(["Mary", "Army"]) should return true.

Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array.

For example, ["hello", "Hello"], should return true because all of the letters in the second string are present in the first, ignoring case.

The arguments ["hello", "hey"] should return false because the string hello does not contain a y.

Lastly, ["Alien", "line"], should return true because all of the letters in line are present in Alien.
*/