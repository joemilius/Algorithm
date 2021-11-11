function knightBattle(array, p, r){
    let seatAddedArray = array.splice(p, 0, r)

    let counter = 0

    while(counter < seatAddedArray.length){
        if(seatAddedArray[0] === seatAddedArray[seatAddedArray[seatAddedArray.length -1]]){
            seatAddedArray.pop()
            seatAddedArray[0] = seatAddedArray[0] + 1
        }else if(seatAddedArray[counter]){
            
        }
    }
}