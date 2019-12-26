# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        s, ans = [root, ], []
        while s:
            tmp = s.pop()
            ans.append(tmp.val)
            if tmp.left:
                s.append(tmp.left)
            if tmp.right:
                s.append(tmp.right)
        return ans[::-1]
