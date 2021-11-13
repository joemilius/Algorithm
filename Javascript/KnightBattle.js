function knightBattle(array, p, r){
    array.splice(p, 0, r)
    console.log(array)
    let counter = 0
    let winner = 0
    

    while(counter < array.length){
        if(array[0] === array[array.length -1]){
            array.splice(array.length - 1)
            winner++
        }else if(array[counter] === array[counter + 1]){
            array.splice(counter, 1)
            winner++
        }else if(array[counter] === array[counter - 1]){
            array.splice(counter - 1, 1)
            console.log('hi')
            winner = 1
        }else if(array[counter] !== array[counter + 1]){
            array.splice(counter, 1, array[counter] + winner)
            array.splice(counter, 1)
            
            winner = 0
            counter++
        } 
    }
    
    console.log(array)
}
knightBattle([8, 8, 6], 1, 8)
knightBattle([8, 6, 8], 1, 8)
knightBattle([1, 2, 4, 2, 3, 4], 1, 1)

//unfinished!

/*
should compare values of an array to the values next to it.  if they are the same
then one value is deleted and the other is incremented by 1 
for each value in the collection of values that are the same 
[8, 8, 8, 6] => [10, 6]
[8, 8, 6, 8] => [10, 6]
[1, 1, 2, 4, 2, 3, 4] => [3, 4, 2, 3, 4]
*/

// knightBattle([8, 8, 6], 1, 8)
// knightBattle([8, 6, 8], 1, 8)
knightBattle([1, 2, 4, 2, 3, 4], 1, 1)