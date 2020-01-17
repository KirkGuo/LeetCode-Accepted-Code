class Solution:
    class node:
        def __init__(self, val=None):
            self.val = val
            self.left = None
            self.right = None
            self.cnt = 0
            
    def __init__(self):
        self.root = None
    
    def addNode(self, node, val):
        if not self.root:
            self.root = self.node(val)
            return 0
        if node.val>=val:
            node.cnt += 1
            if not node.left:
                node.left = self.node(val)
                return 0
            return self.addNode(node.left, val)
        if not node.right:
            node.right = self.node(val)
            return node.cnt + 1
        return node.cnt + 1 + self.addNode(node.right, val)
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0 for each in nums]
        for i in range(len(nums)-1, -1, -1):
            ans[i] = self.addNode(self.root, nums[i])
        return ans
