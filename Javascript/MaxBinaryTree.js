/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
 var maxDepth = function(root) {
    //console.log(root.left, root.right)
    if(!root) return 0
    
    console.log('Left =', root.left, 'Right =', root.right)
    //console.log('Recursive Left', maxDepth(root.left))
    
    //console.log(Math.max(maxDepth(root.left)), Math.max(maxDepth(root.right)))
     
    return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1
};

/*
Given the root of a binary tree, return its maximum depth.
A binary tree’s maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf 
node.
*/