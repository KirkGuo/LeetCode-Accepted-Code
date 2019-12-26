# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        s, ans = [], []
        curr = root
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans
