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




var hasPathSum2 = function(root, targetSum) {
    if (root === null) return false;

    const stack = [[root, targetSum]];

    while (stack.length > 0) {
        const [node, currSum] = stack.pop();

        if (node.left === null && node.right === null) {
            if (currSum === node.val) return true;
        }

        if (node.right !== null) {
            stack.push([node.right, currSum - node.val]);
        }
        if (node.left !== null) {
            stack.push([node.left, currSum - node.val]);
        }
    }

    return false;
};
