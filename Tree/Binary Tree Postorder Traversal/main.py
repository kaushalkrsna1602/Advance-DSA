# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def transversal(curr):
            if not curr: return 
            transversal(curr.left)
            transversal(curr.right)
            ans.append(curr.val)
        transversal(root)
        return ans
        