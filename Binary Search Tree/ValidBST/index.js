// 98. Validate Binary Search Tree
// Solved
// Medium
// Topics
// premium lock icon
// Companies
// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

// A valid BST is defined as follows:

// The left subtree of a node contains only nodes with keys strictly less than the node's key.
// The right subtree of a node contains only nodes with keys strictly greater than the node's key.
// Both the left and right subtrees must also be binary search trees.




var isValidBST = function(curr, lo = null, hi = null) {
    if (!curr) return true;
    if ((lo !== null && curr.val <= lo) || (hi !== null && curr.val >= hi))
        return false;
    let isLeftBST = isValidBST(curr.left, lo, curr.val);
    let isRightBST = isValidBST(curr.right, curr.val, hi);
    return isLeftBST && isRightBST;
}