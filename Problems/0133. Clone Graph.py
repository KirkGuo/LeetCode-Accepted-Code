"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        self.node = node
        self.new_node = None
        self.newed = {}
        
        self.helper()
        
        return self.new_node
    
    def helper(self):
        self.new_node = self.dfs(self.node)
        return
    
    def dfs(self, node):
        if node is None:
            return None
        
        val, neighbors = node.val, node.neighbors
        
        if val in self.newed:
            return self.newed[val]
        
        self.newed[val] = Node(val)
        
        if neighbors is None:
            return self.newed[val]
        
        self.newed[val].neighbors = []
        for each in neighbors:
            self.newed[val].neighbors.append(self.dfs(each))
        return self.newed[val]
