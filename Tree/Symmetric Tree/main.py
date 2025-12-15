# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (
                left.val == right.val and
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left)
            )

        return isMirror(root.left, root.right)


# Iterative

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root.left, root.right])

        while q:
            p1 = q.popleft()
            p2 = q.popleft()

            if not p1 and not p2:
                continue

            if not p1 or not p2:
                return False

            if p1.val != p2.val:
                return False

            q.append(p1.left)
            q.append(p2.right)
            q.append(p1.right)
            q.append(p2.left)

        return True
