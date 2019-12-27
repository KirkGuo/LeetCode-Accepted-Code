"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        head, tail = self.helper(root)
        tail.right = head
        head.left = tail
        return head
        
    
    def helper(self, root):
        if root==None:
            return [None, None]
        if root.left==root.right==None:
            return [root, root]
        if root.left==None:
            head, tail = self.helper(root.right)
            root.right = head
            head.left = root
            return [root, tail]
        if root.right==None:
            head, tail = self.helper(root.left)
            tail.right = root
            root.left = tail
            return [head, root]
        head1, tail1 = self.helper(root.left)
        head2, tail2 = self.helper(root.right)
        tail1.right = root
        root.left = tail1
        root.right = head2
        head2.left = root
        return [head1, tail2]
