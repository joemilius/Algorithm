function getIndexToIns(arr, num) {
    let sorted = arr.sort((a,b) => a - b)
    
    let index = 0
  
    for(let i = 0; i < arr.length; i++){
      if(arr[i] < num && arr[i + 1] > num){
        index = i + 1
      }else if(arr[i] === num){
        index = i
      }else if(arr[arr.length -1] < num){
        index = arr.length
      }
    }
    console.log(index)
    return index;
  }
  
  getIndexToIns([40, 60], 50);
  getIndexToIns([10, 20, 30, 40, 50], 35)
  getIndexToIns([10, 20, 30, 40, 50], 30)
  getIndexToIns([2, 5, 10], 15)