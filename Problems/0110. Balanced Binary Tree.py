# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self, root):
        if not root:
            return True, 0
        leftBal, leftHeight = self.getHeight(root.left)
        if not leftBal:
            return False, 0
        rightBal, rightHeight = self.getHeight(root.right)
        if not rightBal:
            return False, 0
        if abs(leftHeight-rightHeight)>1:
            return False, 0
        return True, max(leftHeight, rightHeight) + 1
    def isBalanced(self, root: TreeNode) -> bool:
        return self.getHeight(root)[0]
        
        
        
