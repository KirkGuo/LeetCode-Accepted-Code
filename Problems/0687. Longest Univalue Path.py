# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
    
    def helper(self, root):
        if not root:
            return 0   
        left = self.helper(root.left)
        right = self.helper(root.right)
        left = left+1 if root.left and root.val==root.left.val else 0
        right = right+1 if root.right and root.val==root.right.val else 0
        self.ans = max(self.ans, left+right)
        return max(left, right)
    
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.helper(root)
        return self.ans
