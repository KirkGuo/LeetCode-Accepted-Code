class UnionFindSet:
    
    def __init__(self, data):
        self.data = {k: v for v, k in enumerate(data)}
        self.index = [i for i, _ in enumerate(data)]
        
    def __is_root(self, idx):
        return self.index[idx] == idx
    
    def find_parent(self, idx):
        if self.__is_root(idx):
            return idx
        self.index[idx] = self.find_parent(self.index[idx])
        return self.index[idx]
    
    def merge_parent(self, x, y):
        parent_x, parent_y = self.find_parent(x), self.find_parent(y)
        if parent_x != parent_y:
            self.index[x] = parent_y
    
    def is_same_root(self, x, y):
        return self.find_parent(x) == self.find_parent(y)
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        unionFind = UnionFindSet(nums_set)
        for each in nums_set:
            if each+1 in nums_set:
                unionFind.merge_parent(unionFind.data[each],  unionFind.data[each+1])
            if each-1 in nums_set:
                unionFind.merge_parent(unionFind.data[each],  unionFind.data[each-1])
                
        parents = collections.Counter()
        for i, _ in enumerate(nums_set):
            parents.update([unionFind.find_parent(i)])
        return sorted(parents.items(), key=lambda x:-x[1])[0][1]
        
        
