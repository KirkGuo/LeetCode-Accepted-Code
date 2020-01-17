# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flat(root)
    
    def flat(self, node):
        if not node:
            return None, None
        if not node.left and not node.right:
            return node, node
        if not node.left:
            return node, self.flat(node.right)[1]
        if not node.right:
            head, tail = self.flat(node.left)
            node.left = None
            node.right = head
            return node, tail
        left, right = node.left, node.right
        front, tail = self.flat(left)
        node.left = None
        node.right = front
        tail.left = None
        tail.right, tail = self.flat(right)
        return node, tail
