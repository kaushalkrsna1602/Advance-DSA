# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_depth = 0

        def traverse(node, depth):
            self.max_depth = max(self.max_depth, depth)
            if node.left:
                traverse(node.left, depth + 1)
            if node.right:
                traverse(node.right, depth + 1)

        traverse(root, 1)
        return self.max_depth




#bottoms up



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return 1 + max(left_max, right_max)
