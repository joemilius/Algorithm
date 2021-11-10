function countBits(n){
    let number = (n).toString(2)
    let counter = 0

    for(let i = 0; i < number.length; i++){
        if(number[i] === '1'){
            counter++
        }
    }
    return counter
}