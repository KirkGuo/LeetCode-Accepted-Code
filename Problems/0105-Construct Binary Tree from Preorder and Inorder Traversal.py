# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        left_inorder, right_inorder = inorder[:idx], inorder[idx+1:]
        root.left = self.buildTree(preorder[1:1+len(left_inorder)], left_inorder)
        root.right = self.buildTree(preorder[len(preorder)-len(right_inorder):], right_inorder)
        return root   
