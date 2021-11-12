function confirmEnding(str, target) {
    let testResults = false
    console.log(str.substring(str.length - target.length))
  
    if(str.substring(str.length - target.length) === target){
      testResults = true
    }
    console.log(testResults)
  }
  
  confirmEnding("Bastian", "n");
  confirmEnding("Congratulation", "on")
  confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification")
  confirmEnding("He has to give me a new name", "name")
  confirmEnding("Open sesame", "same")
  confirmEnding("Open sesame", "sage")