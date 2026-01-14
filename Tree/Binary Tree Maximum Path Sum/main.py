class Solution:
    def maxPathSum(self, root):
        self.maxSumPath = float('-inf')       
        def traversal(node):
            if not node:
                return 0
            maxLeft = max(0, traversal(node.left))
            maxRight = max(0, traversal(node.right))
            currMax = node.val + maxLeft + maxRight
            self.maxSumPath = max(self.maxSumPath, currMax)
            return node.val + max(maxLeft, maxRight)
        traversal(root)
        return self.maxSumPath