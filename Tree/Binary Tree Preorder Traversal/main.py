# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traversal(curr):
            if not curr: return 
            ans.append(curr.val)
            traversal(curr.left)
            traversal(curr.right)
        traversal(root)
        return ans

        
        
# iterative approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        stack = [root]
        while len(stack):
            curr = stack.pop()
            ans.append(curr.val)
            curr.right and stack.append(curr.right)
            curr.left and stack.append(curr.left)
        return ans
        