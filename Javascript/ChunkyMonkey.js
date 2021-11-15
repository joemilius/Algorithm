function chunkArrayInGroups(arr, size){
    let newChunk = []

    while (arr.length > 0){
        newChunk.push(arr.splice(0, size))
    }
    console.log(newChunk)
    return newChunk
}

chunkArrayInGroups(["a", "b", "c", "d"], 2);