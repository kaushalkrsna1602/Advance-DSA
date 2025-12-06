// 144. Binary Tree Preorder Traversal
// Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

// Example 1:

// Input: root = [1,null,2,3]

// Output: [1,2,3]

// Explanation:


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
 * @return {number[]}
 */
var preorderTraversal = function(root) {
    let ans = []
    function traversal(curr){
        if(!curr) return;
        ans.push(curr.val);
        traversal(curr.left);
        traversal(curr.right)
    }
    traversal(root)
    return ans;
};



// iterative appraoach

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
 * @return {number[]}
 */
var preorderTraversal = function(root) {
    if(!root) return []
    let ans = []
    let stack = [root]
    while(stack.length){
        let curr = stack.pop()
        ans.push(curr.val)
        curr.right && stack.push(curr.right)
        curr.left && stack.push(curr.left)
    }
    return ans
};