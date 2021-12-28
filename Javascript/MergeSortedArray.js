var merge = function(nums1, m, nums2, n) {
    let index1 = m
    let index2 = 0
    while(index1 < nums1.length){
        nums1[index1] = nums2[index2]
        index1++
        index2++
    }
     console.log(nums1.sort((a,b) => a - b))
     
 };

 merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)
 merge([1], 1, [], 0)
 merge([0], 0, [1], 1)

 /*
 You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

*/