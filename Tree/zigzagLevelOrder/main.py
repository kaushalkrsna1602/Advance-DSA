
from collections import deque

def zigzagLevelOrder(root):
    if not root:
        return []
    res = []
    q = deque([root])
    level = 0
    while q:
        size = len(q)
        level_nodes = deque()
        for _ in range(size):
            node = q.popleft()
            if level % 2 == 0:
                level_nodes.append(node.val)
            else:
                level_nodes.appendleft(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(list(level_nodes))
        level += 1
    return res