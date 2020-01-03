# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        cnt = collections.defaultdict(list)
        def markTree(root):
            if not root:
                return 0
            dep = max(markTree(root.left), markTree(root.right)) + 1
            cnt[dep].append(root.val)
            return dep
        
        markTree(root)
        
        return [cnt[each] for each in cnt.keys()]
