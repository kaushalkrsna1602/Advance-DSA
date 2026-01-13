class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
def connect(root):
    if not root:
        return root
    def traversal(curr):
        if curr.left:
            curr.left.next = curr.right
        if curr.right and curr.next:
            curr.right.next = curr.next.left
        if curr.left:
            traversal(curr.left)
        if curr.right:
            traversal(curr.right)
    traversal(root)
    return root