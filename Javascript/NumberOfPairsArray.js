function sockMerchant(n, ar) {
    let copyArray = ar.slice()
    let sortedArray = copyArray.sort((a, b) => a - b)
    let pairArray = []
    let index = 0
    let counter = 1
    
    while(index < sortedArray.length){
        if(sortedArray[index] === sortedArray[index + 1]){
            pairArray = [...pairArray, sortedArray.splice(index, 2)]
              counter++
              index++
        }else {
            index++
        }
    }
    
    return counter
}