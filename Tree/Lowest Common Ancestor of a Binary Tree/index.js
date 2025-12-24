// 236 Lowest Common Ancestor of a Binary Tree

var lowestCommonAncestor = function(root, p, q) {
    let lca = null;
    let traversal = (curr) => {
        let count = 0;
        if(!curr) return 0;
        let ansOnLeft = traversal(curr.left);
        let ansOnRight = traversal(curr.right);
        if(curr.val === p.val || curr.val === q.val) {
            ++count;
        } 
        count = count + ansOnLeft + ansOnRight;
        if(count === 2 && !lca) {
            lca = curr;
        }
        return count;
    }
    traversal(root);
    return lca;
};    