# Balanced Binary Tree 110


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def calculate_height(curr):
            nonlocal ans
            if not curr:
                return 0

            left_height = calculate_height(curr.left)
            right_height = calculate_height(curr.right)

            if abs(left_height - right_height) > 1:
                ans = False

            return 1 + max(left_height, right_height)

        calculate_height(root)
        return ans
