# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = -float("inf")
    
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        curr = root.val
        if left>0:
            curr += left
        if right>0:
            curr += right
        self.ans = max(self.ans, curr)
        return max(max(left, right)+root.val, root.val)
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.ans
