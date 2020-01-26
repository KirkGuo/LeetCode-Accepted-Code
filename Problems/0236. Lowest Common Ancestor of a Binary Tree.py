# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.path_p = []
        self.path_q = []
    
    def helper(self, root, path, p, q):
        if not root:
            return
        if root==p:
            self.path_p = path + [p]
        if root==q:
            self.path_q = path + [q]
        self.helper(root.left, path+[root], p, q)
        self.helper(root.right, path+[root], p, q)
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.helper(root, [], p, q)
        ans = None
        while self.path_p and self.path_q and self.path_p[0]==self.path_q[0]:
            ans = self.path_p.pop(0)
            self.path_q.pop(0)
        return ans
