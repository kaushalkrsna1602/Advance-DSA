# Subtree of Another Tree 72

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def serialize(self, root):
        hash = []
        def dfs(node):
            if not node:
                hash.append("-#")
                return
            hash.append("-" + str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ''.join(hash)

    def isSubtree(self, root, subRoot):
        hashRoot = self.serialize(root)
        hashSubRoot = self.serialize(subRoot)
        return hashSubRoot in hashRoot