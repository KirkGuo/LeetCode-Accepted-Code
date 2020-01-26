# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lvl = []
    
    @staticmethod
    def helper(self, root, pos, lvl):
        if not root:
            return
        if lvl>=len(self.lvl):
            self.lvl.append([pos, pos])
        self.lvl[lvl][0] = min(self.lvl[lvl][0], pos)
        self.lvl[lvl][1] = max(self.lvl[lvl][1], pos)
        Solution.helper(self,root.left, pos*2, lvl+1)
        Solution.helper(self,root.right, pos*2+1, lvl+1)
        
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        Solution.helper(self, root, 0, 0)
        return max([each[1]-each[0] for each in self.lvl]) + 1
