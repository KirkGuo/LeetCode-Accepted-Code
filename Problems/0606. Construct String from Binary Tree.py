# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        return self.helper(t)
    
    def helper(self, t):
        if not t:
            return ''
        left = self.helper(t.left)
        right = self.helper(t.right)
        if left and right:
            return str(t.val)+'('+left+')('+right+')'
        if left:
            return str(t.val)+'('+left+')'
        if right:
            return str(t.val)+'()'+'('+right+')'
        return str(t.val)
