# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def __init__(self):
        self.nodes = []
        
    def helper(self, nestedList, height):
        lst = []
        integers = []
        for each in nestedList:
            if each.isInteger():
                integers.append(each.getInteger())
            else:
                lst.append(each.getList())
        if len(self.nodes)<=height:
            self.nodes.append([])
        self.nodes[height] += integers
        for each in lst:
            self.helper(each, height+1)
    
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.helper(nestedList, 0)
        idx = 0
        ans = 0
        while self.nodes:
            item = self.nodes.pop()
            idx += 1
            for each in item:
                ans += each*idx
        return ans
