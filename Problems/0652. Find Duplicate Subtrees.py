# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.mem = set()
        self.added = set()
        self.ans = []
    
    def helper(self, root):
        if not root:
            return [None]
        left = self.helper(root.left)
        right = self.helper(root.right)
        curr = [root.val]+left+right
        code = tuple(curr)
        if code in self.mem and code not in self.added:
            self.added.add(code)
            self.ans.append(root)
        else:
            self.mem.add(code)
        return curr

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.helper(root)
        return self.ans
