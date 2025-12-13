var hasPathSum = function(root, targetSum) {
    if (root === null) return false;

    // If it's a leaf node
    if (root.left === null && root.right === null) {
        return targetSum === root.val;
    }

    return (
        hasPathSum(root.left, targetSum - root.val) ||
        hasPathSum(root.right, targetSum - root.val)
    );
};
