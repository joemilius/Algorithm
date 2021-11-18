function medianSort(array){
    let median = 0
    let number = 0
    let sortedArray = []
    for(let i = 0; i < array.length; i++){
        if(Array.isArray(array[i])){
            if(array[i].length % 2 === 0){
                median = (array[i][arr[i].length / 2] + array[i][(arr[i].length / 2) - 1 ]) / 2
            }else {
                median = array[i][(arr[i].length - 1) / 2]
            }
        }else {
            number = arr[i]
        }
    }

    for(let j = 0; j < array.length; j++){
        if(Array.isArray(array[j])){
            if(median >= number){
                sortedArray.push(number)
                sortedArray.push(array[j])
            }else {

            }
        }
    }

}

/*
Write a function medianSort() that accepts one argument: an array. The elements of this array can be 
either numbers or arrays of numbers. The function should return the initial array sorted by the numbers 
or the median values of the arrays of numbers. 
 
For example: 
medianSort([3, [-2, 4, 9]]) à [3, [-2, 4, 9]] 
The median of [-2, 4, 9] is 4, so we should sort that array after the 3. 
 
medianSort([[12, 9, 1, 25], 4]) à [4, [12, 9, 1, 25]] 
The median of [12, 9, 1, 25] is 10.5, and 10.5 is greater than 4. 
 
medianSort([[2.4, 0.2, 9.8], 0, [-1], [-9, -4]]) à [[-9, -4], [-1], 0, [2.4, 
0.2, 9.8]] 
The median of [2.4, 0.2, 9.8] is 2.4. The median of [-1] is -1. The median of [-9, -4] is -6.5. 
Therefore, the sorted order of these medians is [-6.5, -1, 0, 2.4]
*/

/*
```const medianSort = (arr) => {
		return arr.sort((a, b) => {
   		if (Array.isArray(a)) {
      	a = a.reduce((c, d) => c+d, 0)
      }
      if (Array.isArray(b)) {
      	b = b.reduce((c, d) => c+d, 0)
      }
      return a - b
    })
}```
*/