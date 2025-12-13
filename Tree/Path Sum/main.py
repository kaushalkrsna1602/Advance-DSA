# 112 Path Sum

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        ans = False

        def traverse(curr, currSum):
            nonlocal ans
            newSum = currSum + curr.val

            if not curr.left and not curr.right:
                if newSum == targetSum:
                    ans = True
                    return

            if curr.left:
                traverse(curr.left, newSum)
            if curr.right:
                traverse(curr.right, newSum)

        traverse(root, 0)
        return ans



# Bottom's Up

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )
