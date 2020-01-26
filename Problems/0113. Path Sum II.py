# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def helper(self, root, tgt, curr, path):
        if not root.left and not root.right:
            if curr+root.val==tgt:
                self.ans.append(path+[root.val])
            return
        if root.left:
            self.helper(root.left, tgt, curr+root.val, path+[root.val])
        if root.right:
            self.helper(root.right, tgt, curr+root.val, path+[root.val])

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root:
            self.helper(root, sum, 0, [])
        return self.ans
