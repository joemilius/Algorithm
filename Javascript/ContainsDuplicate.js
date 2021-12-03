var containsDuplicate = function(nums) {
    let set = new Set([...nums])
    
    return set.size !== nums.length
    
    
};

containsDuplicate([1, 2, 3, 1])
containsDuplicate([1, 2, 3, 4])