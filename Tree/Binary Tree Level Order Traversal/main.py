from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        result = []
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(level)
        
        return result
    
    
    
# recursion

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        ans = []

        def dfs(node, level):
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        return ans


