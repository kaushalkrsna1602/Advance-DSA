var zigzagLevelOrder = function(root) {
    if (!root) return [];
    let ans = [];
    let q = [root];
    let level = 0;
    while (q.length) {
        let levelArr = [];
        let levelSize = q.length;
        for (let i = 0; i < levelSize; i++) {
            let curr = q.shift();
            if (level % 2 === 0) {
                levelArr.push(curr.val);
            } else {
                levelArr.unshift(curr.val);
            }
            if (curr.left) q.push(curr.left);
            if (curr.right) q.push(curr.right);
        }
        ans.push(levelArr);
        level++;
    }
    return ans;
};