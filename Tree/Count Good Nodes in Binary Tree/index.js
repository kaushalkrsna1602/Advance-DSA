// 1448. Count Good Nodes in Binary Tree

// Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

// Return the number of good nodes in the binary tree.

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
var goodNodes = function (root) {
    let ans = 0;
    let traversal = (curr, maxSeenSoFar) => {
        if (curr.val >= maxSeenSoFar) {
            ++ans
        }

        let currMax = Math.max(maxSeenSoFar, curr.val)
        curr.left && traversal(curr.left, currMax)
        curr.right && traversal(curr.right, currMax)
    }
    traversal(root, -Infinity)
    return ans
};