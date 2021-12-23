var searchInsert = function(nums, target) {   
    if(nums.includes(target)){
        return nums.indexOf(target)
    }
    
    nums.push(target)
    nums.sort((a,b) => a-b)
    return nums.indexOf(target)
};

// var searchInsert = function(nums, target) {
    
//     for(let i = 0; i < nums.length; i++){
//         if(nums[i] === target){
//             return i
//         }else if(nums[i] < target && nums[i + 1] > target){
//             return i + 1
//         }else if(nums[nums.length - 1] < target){
//             return nums.length 
//         }
//     }
// };

searchInsert([1,3,4,6], 5)
searchInsert([3,5,6,7,9,10], 8)