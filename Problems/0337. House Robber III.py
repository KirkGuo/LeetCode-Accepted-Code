# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.helper(root, False)
    
    def helper(self, root, robbed):
        if not root:
            return 0
        
        if hasattr(root, 'rob'):
            if robbed:
                return root.n_rob
            return max(root.rob, root.n_rob)
        
        n_rob = self.helper(root.left, False) + self.helper(root.right, False)
        root.n_rob = n_rob
        if robbed:
            return n_rob
        rob = self.helper(root.left, True) + self.helper(root.right, True) + root.val
        root.rob = rob
        
        return max(rob, n_rob)
