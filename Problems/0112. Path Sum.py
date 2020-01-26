# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, curr, tgt):
        if not root.left and not root.right:
            return curr+root.val==tgt
        if not root.left:
            return self.helper(root.right, curr+root.val, tgt)
        if not root.right:
            return self.helper(root.left, curr+root.val, tgt)
        return self.helper(root.left, curr+root.val, tgt) or self.helper(root.right, curr+root.val, tgt)
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.helper(root, 0, sum)
