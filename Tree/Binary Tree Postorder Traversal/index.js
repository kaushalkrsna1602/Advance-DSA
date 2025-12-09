function inorderTransversal(root) {
    let ans = []
    function transversal(curr) {
        if (!curr) return
        transversal(curr.left)
        transversal(curr.right)
        ans.push(curr.val)
    }
    transversal(root)
    return ans
}

// iterative approach 2 stack

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
var postorderTraversal = function(root) {
    if(!root) return []
    let s1 = [root]
    let s2 = []
    while(s1.length){
        let curr = s1.pop()
        s2.push(curr)
        curr.left && s1.push(curr.left)
        curr.right && s1.push(curr.right)
    }
    let ans = []
    while(s2.length){
        ans.push(s2.pop().val)
    }
    return ans
};




// one stack 

var postorderTraversal = function(root) {
    let stack = [];
    let curr = root;
    let ans = [];
    let lastVisited = null;
    while(curr || stack.length) {
        while(curr) {
            stack.push(curr);
            curr = curr.left;
        }
        let peek = stack[stack.length - 1];
        if(peek.right && peek.right != lastVisited){
            curr = peek.right;
        } else {
            ans.push(peek.val);
            lastVisited = stack.pop();
        }
    }
    return ans;
};