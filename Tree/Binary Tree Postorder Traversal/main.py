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
        
        
        
def postorderTraversal(root):
    if not root:
        return []
    s1 = [root]
    s2 = []

    while s1:
        curr = s1.pop()
        s2.append(curr)
        if curr.left:
            s1.append(curr.left)
        if curr.right:
            s1.append(curr.right)

    ans = []
    while s2:
        ans.append(s2.pop().val)
    return ans


#one stack 

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        ans = []
        lastVisited = None
        while curr or len(stack):
            while curr:
                stack.append(curr)
                curr = curr.left
            peek = stack[len(stack) - 1]
            if peek.right and peek.right != lastVisited:
                curr = peek.right
            else:
                ans.append(peek.val)
                lastVisited = stack.pop()
        return ans
