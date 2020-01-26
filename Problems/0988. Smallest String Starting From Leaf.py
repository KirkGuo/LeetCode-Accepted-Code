# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = ''
    
    def helper(self, root, prev):
        if not root.left and not root.right:
            curr = chr(root.val + ord('a')) + prev
            if not self.ans:
                self.ans = curr
            self.ans = min(self.ans, curr)
            return
        curr = chr(root.val + ord('a')) + prev
        if root.left:
            self.helper(root.left, curr)
        if root.right:
            self.helper(root.right, curr)
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if root:
            self.helper(root, '')
        return self.ans
