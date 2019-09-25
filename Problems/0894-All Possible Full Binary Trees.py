# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ret = []
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N%2==0:
            return []
        self.ret = [[] for i in range(N+1)]
        self.ret[0] = []
        self.ret[1] = [TreeNode(0)]
        for i in range(3, N+1, 2):
            for left in range(1, i-1, 2):
                right = i-1-left
                for each_left in self.ret[left]:
                    for each_right in self.ret[right]:
                        root = TreeNode(0)
                        root.left = each_left
                        root.right = each_right
                        self.ret[i].append(root)
        return self.ret[N] 
