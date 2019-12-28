# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = collections.defaultdict(list)
        
        if not root:
            return [each for each in q]
        
        q[0] = [root]
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
        return [[each.val for each in q[lvl]] for lvl in q]
