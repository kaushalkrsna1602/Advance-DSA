class Solution:
    def diameterOfBinaryTree(self, root):
        self.maxDiameter = 0

        def findDepth(node):
            if not node:
                return 0
            left = findDepth(node.left)
            right = findDepth(node.right)
            self.maxDiameter = max(self.maxDiameter, left + right)
            return 1 + max(left, right)
        findDepth(root)
        return self.maxDiameter