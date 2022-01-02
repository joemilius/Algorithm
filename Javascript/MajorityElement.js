var majorityElement = function(nums) {
    let sorted = nums.sort((a,b) => a - b)
    console.log(sorted)
    let first = 0
    let next = 1
    let comparison = []
    let majority = []
    
    while(next <= nums.length){
        
        if(nums[first] < nums[next]){          
            comparison = nums.splice(0, next)
            console.log(majority)
            first = 0
            next = 1
        }else if(next === nums.length){
            comparison = nums
        }else{
            first++
            next++
        }
        if(comparison.length > majority.length){
            majority = comparison
        }
            
            comparison = []
    }
    return majority[0]
};

/*
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
*/