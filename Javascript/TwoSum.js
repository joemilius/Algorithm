var twoSum = function(nums, target) {
    let indices = []
    let first = 0
    let second = 1
    let next = 1
    
    while(first < nums.length){
        while(second < nums.length){
        console.log(nums[first], nums[second])
            if(nums[first] + nums[second] === target){
                indices.push(first)
                indices.push(second)
                first = nums.length
                second = nums.length
            }
            second++
        }
        next++
        first++
        second = next
    }
        
    
    console.log(indices)
    return indices
    
};
// var twoSum = function(nums, target) {
//     let indices = []
//     let next = 1
//     let second = 1
    
//     for(let first = 0; first < nums.length; first++){
//             if(nums[first] + nums[next] === target){
//                 indices.push(first)
//                 indices.push(next)
//             }
//             next++
//             second++
//             next = second
//         }
        
    
//     console.log(indices)
//     return indices
    
// };

twoSum([2, 7, 11, 15], 9)
// => [0,1]
twoSum([3, 2, 4], 6)
// => [1,2]
twoSum([3,3], 6)
// => [0,1]