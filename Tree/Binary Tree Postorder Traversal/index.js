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