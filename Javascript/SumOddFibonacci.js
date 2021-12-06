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

// function sumFibs(num) {
  
//     let first = 0
//     let second = 1
//     let next = 1
//     let oddNumbers = [1]
  
//     while(next <= num){
//       console.log(next)
//       if(next % 2 !== 0){
//         oddNumbers.push(next) 
//       }
//       first = second
//       second = next
//       next = first + second
//     }
//     console.log(oddNumbers.reduce((previous, current) => previous + current))
//     return oddNumbers.reduce((previous, current) => previous + current);
//   }
  
//   sumFibs(4);
//   // => 5
//   sumFibs(10)
//   // => 10
//   sumFibs(1000)
//   //=> 1785
//   sumFibs(4000000)
//   //=> 4613732