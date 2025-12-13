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


var hasPathSum3 = function(root, targetSum) {
    if (root === null) {
        return false;
    }

    let ans = false;

    function traverse(curr, currSum) {
        if (curr === null || ans) return;

        const newSum = currSum + curr.val;

        if (curr.left === null && curr.right === null) {
            if (newSum === targetSum) {
                ans = true;
                return;
            }
        }

        if (curr.left !== null) {
            traverse(curr.left, newSum);
        }
        if (curr.right !== null) {
            traverse(curr.right, newSum);
        }
    }

    traverse(root, 0);
    return ans;
};
