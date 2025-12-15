// 101 Symmetric Tree

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
 * @return {boolean}
 */
var isSymmetric = function(root) {
    let isMirror = (left, right) => {
        if(!left && !right) return true
        if(!left || !right) return false

        return left.val === right.val &&
                isMirror(left.left, right.right) &&
                isMirror(left.right, right.left)

    }
    return isMirror(root.left, root.right)
};

// Iterative approach

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
 * @return {boolean}
 */
var isSymmetric = function(root) {
    let q = [root.left, root.right]

    while(q.length){
        let p1 = q.shift()
        let p2 = q.shift()

        if(!p1 && !p2) continue;

        if(!p1 || !p2) return false

        if(p1.val != p2.val) return false

        q.push(p1.left, p2.right)
        q.push(p1.right, p2.left)
    }
    return true
};