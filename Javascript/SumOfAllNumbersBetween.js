function sumAll(arr) {
    arr.sort((a, b) => a-b)

    let sum = 0
    for (let i = arr[0]; i <= arr[arr.length - 1]; i++){
      sum += i
    }
    console.log(sum)
    return sum
  }
  
  sumAll([4, 1]);
  sumAll([10, 5])