var isBalanced = function(root) {
    let ans = true;

    function calculateHeight(curr) {
        if (!curr) return 0;

        const leftHeight = calculateHeight(curr.left);
        const rightHeight = calculateHeight(curr.right);

        if (Math.abs(leftHeight - rightHeight) > 1) {
            ans = false;
        }

        return 1 + Math.max(leftHeight, rightHeight);
    }

    calculateHeight(root);
    return ans;
};
