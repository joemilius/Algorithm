function sumFibs(num){
    let previous = 0
    let current = 1
    let answer = 0

    while (current <= num){
        if (current % 2 !== 0){
            answer += current
        }
        current += previous
        previous = current - previous
    }
    console.log(answer)
}

sumFibs(1000)
// => 1785