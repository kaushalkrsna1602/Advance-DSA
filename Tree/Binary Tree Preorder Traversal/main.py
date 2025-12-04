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

        