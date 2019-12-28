# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.defaultdict(list)
        q[0].append(root)
        
        flag = True
        idx = 0
        
        while flag:
            flag = False
            for each in q[idx]:
                if each.left:
                    q[idx+1].append(each.left)
                    flag = True
                if each.right:
                    q[idx+1].append(each.right)
                    flag = True
            idx += 1
            
        return [[each.val for each in q[lvl]] if not lvl%2 else [each.val for each in q[lvl]][::-1] for lvl in q]
