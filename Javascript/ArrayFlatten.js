function steamrollArray(arr){
    let cycle = arr.reduce((previousValue, currentValue) => previousValue.concat(currentValue), [])
for (let i = 0; i < arr.length; i++){
    cycle = cycle.reduce((previousValue, currentValue) => previousValue.concat(currentValue), [])
}
console.log(cycle)
return cycle
}

steamrollArray([1, [2], [3, [[4]]]])
steamrollArray([1, {}, [3, [[4]]]])