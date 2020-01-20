# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
    
    def isUnivalSubtree(self, root):
        if not root:
            return False
        if not root.left and not root.right:
            self.ans += 1
            return True
        if not root.left:
            if self.isUnivalSubtree(root.right) and root.val==root.right.val:
                self.ans += 1
                return True
            else:
                return False
        if not root.right:
            if self.isUnivalSubtree(root.left) and root.val==root.left.val:
                self.ans += 1
                return True
            else:
                return False
        left = self.isUnivalSubtree(root.left)
        right = self.isUnivalSubtree(root.right)
        if not left or not right:
            return False
        if root.val!=root.left.val or root.val!=root.right.val:
            return False
        self.ans += 1
        return True
            
        
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.isUnivalSubtree(root)
        return self.ans
