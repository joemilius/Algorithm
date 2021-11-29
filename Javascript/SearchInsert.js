var searchInsert = function(nums, target) {   
    if(nums.includes(target)){
        return nums.indexOf(target)
    }
    
    nums.push(target)
    nums.sort((a,b) => a-b)
    return nums.indexOf(target)
};

searchInsert([1,3,4,6], 5)
searchInsert([3,5,6,7,9,10], 8)