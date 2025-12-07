// Binary Tree Inorder Traversal 94

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
var inorderTraversal = function(root) {
    let ans = []
    function traversal(curr) {
        if(!curr) return 
        traversal(curr.left)
        ans.push(curr.val)
        traversal(curr.right)
    }
    traversal(root)
    return ans
};


// itrerative approach

var inorderTraversal = function(root) {
    let ans = [];
    let stack = [];
    let curr = root;

    while(curr || stack.length) {
        while(curr) {
            stack.push(curr);
            curr = curr.left;
        }
        curr = stack.pop();
        ans.push(curr.val);
        curr = curr.right;
    }
    return ans;
};
     