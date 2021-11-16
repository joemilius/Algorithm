function diffArray(arr1, arr2) {
    let newArr = arr1.concat(arr2);
  
    let filtered = newArr.filter(item => {
      if(!arr1.includes(item) || !arr2.includes(item)){
        return item
      }
    })
  
    console.log(filtered)
    return filtered;
  }
  
  diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);
  diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])