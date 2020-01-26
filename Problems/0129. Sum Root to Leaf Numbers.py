# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
    
    def helper(self, root, prev):
        if not root.left and not root.right:
            curr = prev*10+root.val
            self.ans += curr
            return
        curr = curr = prev*10+root.val
        if root.left:
            self.helper(root.left, curr)
        if root.right:
            self.helper(root.right, curr)
    def sumNumbers(self, root: TreeNode) -> int:
        if root:
            self.helper(root, 0)
        return self.ans
