// Our Code
// function spinalCase(str) {
//     let newStr = str.replace(/[^a-zA-Z0-9]/g,' ')
//     let newStrTwo = newStr.replace(/([A-Z])/g, ' $1').trim()
//     return newStrTwo.replaceAll("  ", " ").replaceAll(" ", "-").toLowerCase()
//   }
  
  
  
  // Solution Code
  function spinalCase(str) {
    var regex = /\s+|_+/g;
    str = str.replace(/([a-z])([A-Z])/g, "$1 $2");
    return str.replace(regex, "-").toLowerCase();
  }
  spinalCase('This Is Spinal Tap');
  spinalCase('thisIsSpinalTap');
  spinalCase("The_Andy_Griffith_Show");
  spinalCase("Teletubbies say Eh-oh");
  spinalCase("AllThe-small Things");