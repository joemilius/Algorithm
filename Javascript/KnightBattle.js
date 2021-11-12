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

//unfinished!

/*
should compare values of an array to the values next to it.  if they are the same
then one value is deleted and the other is incremented by 1 
for each value in the collection of values that are the same 
[8, 8, 8, 6] => [10, 6]
[8, 8, 6, 8] => [10, 6]
[1, 1, 2, 4, 2, 3, 4] => [3, 4, 2, 3, 4]
*/