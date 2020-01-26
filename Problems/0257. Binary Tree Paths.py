# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = []
    def helper(self, root, path):
        if not root.left and not root.right:
            self.ans.append(path+'->'+str(root.val) if path else str(root.val))
        if root.left:
            self.helper(root.left, path+'->'+str(root.val) if path else str(root.val))
        if root.right:
            self.helper(root.right, path+'->'+str(root.val) if path else str(root.val))
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            self.helper(root, '')
        return list(self.ans)
