var removeElement = function(nums, val) {
    for (let i = 0; i < nums.length; i++) {
      if (nums[i] === val) {
        nums.splice(i, 1);
        i--;
          console.log(nums)
      }
    }
    return nums.length;
  };

//   var removeElement = function(nums, val) {
//     let i = 0;
//     for (let j = 0; j < nums.length; j++) {
//       if (nums[j] !== val) {
//         nums[i] = nums[j];
//         i++;
//       }
//     }
//     return i;
//   };

  removeElement([3,2,2,3], 3)
  removeElement([0,1,2,2,3,0,4,2], 2)