// 572 Subtree of Another Tree

var isSubtree = function(root, subRoot) {
    let hashRoot = serialize(root);
    let hashSubRoot = serialize(subRoot);

    return hashRoot.includes(hashSubRoot);
};
let serialize = function(root) {
    let hash = "";
    let traversal = (curr) => {
        if(!curr) {
            hash = hash + "-#";
            return;
        }
        hash = hash + "-" + curr.val;
        traversal(curr.left);
        traversal(curr.right);
    }
    traversal(root);
    return hash;
}   